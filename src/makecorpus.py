from __future__ import print_function

import random
import struct
import time
import sys
import os

# Appending current working directory to sys.path
# So that user can run randomtester from the directory where sut.py is located
current_working_dir = os.getcwd()
sys.path.append(current_working_dir)

import sut as SUT

def main():
    if "--help" in sys.argv:
        print("Usage:  tstl_aflcorpus <outputdir> <length> <time> [--noReduce] [--noCover] [--afl] [--aflswarm]")
        print("Options:")
        print(" --noReduce:      do not reduce inputs by coverage")
        print(" --noCover:       do not check for new coverage")
        print(" --swarm:         use swarm format")                        
        sys.exit(0)

    sut = SUT.sut()

    pid = str(os.getpid())

    outputDir = sys.argv[1]
    length = int(sys.argv[2])
    timeout = int(sys.argv[3])

    noReduce = "--noReduce" in sys.argv
    noCover = "--noCover" in sys.argv
    swarm = "--swarm" in sys.argv
    
    R = random.Random()
    Rswarm = random.Random()

    acts = sut.actions()
    i = 0
    stime = time.time()
    while (time.time()-stime) < timeout:
        i += 1
        if swarm:
            seed = R.randint(0,2**32)
            Rswarm.seed(seed)
            sut.standardSwarm(Rswarm)
        (t,ok) = sut.makeTest(length,R)
        if (not noCover) and (len(sut.newCurrBranches()) == 0):
            continue
        else:
            print ("INPUT",i,"GENERATED",end=" ")
            if not noCover:
                print ("NEW BRANCHES:",len(sut.newCurrBranches()),end=" ")
        if ok: # failing tests won't work with afl
            if not noReduce:
                b = set(sut.currBranches())
                s = set(sut.currStatements())
                pred = sut.coversAll(s,b,checkProp=True,catchUncaught=False)
                r = sut.reduce(t,pred,verbose=False)
            else:
                r = t
                
            # always alpha convert to make actions clearer to afl, easier to splice
            r = sut.alphaConvert(r) 
            if not noReduce:
                print ("REDUCED LENGTH:",len(r))
            sut.prettyPrintTest(r)
            print ("="*80)
            if not swarm:
                sut.saveTest(r,outputDir + "/input" +"." + pid + "." + str(i) + ".afl",afl=True)
            else:
                bytes = sut.testToBytes(r)
                with open(outputDir + "/input" +"." + pid + "." + str(i) + ".afl",'wb') as f:
                    f.write(struct.pack("<L",seed))
                    f.write(bytes)
        else:
            print ("TEST FAILS!")


