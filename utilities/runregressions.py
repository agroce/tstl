import sys
import sut
import time

sut = sut.sut()

stime = time.time()
for f in sys.argv[1:]:
    print "RUNNING TEST",f
    t = sut.loadTest(f)
    ok = sut.replay(t, checkProp=True)
    if not ok:
        print "TEST",f,"FAILED:"
        print sut.error()
    print time.time()-stime,"ELAPSED"
    print "STATEMENTS:",len(sut.allStatements()), "BRANCHES:",len(sut.allBranches())


