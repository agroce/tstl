import sys
import time
import os

# Appending current working directory to sys.path
# So that user can run randomtester from the directory where sut.py is located
current_working_dir = os.getcwd()
sys.path.append(current_working_dir)

import sut

sut = sut.sut()

nocover = False
verbose = False
running = False
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

if "--nocover" in sys.argv:
    nocover = True
if "--verbose" in sys.argv:
    verbose = True
if "--ignoreProps" in sys.argv:
    ignoreProps = True
if "--running" in sys.argv:
    running = True

if verbose:
    sut.verbose(True)
    
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
    print time.time()-stime,"ELAPSED"
    if not nocover:
        print "STATEMENTS:",len(sut.allStatements()), "BRANCHES:",len(sut.allBranches())

if not nocover:
    sut.internalReport()
    print sut.report("coverage.out"),"PERCENT COVERED"    

if htmlOut != None:
    sut.htmlReport(htmlOut)
