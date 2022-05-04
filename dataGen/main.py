from dataIO import *
from os.path import exists



def makeLongitudes():

    iFileName = "../resources/longitudes-200M.bin.data"
    oFileName = "../resources/concentrated/longitudes.bin"
    assert not exists(oFileName)
    nums = readDoubles(iFileName, 10000000)
    nums = makeConcentratedDoubles(nums)
    writeDoubles(oFileName, nums)


def makeLogNormal():
    iFileName = "../resources/lognormal-190M.bin.data"
    oFileName = "../resources/concentrated/lognormal.bin"
    assert not exists(oFileName)


def makeYcmb():
    iFileName = "../resources/ycsb-200M.bin.data"
    oFileName = "../resources/concentrated/ycmb.bin"
    assert not exists(oFileName)


def main():

    makeLongitudes() # 8 byte double

    # cannot make concentrated data for int data types.
    # makeYcmb() # 8 byte unsigned int
    # makeLogNormal() # 8 byte signed int



if __name__ == "__main__":
    main()