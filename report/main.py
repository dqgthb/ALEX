import os
import sys

of = open("result.txt", 'w')
sys.stdout = of

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
    cmd = input().strip()

    if cmd == "all":
        for i in range(40, 62, 2):
            print("TESTCASE" + str(i))
            reportDirectory("../results/" + str(i) + "/longitudes/")
            reportDirectory("../results/" + str(i) + "/longlat/")
            print()

    else:
        num = int(cmd)
        assert 40 <= num <= 60, "Not in range!"
        reportDirectory("../results/" + str(num) + "/longitudes/")
        reportDirectory("../results/" + str(num) + "/longlat/")






if __name__ == "__main__":
    main()