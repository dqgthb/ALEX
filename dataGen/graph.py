import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import dataIO

def main():
    #sns.set_theme()
    sns.set_theme(style="whitegrid", palette="deep")

    resourceDir = "../resources/"
    nums = dataIO.readDoubles(resourceDir + "longitudes-200M.bin.data", 20000000)
    sns.displot(nums, kind="ecdf")
    plt.savefig("longitudes-ordinary.png")

    nums = dataIO.readDoubles(resourceDir + "longitudes/longitudes25%.bin", 20000000)
    sns.displot(nums, kind="ecdf")
    plt.savefig("longitudes25%.png")

    nums = dataIO.readDoubles(resourceDir + "longitudes/longitudes50%.bin", 20000000)
    sns.displot(nums, kind="ecdf")
    plt.savefig("longitudes50%.png")

    nums = dataIO.readDoubles(resourceDir + "longitudes/longitudes75%.bin", 20000000)
    sns.displot(nums, kind="ecdf")
    plt.savefig("longitudes75%.png")

    nums = dataIO.readDoubles(resourceDir + "longitudes/longitudesIncreasing.bin", 20000000)
    sns.displot(nums, kind="ecdf")
    plt.savefig("longitudesIncreasing.png")


if __name__ == "__main__":
    main()


if __name__ == "__main__":
    main()