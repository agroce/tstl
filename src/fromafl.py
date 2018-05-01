from __future__ import print_function

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
        print("Usage:  tstl_fromafl <outputdir> <files> [--aflswarm]")
        sys.exit(0)

    sut = SUT.sut()

    aflswarm = "--aflswarm" in sys.argv
    if aflswarm:
        sys.argv.remove("--aflswarm")

    outputDir = sys.argv[1]
    files = sys.argv[2:]

    i = 0
    for f in files:
        t = sut.loadTest(f, afl=True, swarm=aflswarm)
        sut.saveTest(t, outputDir + "/" + os.path.basename(f) + ".test")
        i += 1
