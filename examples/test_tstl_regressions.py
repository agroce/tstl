import pytest
import glob
import traceback
import sut as SUT
import sys

def test_tstl_regressions():
    sut = SUT.sut()

    failCount = 0
    passCount = 0
    
    for f in glob.glob("tstl_tests/*.test"):
        print
        print "*"*50
        print
        t = sut.loadTest(f)
        failed = sut.failsCheck(t)
        if failed:
            print "TEST",f,"FAILS:"
            print
            sut.verbose(True)
            sut.replay(t,checkProp=True,catchUncaught=True)
            failure = sut.failure()
            print failure
            traceback.print_tb(failure[2], file=sys.stdout)
            sut.verbose(False)
            failCount += 1
        else:
            print "TEST",f,"PASSES"
            passCount += 1
    print
    print "*" * 50
    print
    print "TSTL REGRESSIONS RESULT:"
    print passCount,"TESTS PASSED,",failCount,"TESTS FAILED"
    assert failCount == 0
        
