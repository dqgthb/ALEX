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


def makeIncreasingDenseDoubles(iFileName, oFileName, *, iDataNum):
    if exists(oFileName):
        print(oFileName, "already exists.", file = sys.stderr)
        return
    print("Creating", oFileName)
    nums = dataIO.readDoubles(iFileName, iDataNum)
    nums = dataIO.makeIncreasingDenseDoubles(nums)
    dataIO.writeDoubles(oFileName, nums)


def makeIncreasingNums(iFileName, oFileName, *, iDataNum, step):
    if exists(oFileName):
        print(oFileName, "already exists.", file = sys.stderr)
        return
    print("Creating", oFileName)
    nums = dataIO.readDoubles(iFileName, iDataNum)
    nums = dataIO.makeIncreasingNums(nums, step=step)
    dataIO.writeDoubles(oFileName, nums)


def makeDecreasingDenseDoubles(iFileName, oFileName, *, iDataNum):
    if exists(oFileName):
        print(oFileName, "already exists.", file = sys.stderr)
        return
    print("Creating", oFileName)
    nums = dataIO.readDoubles(iFileName, iDataNum)
    nums = dataIO.makeDecreasingDenseDoubles(nums)
    dataIO.writeDoubles(oFileName, nums)


def makeSortedDoubles(iFileName, oFileName, *, iDataNum):
    if exists(oFileName):
        print(oFileName, "already exists.", file = sys.stderr)
        return
    print("Creating", oFileName)
    nums = dataIO.readDoubles(iFileName, iDataNum)
    nums = dataIO.makeSortedDoubles(nums)
    dataIO.writeDoubles(oFileName, nums)





### def makeLogNormal():
###     iFileName = "../resources/lognormal-190M.bin.data"
###     oFileName = "../resources/concentrated/lognormal.bin"
###
###
### def makeYcmb():
###     iFileName = "../resources/ycsb-200M.bin.data"
###     oFileName = "../resources/concentrated/ycmb.bin"


def makeLongitudes():
    iFileName = "../resources/longitudes-200M.bin.data"
    oFileName = "../resources/longitudes/longitudes"
    makeConcentratedDoubles(iFileName, oFileName + "25%.bin", iDataNum=10000000, percentile = 0.25)
    makeConcentratedDoubles(iFileName, oFileName + "50%.bin", iDataNum=10000000, percentile = 0.50)
    makeConcentratedDoubles(iFileName, oFileName + "75%.bin", iDataNum=10000000, percentile = 0.75)
    makeIncreasingDenseDoubles(iFileName, "../resources/longitudes/longitudesIncreasing.bin", iDataNum=10000000)
    makeIncreasingNums(iFileName, "../resources/longitudes/increaseBy1.bin", iDataNum=10000000, step=1)
    makeDecreasingDenseDoubles(iFileName, "../resources/longitudes/longitudesDecreasing.bin", iDataNum=10000000)
    makeSortedDoubles(iFileName, "../resources/longitudes/sorted.bin", iDataNum=20000000)


def makeLonglat():
    iFileName = "../resources/longlat-200M.bin.data"
    oFileName = "../resources/longlat/longlat"
    makeConcentratedDoubles(iFileName, oFileName + "25%.bin", iDataNum=10000000, percentile = 0.25)
    makeConcentratedDoubles(iFileName, oFileName + "50%.bin", iDataNum=10000000, percentile = 0.5000001)
    makeConcentratedDoubles(iFileName, oFileName + "75%.bin", iDataNum=10000000, percentile = 0.75)
    makeIncreasingDenseDoubles(iFileName, "../resources/longlat/longlatIncreasing.bin", iDataNum=10000000)
    makeIncreasingNums(iFileName, "../resources/longlat/increaseBy1.bin", iDataNum=10000000, step=1)
    makeDecreasingDenseDoubles(iFileName, "../resources/longlat/longlatDecreasing.bin", iDataNum=10000000)
    makeSortedDoubles(iFileName, "../resources/longlat/sorted.bin", iDataNum=20000000)


def main():

    print("making longitudes")
    makeLongitudes() # 8 byte double

    print("making longlat")
    makeLonglat() # 8 byte double

    # cannot make concentrated data for int data types.
    # makeYcmb() # 8 byte unsigned int
    # makeLogNormal() # 8 byte signed int



if __name__ == "__main__":
    main()