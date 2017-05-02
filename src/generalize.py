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
        print "Usage:  tstl_generalize <test file> <output test file> [--noCheck] [--matchException] [--coverage] [--uncaught] [--keepLast] [--noFresh] [--verbose verbosity] [--sandbox] [--quietSandbox] [--timeout secs]"
        print "Options:"
        print " --noCheck:         do not run property checks"
        print " --matchException   force test to fail with same exception as original test (does not work for sandbox reduction"
        print " --coverage         reduce with respect to maintaining coverage, rather than failure"
        print " --uncaught         allow uncaught exceptions (only applies to coverage-based generalization)"               
        print " --keepLast         force test to keep same last action"        
        print " --noFresh:         perform fresh object generalization"
        print " --verbose:         set verbosity level for reduction/normalization (defaults to silent reduction/normalization)"
        print " --sandbox:         run tests in a subprocess sandbox, for tests that crash Python interpreter;"
        print "                    due to common difficulties, sandbox is by default very verbose!"
        print "                    WARNING: if not needed, sandbox mode is VERY SLOW"
        print " --quietSandbox:    run sandbox in a quiet mode"
        print " --timeout:         if tests are run in a sandbox, consider tests running longer than this to have failed"
        sys.exit(0)

    sut = SUT.sut()

    if not ("--coverage" in sys.argv):
        try:
            sut.stopCoverage()
        except:
            pass
    
    keepLast = "--keepLast" in sys.argv
    
    vLevel = False      
    if "--verbose" in sys.argv:
        lastWasVerbose = False
        for l in sys.argv:
            if lastWasVerbose:
                vLevel = l
            if l == "--verbose":
                lastWasVerbose = True
            else:
                lastWasVerbose = False
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
            else:
                lastWasTimeout = False

    exceptionMatch = "--matchException" in sys.argv
    coverage = "--coverage" in sys.argv
    
    t = sut.loadTest(sys.argv[1])

    f = None
    
    if exceptionMatch:
        print "RUNNING TO OBTAIN FAILURE FOR EXCEPTION MATCHING..."
        assert (sut.fails(t))
        f = sut.failure()
        print "ERROR:",f
        print "TRACEBACK:"
        traceback.print_tb(f[2],file=sys.stdout)
    
    if not "--sandbox" in sys.argv:
        pred = (lambda x: sut.failsCheck(x,failure=f))
        if "--noCheck" is sys.argv:
            pred = (lambda x: sut.fails(x,failure=f))
    else:
        pred = sandboxReplay

    if coverage:
        print "EXECUTING TEST TO OBTAIN COVERAGE..."
        sut.replay(t,checkProp = not ("--noCheck" in sys.argv),catchUncaught=("--uncaught" in sys.argv))
        b = set(sut.currBranches())
        s = set(sut.currStatements())
        print "PRESERVING",len(b),"BRANCHES AND",len(s),"STATEMENTS"
        pred = sut.coversAll(s,b,checkProp = not ("--noCheck" in sys.argv),catchUncaught=("--uncaught" in sys.argv))

    print "GENERALIZING..."
    start = time.time()
    sut.generalize(t,pred,verbose=vLevel,fresh=freshGen,keepLast=keepLast)
    print "GENERALIZED IN",time.time()-start,"SECONDS"
    
