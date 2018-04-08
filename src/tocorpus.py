from __future__ import print_function

import random
import struct
import time
import sys
import os

# Appending current working directory to sys.path
# So that user can run randomtester from the directory where sut.py is located
current_working_dir = os.getcwd()
sys.path.append(current_working_dir)

import sut as SUT

def main():
    if "--help" in sys.argv:
        print("Usage:  tstl_toaflcorpus <outputdir> <files>")
        sys.exit(0)

    sut = SUT.sut()

    outputDir = sys.argv[1]
    files = sys.argv[2:]

    acts = sut.actions()

    i = 0
    for f in files:
        t = sut.loadTest(f)
        newinput = open(outputDir + "/input" + str(i),'wb')
        for s in t:
            index = 0
            for a in acts:
                if a == s:
                    break
                index += 1
            newinput.write(struct.pack("<H",index))
        newinput.close()
        i += 1


