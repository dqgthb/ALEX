#!/usr/bin/env python
import os
import sys
import subprocess

def main():
    for i in range(40, 62, 2):
        # os.system("./run.ps1 50")
        # p = subprocess.Popen([".\run.ps1", "50"])
        p = subprocess.Popen(["powershell.exe", "./run.ps1 "+str(i)])
        p.communicate()

if __name__ == "__main__":
    main()