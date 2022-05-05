import os, sys
import shutil


def cleanDir():
    n = int(input())

    shutil.rmtree("./"+str(n)+"/longitudes")
    os.mkdir("./"+str(n)+"/longitudes")
    shutil.rmtree("./"+str(n)+"/longlat")
    os.mkdir("./"+str(n)+"/longlat")

def createDirs():
    for i in range(40, 62, 2):
        os.mkdir(str(i))
        os.mkdir(str(i) + "/longlat")
        os.mkdir(str(i) + "/longitudes")

def removeDirs():
    for i in range(40, 62, 2):
        shutil.rmtree(str(i))


def resetDirs():
    removeDirs()
    createDirs()


def main():
    os.chdir("./results")
    cmd = input().strip()
    if cmd == "create":
        createDirs()
    elif cmd == "clean":
        cleanDir()
    elif cmd == "remove":
        removeDirs()
    elif cmd == "reset":
        resetDirs()
    else:
        print("wrong command!", file=sys.stderr)



if __name__ == "__main__":
    main()