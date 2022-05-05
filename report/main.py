import os
import sys

of = open("result.txt", 'w')
#sys.stdout = of

def reportFile(fileName, lineNum):
    with open(fileName, encoding='utf-8') as f:
        lines = f.readlines()
        print(">>>", fileName)
        print(''.join(lines[-lineNum:]))


def reportDirectory(dirName):
    print("################################################")
    print("directory:", dirName)
    print("################################################")
    assert(dirName[-1] == '/')

    for obj in os.listdir(dirName):
        if os.path.isfile(dirName+obj):
            reportFile(dirName+obj, 1)


def main():

    reportDirectory("../results/longitudes/")
    reportDirectory("../results/longlat/")




if __name__ == "__main__":
    main()