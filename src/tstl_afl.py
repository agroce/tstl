from __future__ import print_function

import sys
import afl
import os
import struct
import random

# Appending current working directory to sys.path
# So that user can run randomtester from the directory where sut.py is located
current_working_dir = os.getcwd()
sys.path.append(current_working_dir)

import sut as SUT

def makeInt(s):
    try:
        return int(s)
    except:
        return None

def runTest():
    global swarm, showActions, noCheck, alwaysSave, noSave, sut

    bytesin = os.read(0,1024*1024)  # yes, puts a limit on test length, but not a very important one probably!

    if swarm:
        if len(bytesin) < 4:
            os._exit(0)
        R.seed(struct.unpack("<L",bytesin[0:4])[0])
        sut.standardSwarm(R)
        bytesin = bytesin[4:]

    alen = len(sut.actions())

    test = sut.bytesToTest(bytesin)

    for a in test:
        if a[1]():
            if showActions:
                print (sut.prettyName(a[0]))
            ok = sut.safely(a)
            if (not noSave) and not ok:
                i = 0
                saveFile = "aflfail." + str(os.getpid()) + "." + str(i) + ".test"
                while os.path.exists(saveFile):
                    i += 1
                    saveFile = "aflfail." + str(os.getpid()) + "." + str(i) + ".test"
                sut.saveTest(sut.test(),saveFile)
            assert(ok)
            if not noCheck:
                checkResult = sut.check()
                if (not noSave) and not checkResult:
                    i = 0
                    saveFile = "aflfail." + str(os.getpid()) + "." + str(i) + ".test"
                    while os.path.exists(saveFile):
                        i += 1
                        saveFile = "aflfail." + str(os.getpid()) + "." + str(i) + ".test"
                    sut.saveTest(sut.test(),saveFile)
                assert(checkResult)
    if alwaysSave:
        i = 0
        saveFile = "afltest." + str(os.getpid()) + "." + str(i) + ".test"
        while os.path.exists(saveFile):
            i += 1
            saveFile = "afltest." + str(os.getpid()) + "." + str(i) + ".test"
        sut.saveTest(sut.test(),saveFile)

def main():
    global swarm, showActions, noCheck, alwaysSave, noSave, sut

    if "--help" in sys.argv:
        print("Usage:  tstl_afl [--noCheck] [--swarm] [--verbose] [--showActions] [--noSave] [--alwaysSave]")
        print("Options:")
        print(" --noCheck:      do not run property checks")
        print(" --swarm         use first four bytes to determine a swarm configuration")
        print(" --verbose:      make actions verbose")
        print(" --showActions:  show actions in test")
        print(" --noSave:       don't save failing tests as standard TSTL tests")
        print(" --alwaysSave:   save even non-failing tests")
        sys.exit(0)

    sut = SUT.sut()

    try:
        sut.stopCoverage()
    except:
        pass

    sut.restart()

    if "--swarm" in sys.argv:
        swarm = True
        R = random.Random()
    else:
        swarm = False
    showActions = "--showActions" in sys.argv
    if "--verbose" in sys.argv:
        sut.verbose(True)
    noSave = "--noSave" in sys.argv
    alwaysSave = "--alwaysSave" in sys.argv
    noCheck = "--noCheck" in sys.argv
    persist = "--persist" in sys.argv

    if not persist:
        afl.init()
        runTest()
    else:
        while afl.loop():
            runTest()
            sut.restart()

    os._exit(0)
