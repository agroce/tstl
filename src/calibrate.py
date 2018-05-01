from __future__ import print_function

import sys
import time
import argparse
import os
import subprocess
import random
from collections import namedtuple

# Appending current working directory to sys.path
# So that user can run randomtester from the directory where sut.py is located
current_working_dir = os.getcwd()
sys.path.append(current_working_dir)

if "--help" not in sys.argv:
    import sut as SUT


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--seed', type=int, default=None,
                        help='Random seed (default = None).')

    parsed_args = parser.parse_args(sys.argv[1:])
    return (parsed_args, parser)


def make_config(pargs, parser):
    """
    Process the raw arguments, returning a namedtuple object holding the
    entire configuration, if everything parses correctly.
    """
    pdict = pargs.__dict__
    # create a namedtuple object for fast attribute lookup
    key_list = list(pdict.keys())
    arg_list = [pdict[k] for k in key_list]
    Config = namedtuple('Config', key_list)
    nt_config = Config(*arg_list)
    return nt_config


def main():

    parsed_args, parser = parse_args()
    config = make_config(parsed_args, parser)
    print(('Calibrating using config={}'.format(config)))

    calibFile = open(".tstl_calibration", 'w')

    sut = SUT.sut()

    R = random.Random()
    if config.seed:
        R.seed(config.seed)

    print("=" * 80)
    print("CALIBRATING COST OF COVERAGE...\n")

    oldOut = sys.stdout
    fnull = open(os.devnull, 'w')
    sys.stdout = fnull

    sut.stopCoverage()

    oldOut.write(
        "GENERATING 30 TESTS (OR 30+s of TESTS) WITHOUT COVERAGE...\n")
    oldOut.flush()
    start = time.time()
    noCovCount = 0
    for i in range(0, 30):
        oldOut.write(str(i) + "...")
        oldOut.flush()
        (t, ok) = sut.makeTest(100, R, stopFail=False)
        noCovCount += 1
        if (time.time() - start) > 30:
            oldOut.write("TIMEOUT AT " + str(time.time() - start))
            break
    noCovTime = time.time() - start

    sut.startCoverage()

    oldOut.write(
        "\n\nGENERATING 30 TESTS (OR 30+s of TESTS) WITH COVERAGE...\n")

    start = time.time()
    covCount = 0
    for i in range(0, 30):
        oldOut.write(str(i) + "...")
        oldOut.flush()
        (t, ok) = sut.makeTest(100, R, stopFail=False)
        covCount += 1
        if (time.time() - start) > 30:
            oldOut.write("TIMEOUT AT " + str(time.time() - start))
            break
    covTime = time.time() - start

    sys.stdout = oldOut

    print()
    print()
    sys.stdout.flush()

    covR = (covCount * 100) / covTime
    noCovR = (noCovCount * 100) / noCovTime
    if covR < noCovR:
        print("WITH COVERAGE:", covR, "ACTIONS/s")
        print("WITHOUT COVERAGE:", noCovR, "ACTIONS/s")
        overhead = (noCovR - covR) / noCovR
        print("COVERAGE OVERHEAD:", str(round(overhead * 100, 2)) + "%")
    else:
        print("NO DETECTABLE COVERAGE OVERHEAD")
    calibFile.write("COVERAGE OVERHEAD: " + str(overhead))

    print("=" * 80)
    print("ESTIMATING LINES OF CODE IN ACTIONS...\n")
    subprocess.call(
        ["tstl_rt --timeout 180 --generateLOC .tstl_calibration_loc --noCover"],
        shell=True,
        stdout=fnull,
        stderr=fnull)
    classLOCVals = {}
    for c in sut.actionClasses():
        classLOCVals[c] = 0.0
    totalLOCs = 0.0
    num0 = 0.0
    with open(".tstl_calibration_loc", 'r') as cf:
        for l in cf:
            ls = l.split(" %%%% ")
            c = ls[0]
            loc = float(ls[1])
            totalLOCs += loc
            classLOCVals[c] = loc
        classP = {}
        for c in sut.actionClasses():
            if classLOCVals[c] == 0.0:
                num0 += 1
        for c in sut.actionClasses():
            if classLOCVals[c] == 0.0:
                classP[c] = (0.20 / num0)
            else:
                classP[c] = (classLOCVals[c] / totalLOCs)
    sortLOC = sorted(classLOCVals.keys(),
                     key=lambda x: classP[x], reverse=True)
    print("HIGHEST LOC-BASED PROBABILITY ACTIONS:")
    for c in sortLOC[:3]:
        print("  ", c, round(classP[c], 5))
    print("\nLOWEST LOC-BASED PROBABILITY ACTIONS:")
    for c in sortLOC[-3:]:
        print("  ", c, round(classP[c], 5))

    calibFile.close()
