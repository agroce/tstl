import sys
import time
import traceback
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
        print "Usage:  tstl_reduce <test file> <output test file> [--noCheck] [--matchException] [--keepLast] [--noReduce] [--fast] [--multiple] [--recursion N] [--limit K] [--noAlpha] [--noNormalized] [--verbose verbosity] [--sandbox] [--quietSandbox] [--timeout secs]"
        print "Options:"
        print " --noCheck:         do not run property checks"
        print " --matchException   force test to fail with same exception as original test (does not work for sandbox reduction"
        print " --coverage         reduce with respect to maintaining coverage, rather than failure"
        print " --coverMore        force test to GAIN coverage over baseline, if possible"
        print " --uncaught         allow uncaught exceptions (only applies to coverage-based reduction)"                
        print " --keepLast         force test to keep same last action"
        print " --noReduce         do not reduce test (useful for normalizing an already reduced test)"
        print " --fast             if test is near 1-minimal, this may improve delta-debugging speed"
        print " --multiple         produce multiple reductions, to avoid (or induce) slippage"
        print " --recursive        recursive depth for multiple reductions (default 1)"
        print " --limit            depth limit for multiple reductions"
        print " --noAlpha          do not alpha convert test"
        print " --noNormalize      after reducing, do not also normalize"
        print " --verbose:         set verbosity level for reduction/normalization (defaults to silent reduction/normalization)"
        print " --sandbox:         run tests in a subprocess sandbox, for tests that crash Python interpreter;"
        print "                    due to common difficulties, sandbox is by default very verbose!"
        print "                    WARNING: if not needed, sandbox mode is VERY SLOW"
        print " --quietSandbox:    run sandbox in a quiet mode"
        print " --timeout:         if tests are run in a sandbox, consider tests running longer than this to have failed"
        sys.exit(0)

    sut = SUT.sut()

    if not (("--coverage" in sys.argv) or ("--coverMore" in sys.argv)):
        try:
            sut.stopCoverage()
        except:
            pass
    
    fastReduce = "--fast" in sys.argv
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

    timeout = None
    if "--timeout" in sys.argv:
        lastWasTimeout = False
        for l in sys.argv:
            if lastWasTimeout:
                timeout = l
            if l == "--timeout":
                lastWasTimeout = True
                
    recursive = 1
    if "--recursive" in sys.argv:
        lastWasRecur = False
        for l in sys.argv:
            if lastWasRecur:
                recursive = int(l)
            if l == "--recursive":
                lastWasRecur = True
            else:
                lastWasRecur = False
    limit = 1
    if "--limit" in sys.argv:
        lastWasLimit = False
        for l in sys.argv:
            if lastWasLimit:
                limit = int(l)
            if l == "--limit":
                lastWasLimit = True
            else:
                lastWasLimit = False

    multiple = "--multiple" in sys.argv
    exceptionMatch = "--matchException" in sys.argv
    coverage = "--coverage" in sys.argv
    coverMore = "--coverMore" in sys.argv
    
    r = sut.loadTest(sys.argv[1])

    f = None
    
    if exceptionMatch:
        print "EXECUTING TEST TO OBTAIN FAILURE FOR EXCEPTION MATCHING..."
        assert (sut.fails(r))
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

    if coverage or coverMore:
        print "EXECUTING TEST TO OBTAIN COVERAGE FOR CAUSE REDUCTION..."
        sut.replay(r,checkProp = not ("--noCheck" in sys.argv),catchUncaught=("--uncaught" in sys.argv))
        b = set(sut.currBranches())
        s = set(sut.currStatements())
        print "PRESERVING",len(b),"BRANCHES AND",len(s),"STATEMENTS"
        if coverMore:
            pred = sut.coversMore(s,b,checkProp = not ("--noCheck" in sys.argv),catchUncaught=("--uncaught" in sys.argv))
        else:
            pred = sut.coversAll(s,b,checkProp = not ("--noCheck" in sys.argv),catchUncaught=("--uncaught" in sys.argv))
        
    print "STARTING WITH TEST OF LENGTH",len(r)
    if not ("--noReduce" in sys.argv):
        start = time.time()
        print "REDUCING..."
        if not multiple:
            r = sut.reduce(r,pred,verbose=vLevel,tryFast=fastReduce,keepLast=keepLast)
        else:
            rs = sut.reductions(r,pred,verbose=vLevel,recursive=recursive,limit=limit,keepLast=keepLast)
        print "REDUCED IN",time.time()-start,"SECONDS"
        if not multiple:
            print "NEW LENGTH",len(r)
        else:
            print "NEW LENGTHS",map(len,rs)
    if not ("--noAlpha" in sys.argv):
        print "ALPHA CONVERTING..."
        if not multiple:
            r = sut.alphaConvert(r)
        else:
            rs = map(sut.alphaConvert, rs)
    if not ("--noNormalize" in sys.argv):
        start = time.time()
        print "NORMALIZING..."
        if not multiple:
            r = sut.normalize(r,pred,verbose=vLevel,keepLast=keepLast)
        else:
            newrs = []
            for r in rs:
                newrs.append(sut.normalize(r,pred,verbose=vLevel,keepLast=keepLast))
            rs = newrs
        print "NORMALIZED IN",time.time()-start,"SECONDS"
        if not multiple:
            print "NEW LENGTH",len(r)
        else:
            print "NEW LENGTHS",map(len,news)
    if not multiple:
        sut.saveTest(r,sys.argv[2])
        sut.prettyPrintTest(r)
    else:
        i = 0
        for r in rs:
            print "TEST #"+str(i)+":"
            sut.saveTest(r,sys.argv[2]+"."+str(i))
            sut.prettyPrintTest(r)
            print
            print "TEST WRITTEN TO",sys.argv[2]+"."+str(i)
            i += 1
            
    
    
