import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import dataIO


def makeAllGraphs():
    #sns.set_theme()
    sns.set_theme(style="whitegrid", palette="deep")

    resourceDir = "../resources/"
    dataNames = ["longitudes", "longlat"]
    for dataName in dataNames:
        print("for " + dataName)

        print("creating ordinary")
        nums = dataIO.readDoubles(resourceDir + dataName + "-200M.bin.data", 20000000)
        sns.displot(nums, kind="ecdf")
        plt.savefig(dataName + "-ordinary.png")

        print("creating 25")
        nums = dataIO.readDoubles(resourceDir + dataName + "/" + dataName + "25%.bin", 20000000)
        sns.displot(nums, kind="ecdf")
        plt.savefig(dataName + "25%.png")

        print("creating 50")
        nums = dataIO.readDoubles(resourceDir + dataName + "/" + dataName + "50%.bin", 20000000)
        sns.displot(nums, kind="ecdf")
        plt.savefig(dataName + "50%.png")

        print("creating 75")
        nums = dataIO.readDoubles(resourceDir + dataName + "/" + dataName + "75%.bin", 20000000)
        sns.displot(nums, kind="ecdf")
        plt.savefig(dataName + "75%.png")

        print("creating increasing")
        nums = dataIO.readDoubles(resourceDir + dataName + "/" + dataName + "Increasing.bin", 20000000)
        sns.displot(nums, kind="ecdf")
        plt.savefig(dataName + "Increasing.png")

        print("creating increasingBy1")
        nums = dataIO.readDoubles(resourceDir + dataName + "/increaseBy1.bin", 20000000)
        sns.displot(nums, kind="ecdf")
        plt.savefig(dataName + "IncreaseBy1.png")


def makeUniformVsConcentratedComparison(dataName):

    df =pd.read_csv(dataName + ".csv")
    print(df)

    sns.barplot(
        data=df,
        x="Insert Distribution",
        y="Inserts Per Second",
    )
    plt.title(dataName)
    plt.savefig(dataName + "Comparison.png")


def makeCDF(dataName):

    print("creating ordinary")
    nums = dataIO.readDoubles(resourceDir + dataName + "-200M.bin.data", 20000000)
    sns.displot(nums, kind="ecdf")
    plt.title(dataName)
    plt.savefig(dataName + "-ordinary.png")



def main():
    global resourceDir
    resourceDir = "../resources/"
    makeUniformVsConcentratedComparison("longitudes")
    makeUniformVsConcentratedComparison("longlat")
    makeCDF("longitudes")
    makeCDF("longlat")



if __name__ == "__main__":
    main()