import dataIO
import sys
from os.path import exists


def makeConcentratedDoubles(iFileName, oFileName, *, iDataNum, percentile):
    # assert not exists(oFileName)
    if exists(oFileName):
        print(oFileName, "already exists.", file = sys.stderr)
        return
    print("Creating", oFileName)
    nums = dataIO.readDoubles(iFileName, iDataNum)
    nums = dataIO.makeConcentratedDoubles(nums, percentile=percentile)
    dataIO.writeDoubles(oFileName, nums)


def makeIncreasingDoubles(iFileName, oFileName, *, iDataNum):
    if exists(oFileName):
        print(oFileName, "already exists.", file = sys.stderr)
        return
    print("Creating", oFileName)
    nums = dataIO.readDoubles(iFileName, iDataNum)
    nums = dataIO.makeIncreasingDoubles(nums)
    dataIO.writeDoubles(oFileName, nums)


### def makeLogNormal():
###     iFileName = "../resources/lognormal-190M.bin.data"
###     oFileName = "../resources/concentrated/lognormal.bin"
###
###
### def makeYcmb():
###     iFileName = "../resources/ycsb-200M.bin.data"
###     oFileName = "../resources/concentrated/ycmb.bin"


def makeLonglat():
    iFileName = "../resources/longlat-200M.bin.data"
    oFileName = "../resources/longlat/longlat"
    makeConcentratedDoubles(iFileName, oFileName + "25%.bin", iDataNum=10000000, percentile = 0.25)
    makeConcentratedDoubles(iFileName, oFileName + "50%.bin", iDataNum=10000000, percentile = 0.5000001)
    makeConcentratedDoubles(iFileName, oFileName + "75%.bin", iDataNum=10000000, percentile = 0.75)

    makeIncreasingDoubles(iFileName, "../resources/longlat/longlatIncreasing.bin", iDataNum=10000000)


def makeLongitudes():
    iFileName = "../resources/longitudes-200M.bin.data"
    oFileName = "../resources/longitudes/longitudes"
    makeConcentratedDoubles(iFileName, oFileName + "25%.bin", iDataNum=10000000, percentile = 0.25)
    makeConcentratedDoubles(iFileName, oFileName + "50%.bin", iDataNum=10000000, percentile = 0.50)
    makeConcentratedDoubles(iFileName, oFileName + "75%.bin", iDataNum=10000000, percentile = 0.75)

    makeIncreasingDoubles(iFileName, "../resources/longitudes/longitudesIncreasing.bin", iDataNum=10000000)



def main():

    makeLonglat() # 8 byte double
    makeLongitudes() # 8 byte double

    # cannot make concentrated data for int data types.
    # makeYcmb() # 8 byte unsigned int
    # makeLogNormal() # 8 byte signed int



if __name__ == "__main__":
    main()