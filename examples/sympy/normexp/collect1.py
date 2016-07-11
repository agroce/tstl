import subprocess
import glob
import os
import sut
import random
import time
import sys

sut = sut.sut()

while True:
    forder = glob.glob("*.full")
    random.shuffle(forder)
    for f in forder:
        if os.path.exists(f.replace("full","normalized")):
            continue
        print "PROCESSING",f
        print "EXECUTING"
        t = sut.loadTest(f)
        assert(sut.failsAny(t))
        tfail = sut.failure()
        print tfail
        sys.stdout.flush()
        with open(f.replace("full","failure"),'w') as fout:
            fout.write(repr(sut.failure()[1]) + "\n")
        sameFail = lambda x: sut.failsAny(x,failure=tfail)
        tstart = time.time()
        r = sut.reduce(t, sameFail, keepLast=False)
        rtime = time.time()-tstart
        sys.stdout.flush()
        with open(f.replace("full","reducetime"),'w') as fout:
            fout.write(str(rtime) + "\n")        
        sut.saveTest(r, f.replace("full","reduced"))
        print "NORMALIZING"
        sut.clearNormalizationCache()
        tstart = time.time()
        n = sut.normalize(r, sameFail, keepLast=False, verbose=True)
        ntime = time.time()-tstart
        sys.stdout.flush()
        with open(f.replace("full","normtime"),'w') as fout:
            fout.write(str(ntime) + "\n")        
        sut.saveTest(n, f.replace("full","normalized"))
        break
    break
    
