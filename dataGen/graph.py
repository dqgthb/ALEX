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
        plt.clf()


def makeUniformVsConcentratedComparison(dataName):

    df =pd.read_csv(dataName + ".csv")

    sns.barplot(
        data=df,
        x="Insert Distribution",
        y="Inserts Per Second",
    )
    plt.title(dataName.capitalize())
    plt.savefig(dataName + "Comparison.png")
    plt.clf()


def makeCDF(dataName):

    print("creating ordinary")
    nums = dataIO.readDoubles(resourceDir + dataName + "-200M.bin.data", 20000000)
    sns.displot(nums, kind="ecdf")
    plt.title(dataName.capitalize())
    plt.savefig(dataName + "-ordinary.png")



def main():
    global resourceDir

    sns.set_theme(style="whitegrid", palette="deep", font_scale=1.2)

    resourceDir = "../resources/"
    makeUniformVsConcentratedComparison("longitudes")
    makeUniformVsConcentratedComparison("longlat")
    #makeCDF("longitudes")
    #makeCDF("longlat")


    x = ["Uniform\n(80,60)"] + ["Skewed\n"+i for i in ["(80,60)", "(80,65)", "(80,70)", "(80,75)", "(75,65)", "(75,70)"]]
    #ax.get_figure().savefig("longitudesNumsInserts.png")

    dfs = {}
    y =  [1810000, 573200, 840967, 1413333, 1260333, 1066000, 1260333]
    clrs = ['blue', 'grey'] + ['brown' if (i < max(y[2:])) else 'red' for i in y[2:]]
    dfs["Longitudes"] = pd.DataFrame({'max, min':x, 'Number of Inserts per Seconds': y})

    y = [1383000, 1048067, 1024933, 1271667, 1251000, 1098400, 1102633]
    clrs = ['blue', 'grey'] + ['brown' if (i < max(y[2:])) else 'red' for i in y[2:]]
    dfs["Longlat"] = pd.DataFrame({'max, min':x, 'Number of Inserts per Seconds': y})

    for dataName in ["Longitudes", "Longlat"]:
        barPlt = sns.barplot(data = dfs[dataName], x = 'max, min', y='Number of Inserts per Seconds', palette=clrs)
        barPlt.set(title=dataName)
        barPlt.set_xlabel("")
        barPlt.get_figure().savefig(dataName + "NumOfInserts.png")
        plt.clf()










if __name__ == "__main__":
    main()