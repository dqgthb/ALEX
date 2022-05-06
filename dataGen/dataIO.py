import struct
import math
import random
#random.seed(1)


### def readSigned8ByteInt(fileName, n):
###     signedLL = []
###     with open(fileName, "rb") as f:
###         for _ in range(n):
###             x, = struct.unpack('q', f.read(8))
###             signedLL.append(x)
###     return signedLL
###
###
### def writeSigned8ByteInt(fileName, nums):
###     with open(fileName, "wb") as f:
###         for num in nums:
###             binData = struct.pack("q", num)
###             f.write(binData)
###
###
###
###
### def readUnsigned8ByteInt(fileName, n):
###     unsignedLL = []
###     with open(fileName, "rb") as f:
###         for _ in range(n):
###             x, = struct.unpack('Q', f.read(8))
###             unsignedLL.append(x)
###     return unsignedLL
###
###
### def writeUnsigned8ByteInt(fileName, nums):
###     with open(fileName, "wb") as f:
###         for num in nums:
###             binData = struct.pack("Q", num)
###             f.write(binData)


def readDoubles(fileName, n):
    doubles = []
    with open(fileName, "rb") as f:
        for _ in range(n):
            x, = struct.unpack('d', f.read(8))
            doubles.append(x)
    return doubles


def writeDoubles(fileName, doubles):
    with open(fileName, "wb") as f:
        for double in doubles:
            binData = struct.pack("d", double)
            f.write(binData)


def makeConcentratedDoubles(nums, *, percentile):
    assert 0 <= percentile < 1

    numsSorted = sorted(nums)

    # m = len(numsSorted)//2
    m = len(numsSorted) - 1
    m = m * percentile
    m = math.floor(m)
    print("idx is", m)
    assert m+1 < len(numsSorted), "m+1 is not less than len"

    val = numsSorted[m]
    upperLimit = numsSorted[m+1]

    print(f"val = {val}, upperLimit = {upperLimit}")

    newNums = []
    for i in range(len(nums)):
        val = math.nextafter(val, math.inf)
        assert val < upperLimit, "too close"
        newNums.append(val)
    #random.shuffle(newNums)

    nums.extend(newNums)

    return nums


def makeIncreasingDenseDoubles(nums):
    max_ = max(nums)

    val = max_
    for i in range(len(nums)):
        val = math.nextafter(val, math.inf)
        nums.append(val)
    return nums


def makeIncreasingNums(nums, *, step):
    max_ = max(nums)
    newNums = [max_ + i * step for i in range(1, len(nums)+1)]
    assert len(nums) == len(newNums), "length is wrong"
    nums.extend(newNums)
    return nums


def makeDecreasingDenseDoubles(nums):
    min_ = min(nums)
    val = min_
    for i in range(len(nums)):
        val = math.nextafter(val, -math.inf)
        nums.append(val)
    return nums


def makeSortedDoubles(nums):
    nums.sort()
    return nums



DEBUG = True


def main():

    # nums = readDoubles("../resources/longitudes-200M.bin.data", 10000000)
    nums = readDoubles("../resources/longlat-200M.bin.data", 10000000)
    print(nums[:100])
    print(min(nums), max(nums))


if __name__ == "__main__":
    main()