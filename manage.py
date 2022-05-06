import os, sys
import shutil


def cleanDir():
    print("Which directory to clean?")
    n = input().strip()

    shutil.rmtree("./"+str(n)+"/longitudes")
    os.mkdir("./"+str(n)+"/longitudes")
    shutil.rmtree("./"+str(n)+"/longlat")
    os.mkdir("./"+str(n)+"/longlat")

def createDirs():
    try:
        for i in range(40, 62, 2):
            os.mkdir(str(i))
            os.mkdir(str(i) + "/longlat")
            os.mkdir(str(i) + "/longitudes")
    except:
        pass

    names = [
        "min60max75",
        "min60max70",
        "min60max65",
        "min55max75",
        "min50max70",
        "min45max65",
    ]

    for name in names:
        try:
            os.makedirs("./" + name + "/longitudes")
            os.makedirs("./" + name + "/longlat")
        except:
            pass


def removeDirs():
    for i in range(40, 62, 2):
        shutil.rmtree(str(i))
    shutil.rmtree("./min55max75")
    shutil.rmtree("./min60max75")


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