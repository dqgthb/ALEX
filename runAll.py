#!/usr/bin/env python
import os
import sys
import subprocess

maxStr = [str(i) for i in range(65, 85, 5)]
minStr = [str(i) for  i in range(60, 80, 5)]

def oldMain():
    for i in range(40, 62, 2):
        # os.system("./run.ps1 50")
        # p = subprocess.Popen([".\run.ps1", "50"])
        p = subprocess.Popen(["powershell.exe", "./run.ps1 "+str(i)])
        p.communicate()


def main():
    for i in range(len(minStr)):
        for j in range(i, len(maxStr)):
            p = subprocess.Popen(["powershell.exe", "./runMinMax.ps1", minStr[i], maxStr[j]])
            p.communicate()

if __name__ == "__main__":
    main()