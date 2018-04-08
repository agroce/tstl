import sys
import afl
import os
import struct

# Appending current working directory to sys.path
# So that user can run randomtester from the directory where sut.py is located
current_working_dir = os.getcwd()
sys.path.append(current_working_dir)

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

    bytesin = sys.stdin.read()

    test = []
    for i in range(0,len(bytesin)/4):
        test.append(struct.unpack(">L",bytesin[i:i+4])[0] % alen)
    
    for s in test:
        p = s
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
