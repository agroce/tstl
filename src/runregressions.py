import sys
import time
import os

# Appending current working directory to sys.path
# So that user can run randomtester from the directory where sut.py is located
current_working_dir = os.getcwd()
sys.path.append(current_working_dir)

import sut as SUT

def main():
    
    if "--help" in sys.argv:
        print "Usage:  tstl_regress <test files> [--noCheck] [--html dir] [--noCover] [--verbose] [--running]"
        print "Options:"
        print " --noCheck:      do not run property checks"
        print " --html:         output an HTML coverage report to the chosen directory"
        print " --noCover:      do not compute code coverage"
        print " --verbose:      make actions verbose"
        print " --running:      give a running report on code coverage"
        print " --keepGoing:    don't stop on failed test"
        sys.exit(0)
    
    sut = SUT.sut()

    nocover = False
    verbose = False
    running = False
    keepGoing = False
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
        except:
            pass
    if "--verbose" in sys.argv:
        verbose = True
    if "--noCheck" in sys.argv:
        ignoreProps = True
    if "--running" in sys.argv:
        running = True
    if "--keepGoing" in sys.argv:
        keepGoing = True

    if verbose:
        sut.verbose(True)

    anyFailed = False
        
    stime = time.time()
    for f in files:
        print "RUNNING TEST",f
        t = sut.loadTest(f)
        ok = False
        try:
            ok = sut.replay(t, checkProp=(not ignoreProps))
        except Exception as e:
            print "EXCEPTION RAISED:",e
        if running:
            if sut.newBranches() != set([]):
                for b in sut.newBranches():
                    print "New branch:",b
            if sut.newStatements() != set([]):
                for s in sut.newStatements():
                    print "New statement:",s
        if not ok:
            print "TEST",f,"FAILED:"
            print sut.failure()
            anyFailed = True
            if not keepGoing:
                sys.exit(255)
        print time.time()-stime,"ELAPSED"
        if not nocover:
            print "STATEMENTS:",len(sut.allStatements()), "BRANCHES:",len(sut.allBranches())

    if not nocover:
        sut.internalReport()
        print sut.report("coverage.out"),"PERCENT COVERED"    

    if htmlOut != None:
        sut.htmlReport(htmlOut)

    if not anyFailed:
        print "ALL TESTS SUCCESSFUL"
