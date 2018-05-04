from __future__ import print_function

import sys
import time
import os
import glob

# Appending current working directory to sys.path
# So that user can run randomtester from the directory where sut.py is located
current_working_dir = os.getcwd()
sys.path.append(current_working_dir)

if "--help" not in sys.argv:
    import sut as SUT


def main():

    if "--help" in sys.argv:
        print("Usage:  tstl_regress <test files> [--noCheck] [--html dir] [--noCover]",
              "[--verbose] [--running] [--afl] [--aflswarm]")
        print("Options:")
        print(" --glob:         <test files> are glob expressions (used when too many files to use shell expansion)")
        print(" --noCheck:      do not run property checks")
        print(" --html:         output an HTML coverage report to the chosen directory")
        print(" --noCover:      do not compute code coverage")
        print(" --verbose:      make actions verbose")
        print(" --running:      give a running report on code coverage")
        print(" --keepGoing:    don't stop on failed test")
        print(" --afl:          tests are in afl format")
        print(" --aflswarm:     tests are in afl swarm format")
        sys.exit(0)

    sut = SUT.sut()

    nocover = False
    verbose = False
    running = False
    keepGoing = False
    afl = False
    aflswarm = False
    ignoreProps = False
    lastWasHtml = False
    files = []
    htmlOut = None
    for f in sys.argv[1:]:
        if lastWasHtml:
            htmlOut = f
            lastWasHtml = False
        elif "--" not in f:
            files.append(f)
        elif f == "--html":
            lastWasHtml = True
        else:
            lastWasHtml = False

    if "--noCover" in sys.argv:
        nocover = True
        try:
            sut.stopCoverage()
        except BaseException:
            pass
    if "--glob" in sys.argv:
        newFiles = []
        for f in files:
            newFiles.extend(glob.glob(f))
        files = newFiles
    if "--verbose" in sys.argv:
        verbose = True
    if "--noCheck" in sys.argv:
        ignoreProps = True
    if "--running" in sys.argv:
        running = True
    if "--keepGoing" in sys.argv:
        keepGoing = True
    if "--afl" in sys.argv:
        afl = True
    if "--aflswarm" in sys.argv:
        aflswarm = True

    if verbose:
        sut.verbose(True)

    failedTests = []
    anyFailed = False

    noNewCover = []
    newCover = []

    totalTests = 0
    invalidTests = []

    stime = time.time()
    for f in files:
        totalTests += 1
        print("RUNNING TEST", f)
        try:
            t = sut.loadTest(f, afl=afl, swarm=aflswarm)
        except KeyError:
            print("INVALID TEST, SKIPPING...")
            invalidTests.append(f)
            continue
        ok = False
        try:
            ok = sut.replay(t, checkProp=(not ignoreProps))
        except Exception as e:
            print("EXCEPTION RAISED:", e)
        if not nocover:
            if (len(sut.newCurrBranches()) == 0) and (
                    len(sut.newCurrStatements()) == 0):
                noNewCover.append(f)
            else:
                newCover.append(f)
        if running:
            if sut.newCurrBranches() != set([]):
                for b in sut.newCurrBranches():
                    print("New branch:", b)
            if sut.newCurrStatements() != set([]):
                for s in sut.newCurrStatements():
                    print("New statement:", s)
        if not ok:
            print("TEST", f, "FAILED:")
            print(sut.failure())
            failedTests.append(f)
            anyFailed = True
            if not keepGoing:
                sys.exit(255)
        print(time.time() - stime, "ELAPSED")
        if not nocover:
            print("STATEMENTS:", len(sut.allStatements()),
                  "BRANCHES:", len(sut.allBranches()))
            if f not in noNewCover:
                print("NEW STATEMENTS:", len(sut.newCurrStatements()),
                      "BRANCHES:", len(sut.newCurrBranches()))
        sys.stdout.flush()

    if not nocover:
        sut.internalReport()
        print(sut.report("coverage.out"), "PERCENT COVERED")

    if htmlOut is not None:
        sut.htmlReport(htmlOut)

    if (not nocover) and (len(noNewCover) > 0):
        for f in noNewCover:
            print("TEST", f, "REDUNDANT WITH RESPECT TO COVERAGE")
        print()
        print(len(newCover), "TESTS NEEDED FOR FULL COVERAGE:",
              ", ".join(newCover))
        print()

    print("EXECUTED", totalTests, "TESTS")

    if len(invalidTests) > 0:
        print(len(invalidTests), "INVALID TESTS:")
        for f in invalidTests:
            print(f, end=' ')
        print()

    if not anyFailed:
        print("ALL TESTS SUCCESSFUL")
    else:
        print(len(failedTests), "FAILED TESTS:")
        for f in failedTests:
            print(f, end=' ')
        print()
