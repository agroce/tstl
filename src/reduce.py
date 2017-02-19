import sys
import traceback
import os
import time

# Appending current working directory to sys.path
# So that user can run randomtester from the directory where sut.py is located
current_working_dir = os.getcwd()
sys.path.append(current_working_dir)

import sut as SUT

def main():


    if "--help" in sys.argv:
        print "Usage:  tstl_reduce <test file> <output test file> [--noNormalize] [--noCheck] [--verbose verbosity]"
        print "Options:"
        print " --noCheck:      do not run property checks"
        print " --noNormalize   after reducing, do not also normalize"
        print " --verbose:      set verbosity level for reduction/normalization (defaults to silent reduction/normalization)"
        sys.exit(0)

    import sut as SUT
    sut = SUT.sut()
        
    vLevel = False
        
    if "--verbose" in sys.argv:
        lastWasVerbose = False
        for l in sys.argv:
            if lastWasVerbose:
                vLevel = l
            if l == "--verbose":
                lastWasVerbose = True
    if vLevel == "True":
        vLevel = True
    if vLevel == "False":
        vLevel = False       
        
    t = sut.loadTest(sys.argv[1])
    start = time.time()
    print "REDUCING..."
    pred = sut.failsCheck
    if "--noCheck" is sys.argv:
        pred = sut.fails
    r = sut.reduce(t,pred,verbose=vLevel)
    print "REDUCED IN",time.time()-start,"SECONDS"
    if not ("--noNormalize" in sys.argv):
        start = time.time()
        print "NORMALIZING..."
        r = sut.normalize(r,pred,verbose=vLevel)
        print "NORMALIZED IN",time.time()-start,"SECONDS"
    sut.saveTest(r,sys.argv[2])        
    print "Reduced",
    if not ("--noNormalize" in sys.argv):
        print "and normalized",
    print "test written to",sys.argv[2]
    
    
