import sys
import sut
import time

sut = sut.sut()

nocover = False
verbose = False
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

if verbose:
    sut.verbose(True)
    
stime = time.time()
for f in files:
    print "RUNNING TEST",f
    t = sut.loadTest(f)
    ok = False
    try:
        ok = sut.replay(t, checkProp=True)
    except Exception as e:
        print "EXCEPTION RAISED:",e
    if not ok:
        print "TEST",f,"FAILED:"
        print sut.failure()
    print time.time()-stime,"ELAPSED"
    if not nocover:
        print "STATEMENTS:",len(sut.allStatements()), "BRANCHES:",len(sut.allBranches())

if not nocover:
    sut.report("coverage.out")

if htmlOut != None:
    sut.htmlReport(htmlOut)
