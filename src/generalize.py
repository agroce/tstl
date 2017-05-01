import sys
import time
import os
import subprocess

# Appending current working directory to sys.path
# So that user can run randomtester from the directory where sut.py is located
current_working_dir = os.getcwd()
sys.path.append(current_working_dir)

import sut as SUT


def sandboxReplay(test):
    global timeout
    if not "--quietSandbox" in sys.argv:
        print "ATTEMPTING SANDBOX REPLAY WITH",len(test),"STEPS"
    tmpName = "tmptest." + str(os.getpid()) + ".test"
    tmptest = open(tmpName,'w')
    for s in test:
        tmptest.write(s[0] + "\n")
    tmptest.close()
    cmd = "tstl_replay " + tmpName
    if "--noCheck" in sys.argv:
        cmd += " --noCheck"
    if timeout != None:
        cmd = "ulimit -t " + timeout + "; " + cmd
    start = time.time()
    subprocess.call([cmd],shell=True)
    if not "--quietSandbox" in sys.argv:    
        print "ELAPSED:",time.time()-start
    for l in open("replay.out"):
        if "TEST REPLAYED SUCCESSFULLY" in l:
            if not "--quietSandbox" in sys.argv:            
                print "TEST SUCCEEDS"
            return False
    if not "--quietSandbox" in sys.argv:        
        print "TEST FAILS"
    print "SANDBOX RUN FAILS: TEST LENGTH NOW",len(test)
    bestreduce = open("lastreduction." + str(os.getpid()) + ".test",'w')
    for l in open("tmptest.txt"):
        bestreduce.write(l)
    bestreduce.close()
    return True

def main():

    global timeout

    if "--help" in sys.argv:
        print "Usage:  tstl_generalize <test file> <output test file> [--noFresh] [--noCheck] [--verbose verbosity] [--sandbox] [--quietSandbox] [--timeout secs]"
        print "Options:"
        print " --noFresh:        perform fresh object generalization"
        print " --noCheck:      do not run property checks"
        print " --verbose:      set verbosity level for reduction/normalization (defaults to silent reduction/normalization)"
        print " --sandbox:      run tests in a subprocess sandbox, for tests that crash Python interpreter;"
        print "                 due to common difficulties, sandbox is by default very verbose!"
        print "                 WARNING: if not needed, sandbox mode is VERY SLOW"
        print " --quietSandbox: run sandbox in a quiet mode"
        print " --timeout:      if tests are run in a sandbox, consider tests running longer than this to have failed"
        sys.exit(0)

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

    freshGen = not "--noFresh" in sys.argv

    timeout = None
    if "--timeout" in sys.argv:
        lastWasTimeout = False
        for l in sys.argv:
            if lastWasTimeout:
                timeout = l
            if l == "--timeout":
                lastWasTimeout = True
    if not "--sandbox" in sys.argv:
        pred = sut.failsCheck
        if "--noCheck" is sys.argv:
            pred = sut.fails
    else:
        pred = sandboxReplay
    t = sut.loadTest(sys.argv[1])
    sut.generalize(t,pred,verbose=vLevel,fresh=freshGen)
    
    
