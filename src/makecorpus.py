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

if "--help" not in sys.argv:
    import sut as SUT


def main():
    if "--help" in sys.argv:
        print("Usage:  tstl_aflcorpus <outputdir> <length> <time> [--noCheck]",
              "[--noReduce] [--noCover] [--swarm] [--skipFails]")
        print("Options:")
        print(" --noCheck:       do not check properties")
        print(" --noReduce:      do not reduce inputs by coverage")
        print(" --noCover:       do not check for new coverage")
        print(" --swarm:         use swarm format, generate tests using swarm")
        print(" --skipFails:     just pass over failures, don't try to fix")
        print(" --burst:         high speed, dumb version (let AFL sort 'em out)")
        print(" --loudSUT:       show output from the SUT")
        sys.exit(0)

    sut = SUT.sut()

    pid = str(os.getpid())

    dnull = open(os.devnull, 'w')
    oldStdout = sys.stdout
    oldStderr = sys.stderr

    print("GENERATING INITIAL AFL INPUTS...")

    outputDir = sys.argv[1]
    length = int(sys.argv[2])
    timeout = int(sys.argv[3])

    burst = "--burst" in sys.argv
    checkProp = "--noCheck" not in sys.argv
    noReduce = "--noReduce" in sys.argv
    noCover = "--noCover" in sys.argv
    swarm = "--swarm" in sys.argv
    skipFails = "--skipFails" in sys.argv
    loudSUT = "--loudSUT" in sys.argv

    if burst:
        timeout = 60

    if noCover or burst:
        sut.stopCoverage()

    R = random.Random()
    Rswarm = random.Random()

    i = 0
    stime = time.time()
    while (time.time() - stime) < timeout:
        i += 1
        if swarm:
            seed = R.randint(0, 2**32)
            Rswarm.seed(seed)
            sut.standardSwarm(Rswarm)
        if not loudSUT:
            sys.stdout = dnull
            sys.stderr = dnull
        (t, ok) = sut.makeTest(length, R, stopFail=True, checkProp=checkProp)
        if not loudSUT:
            sys.stdout = oldStdout
            sys.stderr = oldStderr
        if ((not noCover) and (not burst) and (len(sut.newCurrBranches())
                                               == 0) and len(sut.newCurrStatements()) == 0):
            continue
        else:
            print("INPUT", i, "GENERATED", end=" ")
            if (not noCover) and (not burst):
                print("NEW BRANCHES:", len(sut.newCurrBranches()), end=" ")
            type = "branch" + str(len(sut.newCurrBranches()))
        if ok:  # failing tests won't work with afl
            if (not burst) and (not noCover) and (not noReduce):
                b = set(sut.currBranches())
                s = set(sut.currStatements())
                if not loudSUT:
                    sys.stdout = dnull
                    sys.stderr = dnull
                pred = sut.coversAll(s, b, checkProp=True, catchUncaught=False)
                r = sut.reduce(t, pred, verbose=False)
                if not loudSUT:
                    sys.stdout = oldStdout
                    sys.stderr = oldStderr
            else:
                r = t
        elif skipFails:
            print("SKIPPING FAILED TEST...")
            continue
        else:
            type = "nearfail"
            print("SAVING ALL BUT LAST STEP OF FAILED TEST")
            r = t[:-1]

        # always alpha convert to make actions clearer to afl, easier to splice
        r = sut.alphaConvert(r)
        if ok and (not burst) and (not noCover) and (not noReduce):
            print("REDUCED LENGTH:", len(r))
        if not burst:
            sut.prettyPrintTest(r)
        print("=" * 80)
        if not swarm:
            sut.saveTest(r, outputDir + "/tstl." + type + "." +
                         pid + "." + str(i) + ".afl", afl=True)
        else:
            bytes = sut.testToBytes(r)
            with open(outputDir + "/tstl." + type + "." + pid + "." + str(i) + ".afl", 'wb') as f:
                f.write(struct.pack("<L", seed))
                f.write(bytes)
