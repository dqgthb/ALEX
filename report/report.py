from collections import defaultdict
import os
from statistics import mean
import sys
from contextlib import ExitStack

from numpy import average

#of = open("result.txt", 'w')
#sys.stdout = of

QuantileData = defaultdict(dict)

def reportFile(fileName, lineNum):
    with open(fileName, encoding='utf-8') as f:
        lines = f.readlines()
        print(">>>", fileName)
        print(''.join(lines[-lineNum:]))


def reportDirectory(dirName, dataName):
    print("################################################")
    print("directory:", dirName)
    print("################################################")
    assert(dirName[-1] == '/')

    for obj in os.listdir(dirName):
        if os.path.isfile(dirName+obj):
            reportFile(dirName+obj, 1)
    try:
        calculateAverageOf3Quantiles(dirName, dataName)
    except:
        pass


def calculateAverageOf3Quantiles(dirName, dataName):
    fn25 = dirName + dataName + "25%.txt"
    fn50 = dirName + dataName + "50%.txt"
    fn75 = dirName + dataName + "75%.txt"
    filenames = [fn25, fn50, fn75]

    with ExitStack() as stack:
        files = [stack.enter_context(open(fname)) for fname in filenames]

        numInserts = []
        for file in files:
            numInserts.append(float(file.readlines()[-1].split()[4]))
        print(' + '.join(str(i) for i in numInserts), "=", sum(numInserts))
        print("Average of 25, 50, 75% quantile inserts are:", mean(numInserts), "inserts per second.")
        #print(dirName, ":", mean(numInserts), file=sys.stderr)

        QuantileData[dataName][dirName] = mean(numInserts)


def main():
    print("all? Number (40 <= x <= 60)?", file=sys.stderr)
    cmd = input().strip()

    if cmd == "all":
        for i in range(40, 62, 2):
            print("TESTCASE" + str(i))
            reportDirectory("../results/" + str(i) + "/longitudes/", "longitudes")
            reportDirectory("../results/" + str(i) + "/longlat/", "longlat")
            print()

        names = [
            "min60max75",
            "min60max70",
            "min60max65",
            "min55max75",
            "min50max70",
            "min45max65",
        ]

        for name in names:
            print("TESTCASE" + name)
            reportDirectory("../results/" + name + "/longitudes/", "longitudes")
            reportDirectory("../results/" + name + "/longlat/", "longlat")
            print()

    elif "min" in cmd:
        assert "max" in cmd, "Wrong command!"
        reportDirectory("../results/" + (cmd) + "/longitudes/", "longitudes")
        reportDirectory("../results/" + (cmd) + "/longlat/", "longlat")

    else:
        num =int(cmd)
        assert 40 <= num <= 60, "Not in range!"
        reportDirectory("../results/" + str(num) + "/longitudes/", "longitudes")
        reportDirectory("../results/" + str(num) + "/longlat/", "longlat")

    for dataName in QuantileData:
        print("#####")
        print(dataName, "25, 50, 75% quantile concentrated average result:")
        for data in QuantileData[dataName]:
            print(data, QuantileData[dataName][data])
        print()
    print("Report finished.", file=sys.stderr)




if __name__ == "__main__":
    main()