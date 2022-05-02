from dataIO import *



def makeLongitudes():

    iFileName = "../resources/longitudes-200M.bin.data"
    oFileName = "../resources/concentrated/longitudes.bin"




def makeLogNormal():
    iFileName = "../resources/lognormal-190M.bin.data"
    oFileName = "../resources/concentrated/lognormal.bin"


def makeYcmb():
    iFileName = "../resources/ycsb-200M.bin.data"
    oFileName = "../resources/concentrated/ycmb.bin"


def main():


    makeLongitudes()

    makeYcmb()

    makeLogNormal()



if __name__ == "__main__":
    main()