import sys
import afl
import os
import sut as SUT

def makeInt(s):
    try:
        return int(s)
    except:
        return None


def main():

    sut = SUT.sut()
    saveFile = str(os.getpid()) + ".failure.test"
    
    try:
        sut.stopCoverage()
    except:
        pass

    sut.restart()

    if "--verbose" in sys.argv:
        sut.verbose(True)
    noSave = "--noSave" in sys.argv
    noCheck = "--noCheck" in sys.argv


    alen = len(sut.actions())

    afl.init()

    test = list(filter(lambda x:x != None,map(makeInt,sys.stdin.read().split(","))))

    for s in test:
        p = s
        if p < 0:
            p = -p
        if p >= alen:
            p = (p % alen)
        while not sut.actions()[p][1]():
            p = (p + 1) % alen

        a = sut.actions()[p]
        if a[1]():
            ok = sut.safely(a)
            if (not noSave) and not ok:
                sut.saveTest(saveFile,sut.test())
            assert(ok)
        if not noCheck:
            checkResult = sut.check()
            if (not noSave) and not checkResult:
                sut.saveTest(saveFile,sut.test())            
            assert(checkResult)
            
    os._exit(0)
