from collections import defaultdict
import os
from statistics import mean
import sys
from contextlib import ExitStack

from numpy import average

#of = open("result.txt", 'w')
#sys.stdout = of

maxStr = [str(i) for i in range(65, 85, 5)]
minStr = [str(i) for  i in range(60, 80, 5)]

def ddict():
    return defaultdict(ddict)


QuantileData = defaultdict(ddict)
KeyData = defaultdict(ddict)


def reportFile(min_, max_, fileName, dataName, lineNum):
    with open(fileName, encoding='utf-8') as f:
        lines = f.readlines()
        print(">>>", fileName)
        print(''.join(lines[-lineNum:]))

    parseAndCollectKeyData(min_, max_, fileName, dataName, lines)


def reportDirectory(min_, max_, dirName, dataName):
    print("################################################")
    print("directory:", dirName)
    print("################################################")
    assert(dirName[-1] == '/')

    for obj in os.listdir(dirName):
        fileName = dirName + obj
        if os.path.isfile(fileName):
            reportFile(min_, max_, fileName, dataName, 1)



def parseAndCollectKeyData(min_, max_, fileName, dataName, lines):

    for key in ["ordinary", "25%", "50%", "75%"]:
        if key in fileName:
            try:
                numInserts =  float(lines[-1].split()[4])
                KeyData[dataName][min_][max_][key] = numInserts
                break
            except:
                return


def minMax(dataName):

    for i in range(len(minStr)):
        for j in range(i, len(maxStr)):
            min_ = minStr[i]
            max_ = maxStr[j]
            print(i, j, min_, max_)
            dirName = "../results/min" + min_ + "max" + max_ + "/" + dataName + "/"
            reportDirectory(min_, max_, dirName, dataName)




def main(argv):
    cmd = argv[1]

    if cmd == "all":
        print("")
        minMax("longitudes")
        minMax("longlat")


    for dataName in ["longitudes", "longlat"]:
        print()
        print("###############################")
        print(dataName, "#####################")
        print("###############################")
        print()
        print("ordinary ###############################")
        print('\t\t', '\t\t'.join(maxStr))
        for i in range(4):
            print(minStr[i], end='\t\t')
            print('\t\t'*i, end="")
            for j in range(i, 4):
                data = (KeyData[dataName][minStr[i]][maxStr[j]]["ordinary"])
                if type(data) is float:
                    print(data, end='\t')
                else:
                    print("DATA NOT", end='\t')

            print()

        print("quantile ###############################")


        print('\t\t', '\t\t\t\t'.join(maxStr))
        for i in range(4):
            print(minStr[i], end='\t\t')
            print('\t\t\t\t'*i, end="")
            for j in range(i, 4):
                _25 = KeyData[dataName][minStr[i]][maxStr[j]]["25%"]
                _50 = KeyData[dataName][minStr[i]][maxStr[j]]["50%"]
                _75 = KeyData[dataName][minStr[i]][maxStr[j]]["75%"]
                try:
                    print(mean((_25, _50, _75)), end='\t\t')
                except:
                    print("NO VALUE AVAIL", end='\t\t')
            print()


    for dataName in ["longitudes", "longlat"]:
        print()
        print("##########" + dataName + "#########")
        ordinary = KeyData[dataName]["60"]["80"]["ordinary"]
        _25 = KeyData[dataName]["60"]["80"]["25%"]
        _50 = KeyData[dataName]["60"]["80"]["50%"]
        _75 = KeyData[dataName]["60"]["80"]["75%"]
        skewed = mean((_25, _50, _75))
        print("Ordinary:", ordinary)
        print("Skewed:", skewed)
        print("percentage: skewed / ordinary:", skewed / ordinary)
        print()

        _25 = KeyData[dataName]["70"]["80"]["25%"]
        _50 = KeyData[dataName]["70"]["80"]["50%"]
        _75 = KeyData[dataName]["70"]["80"]["75%"]
        newSkewed = mean((_25, _50, _75))

        print("Skewed:", skewed)
        print("7080 Skewed:", newSkewed)
        print("percentage: newSkewed / Skewed:", newSkewed / skewed)

        print("newSkewed / ordinary:", newSkewed / ordinary)



if __name__ == "__main__":
     main(sys.argv)