import struct
import math


def readSigned8ByteInt(fileName, n):
    signedLL = []
    with open(fileName, "rb") as f:
        for _ in range(n):
            x, = struct.unpack('q', f.read(8))
            signedLL.append(x)
    return signedLL


def writeSigned8ByteInt(fileName, nums):
    with open(fileName, "wb") as f:
        for num in nums:
            binData = struct.pack("q", num)
            f.write(binData)




def readUnsigned8ByteInt(fileName, n):
    unsignedLL = []
    with open(fileName, "rb") as f:
        for _ in range(n):
            x, = struct.unpack('Q', f.read(8))
            unsignedLL.append(x)
    return unsignedLL


def writeUnsigned8ByteInt(fileName, nums):
    with open(fileName, "wb") as f:
        for num in nums:
            binData = struct.pack("Q", num)
            f.write(binData)




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


def makeConcentratedDoubles(nums, percentile = 0.5):
    assert 0 <= percentile < 1

    numsSorted = sorted(nums)

    # m = len(numsSorted)//2
    m = math.floor((len(numsSorted)-1) * percentile)
    assert m+1 < len(numsSorted), "m+1 is not less than len"

    val = numsSorted[m]
    upperLimit = numsSorted[m+1]

    print(f"val = {val}, upperLimit = {upperLimit}")

    for i in range(len(nums)):
        val = math.nextafter(val, 1)
        assert val < upperLimit, "too close"
        nums.append(val)

    return nums




DEBUG = True


def main():
    doubles = readDoubles("../resources/longlat-200M.bin.data", 10000000)
    #print(doubles)
    doubles = makeConcentratedDoubles(doubles)
    writeDoubles("concentratedDoubles.bin", doubles)

    if DEBUG:
        print("Debugging...")
        doubles2 = readDoubles("concentratedDoubles.bin", 20000000)
        assert doubles == doubles2, "two doubles different"

    print("Data created!")


def test():
    print("Testing...")
    doubles = readDoubles("./concentratedDoubles.bin", 20000000)
    for i in (doubles[19999990:]):
        print("{:.15f}".format(i))



if __name__ == "__main__":
    main()
    # test()