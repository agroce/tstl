import os
import sys

# Appending current working directory to sys.path
# So that user running randomtester from the directory where sut.py is located
current_working_dir = os.getcwd()
sys.path.append(current_working_dir)

import sut as SUT
import random
import time
import traceback
import argparse
from collections import namedtuple

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--depth', type=int, default=100,
                        help='Maximum search depth (100 default).')
    parser.add_argument('-t', '--timeout', type=int, default=3600,
                        help='Timeout in seconds (3600 default).')
    parser.add_argument('-s', '--seed', type=int, default=None,
                        help='Random seed (default = None).')
    parser.add_argument('-m', '--maxtests', type=int, default=-1,
                        help='Maximum #tests to run (-1 = infinite default).')
    parser.add_argument('-u', '--uncaught', action='store_true',
                        help='Allow uncaught exceptions in actions.')
    parser.add_argument('-i', '--ignoreprops', action='store_true',
                        help='Ignore properties.')
    parser.add_argument('-f', '--full', action='store_true',
                        help="Don't reduce -- report full failing test.")
    parser.add_argument('-N', '--normalize', action='store_true',
                        help="Normalize/simplify after reduction.")
    parser.add_argument('-E', '--essentials', action='store_true',
                        help="Determine essential elements in failing test.")
    parser.add_argument('-G', '--generalize', action='store_true',
                        help="Generalize tests.")
    parser.add_argument('-D', '--gendepth', type=int, default=None,
                        help = "Generalization depth for cloud overlap comparisons (default = None).")
    parser.add_argument('-e', '--speed', type=str, default="FAST",
                        help='Normalization/simplification speed (default = FAST).')    
    parser.add_argument('-k', '--keep', action='store_true',
                        help="Keep last action the same when reducing.")
    parser.add_argument('-o', '--output', type=str, default=None,
                        help="Filename to save failing test(s).")
    parser.add_argument('-R', '--replayable', action='store_true',
                        help="Keep replayable file of current test, in case of crash.")
    parser.add_argument('-T', '--total', action='store_true',
                        help="Keep a file with ALL TESTING ACTIONS in case of crash.")
    parser.add_argument('-M', '--multiple', action='store_true',
                        help="Allow multiple failures.")
    parser.add_argument('-l', '--logging', type=int, default=None,
                        help="Set logging level")
    parser.add_argument('-F', '--failedLogging', type=int, default=None,
                        help="Set failed test case logging level")    
    parser.add_argument('-r', '--running', action='store_true',
                        help="Produce running branch coverage report.")
    parser.add_argument('-C', '--compareFails', action='store_true',
                        help="Compare all failing tests.")
    parser.add_argument('-S', '--stutter', type=float, default=None,
                        help="Repeat last action if still enabled with P = <stutter>.")
    parser.add_argument('-g', '--greedyStutter', action='store_true',
                        help="Repeat last action if it is enabled and improved coverage.")
    parser.add_argument('-n', '--nocover', action='store_true',
                        help="Don't produce a coverage report at the end.")
    parser.add_argument('-I', '--internal', action='store_true',
                        help="Produce internal coverage report at the end, as sanity check on coverage.py results.")    
    parser.add_argument('-c', '--coverfile', type=str, default="coverage.out",
                        help="File to write coverage report to ('coverage.out' default).")
    parser.add_argument('-q', '--quickTests', action='store_true',
                        help="Produce quick tests for coverage.")
    parser.add_argument('-a', '--noreassign', action='store_true',
                        help="Add noReassign rule to normalization steps.")
    parser.add_argument('-v', '--verbose', action='store_true',
                        help="Run in verbose mode.")
    parser.add_argument('-H', '--html', type=str, default=None,
                        help="Write HTML report (directory to write to, None default).")
    parsed_args = parser.parse_args(sys.argv[1:])
    return (parsed_args, parser)

def make_config(pargs, parser):
    """
    Process the raw arguments, returning a namedtuple object holding the
    entire configuration, if everything parses correctly.
    """
    pdict = pargs.__dict__
    # create a namedtuple object for fast attribute lookup
    key_list = pdict.keys()
    arg_list = [pdict[k] for k in key_list]
    Config = namedtuple('Config', key_list)
    nt_config = Config(*arg_list)
    return nt_config   

def handle_failure(test, msg, checkFail, newCov = False):
    global failCount, reduceTime, repeatCount, failures, quickCount, failCloud, cloudFailures, allClouds

    sys.stdout.flush()

    if not newCov:
        failCount += 1
        print msg
        f = sut.failure()
        print "ERROR:",f
        print "TRACEBACK:"
        traceback.print_tb(f[2])
    else:
        print "Handling new coverage for quick testing"
        snew = sut.newCurrStatements()
        for s in snew:
            print "NEW STATEMENT",s
        bnew = sut.newCurrBranches()
        for b in bnew:
            print "NEW BRANCH",b
        trep = sut.replay(test)
        sremove = []
        scov = sut.currStatements()
        for s in snew:
            if s not in scov:
                print "REMOVING",s
                sremove.append(s)
        for s in sremove:
            snew.remove(s)
        bremove = []
        bcov = sut.currBranches()
        for b in bnew:
            if b not in bcov:
                print "REMOVING",b
                bremove.append(b)
        for b in bremove:
            bnew.remove(b)
        beforeReduceS = set(sut.allStatements())
        beforeReduceB = set(sut.allBranches())
    print "Original test has",len(sut.test()),"steps"
    cloudMatch = False
    if not config.full:
        if not checkFail:
            failProp = sut.fails
        else:
            failProp = sut.failsCheck
        if newCov:
            failProp = sut.coversAll(snew,bnew)
        print "REDUCING..."
        startReduce = time.time()
        original = test
        test = sut.reduce(test, failProp, True, config.keep)
        print "Reduced test has",len(test),"steps"
        print "REDUCED IN",time.time()-startReduce,"SECONDS"
        sut.prettyPrintTest(test)
        if config.essentials:
            print "FINDING ESSENTIAL ELEMENTS OF REDUCED TEST"
            (canRemove, cannotRemove) = sut.reduceEssentials(test, original, failProp, True, config.keep)
            print len(canRemove),len(cannotRemove)
            for (c,reducec) in canRemove:
                print "CAN BE REMOVED:",map(lambda x:x[0], c)
                i = 0
                sut.prettyPrintTest(reducec)
        sys.stdout.flush()
        if config.normalize:
            startSimplify = time.time()
            print "NORMALIZING..."
            test = sut.normalize(test, failProp, True, config.keep, verbose = True, speed = config.speed, noReassigns = config.noreassign)
            print "Normalized test has",len(test),"steps"
            print "NORMALIZED IN",time.time()-startSimplify,"SECONDS"
        if (config.gendepth != None) and (test not in map(lambda x:x[0],failures)) and (test not in cloudFailures):
            startCheckCloud = time.time()
            print "GENERATING GENERALIZATION CLOUD"
            (cloudFound,matchTest,thisCloud) = sut.generalize(test, failProp, silent=True, returnCollect=True, depth=config.gendepth, targets = allClouds)
            print "CLOUD GENERATED IN",time.time()-startCheckCloud,"SECONDS"
            print "CLOUD LENGTH =",len(thisCloud)
            if cloudFound:
                print "CLOUD MATCH",
                faili = 0
                for (cfailbase,err) in failures:
                    cfail = sut.captureReplay(cfailbase)
                    if matchTest in failCloud[cfail]:
                        print "THIS TEST CAN BE CONVERTED TO:"
                        sut.prettyPrintTest(matchTest)
                        print "MATCHING FAILURE",faili
                        break
                    faili += 1
                cloudMatch = True
                cloudFailures.append(test)
        if config.generalize and (test not in map(lambda x:x[0],failures)):
            startGeneralize = time.time()
            print "GENERALIZING..."
            sut.generalize(test, failProp, verbose = True)
            print "GENERALIZED IN",time.time()-startGeneralize,"SECONDS"            
        reduceTime += time.time()-startReduce

    i = 0
    outf = None
    if ((config.output != None) and (test not in map(lambda x:x[0],failures))) or (config.quickTests):
        outname = config.output
        if (outname != None) and config.multiple and not newCov:
            outname += ("." + str(failCount))
        if config.quickTests and newCov:
            for s in sut.allStatements():
                if s not in beforeReduceS:
                    print "NEW STATEMENT FROM REDUCTION",s
            for b in sut.allBranches():
                if b not in beforeReduceB:
                    print "NEW BRANCH FROM REDUCTION",b
            outname = "quicktest." + str(quickCount)
            quickCount += 1
        if outname != None:
            outf = open(outname,'w')
    if config.failedLogging != None:
        sut.setLog(config.failedLogging)
    print
    print "FINAL VERSION OF TEST, WITH LOGGED REPLAY:"
    i = 0
    for s in test:
        steps = "# STEP " + str(i)
        print sut.prettyName(s[0]).ljust(80-len(steps),' '),steps
        sut.safely(s)
        i += 1
        if outf != None:
            outf.write(sut.serializable(s)+"\n")
    if not newCov:
        f = sut.failure()
        print "ERROR:",f
        print "TRACEBACK:"
        traceback.print_tb(f[2])
    sys.stdout.flush()
    if outf != None:
        outf.close()
    if config.multiple:
        if (test in map(lambda x:x[0], failures)) or (test in cloudFailures) or cloudMatch:
            print "NEW FAILURE IS IDENTICAL TO PREVIOUSLY FOUND FAILURE, NOT STORING"
            repeatCount += 1
        else:
            failures.append((test,sut.failure()))
            if config.gendepth != None:
                failCloud[sut.captureReplay(test)] = thisCloud
                for c in thisCloud:
                    allClouds[c] = True
            print "FAILURE IS NEW, STORING; NOW",len(failures),"DISTINCT FAILURES"


def main():
    global failCount,sut,config,reduceTime,quickCount,repeatCount,failures,cloudFailures,R,opTime,checkTime,guardTime,restartTime,nops,ntests
    
    parsed_args, parser = parse_args()
    config = make_config(parsed_args, parser)
    print('Random testing using config={}'.format(config))

    R = random.Random(config.seed)

    start = time.time()
    elapsed = time.time()-start

    failCount = 0
    quickCount = 0
    repeatCount = 0
    failures = []
    cloudFailures = []

    if config.gendepth != None:
        failCloud = {}
        allClouds = {}

    sut = SUT.sut()
    if config.logging != None:
        sut.setLog(config.logging)

    if not config.nocover:
        sut.silenceCoverage()
        
    tacts = sut.actions()
    a = None
    sawNew = False

    nops = 0
    ntests = 0
    reduceTime = 0.0
    opTime = 0.0
    checkTime = 0.0
    guardTime = 0.0
    restartTime = 0.0

    checkResult = True

    if config.total:
        fulltest = open("fulltest.txt",'w')

    if config.verbose:
        print "ABOUT TO START TESTING"
        sys.stdout.flush()
        
    while (config.maxtests == -1) or (ntests < config.maxtests):
        if config.verbose:
            print "STARTING TEST",ntests
            sys.stdout.flush()
        ntests += 1

        startRestart = time.time()
        sut.restart()
        restartTime += time.time() - startRestart

        if config.total:
            fulltest.write("<<RESTART>>\n")
        
        if config.replayable:
            currtest = open("currtest.txt",'w')

        for s in xrange(0,config.depth):
            if config.verbose:
                print "GENERATING STEP",s

            startGuard = time.time()
            tryStutter = (a != None) and (a[1]()) and ((config.stutter != None) or config.greedyStutter)

            if tryStutter:
                if (config.stutter == None) or (R.random() > config.stutter):
                    tryStutter = False
                if (config.greedyStutter) and sawNew:
                        print "TRYING TO STUTTER DUE TO COVERAGE GAIN"
                        tryStutter = True
            else:
                 a = sut.randomEnabled(R)   

            if a == None:
                print "WARNING: DEADLOCK (NO ENABLED ACTIONS)"
                
            guardTime += time.time()-startGuard
            elapsed = time.time() - start
            if elapsed > config.timeout:
                print "STOPPING TEST DUE TO TIMEOUT, TERMINATED AT LENGTH",len(sut.test())
                break
            if a == None:
                print "TERMINATING TEST DUE TO NO ENABLED ACTIONS"
                break                
            if tryStutter:
                print "STUTTERING WITH",a[0]
            nops += 1

            if config.replayable:
                currtest.write(a[0] + "\n")
                currtest.flush()

            if config.total:
                fulltest.write(a[0] + "\n")
                fulltest.flush()            

            if config.verbose:
                print "ACTION:",sut.prettyName(a[0])
                
            startOp = time.time()
            stepOk = sut.safely(a)
            if sut.warning() != None:
                print "SUT WARNING:",sut.warning()
            opTime += (time.time()-startOp)
            if tryStutter:
                print "DONE STUTTERING"
            if (not config.uncaught) and (not stepOk):
                handle_failure(sut.test(), "UNCAUGHT EXCEPTION", False)
                if not config.multiple:
                    print "STOPPING TESTING DUE TO FAILED TEST"
                break

            startCheck = time.time()
            if not config.ignoreprops:
                checkResult = sut.check()
                checkTime += time.time()-startCheck
            if not checkResult:
                handle_failure(sut.test(), "PROPERLY VIOLATION", True)
                if not config.multiple:
                    print "STOPPING TESTING DUE TO FAILED TEST"
                break
                
            elapsed = time.time() - start
            if config.running:
                if sut.newBranches() != set([]):
                    print "ACTION:",a[0],tryStutter
                    for b in sut.newBranches():
                        print elapsed,len(sut.allBranches()),"New branch",b
                    sawNew = True
                else:
                    sawNew = False
                if sut.newStatements() != set([]):
                    print "ACTION:",a[0],tryStutter
                    for s in sut.newStatements():
                        print elapsed,len(sut.allStatements()),"New statement",s
                    sawNew = True
                else:
                    sawNew = False                

            if elapsed > config.timeout:
                print "STOPPING TEST DUE TO TIMEOUT, TERMINATED AT LENGTH",len(sut.test())
                break
            
        if config.replayable:
            currtest.close()
        if config.quickTests:
            if (sut.newCurrBranches() != set([])) or (sut.newCurrStatements() != set([])):
                handle_failure(sut.test(), "NEW COVERAGE", False, newCov=True)
        if (not config.multiple) and (failCount > 0):
            break
        if elapsed > config.timeout:
            print "STOPPING TESTING DUE TO TIMEOUT"
            break        

    if config.total:
        fulltest.close()
        
    if not config.nocover:
        sut.restart()
        print sut.report(config.coverfile),"PERCENT COVERED"

        if config.internal:
            sut.internalReport()
        
        if config.html:
            sut.htmlReport(config.html)

    print time.time()-start, "TOTAL RUNTIME"
    print ntests, "EXECUTED"
    print nops, "TOTAL TEST OPERATIONS"
    print opTime, "TIME SPENT EXECUTING TEST OPERATIONS"
    print guardTime, "TIME SPENT EVALUATING GUARDS AND CHOOSING ACTIONS"
    if not config.ignoreprops:
        print checkTime, "TIME SPENT CHECKING PROPERTIES"
        print (opTime + checkTime), "TOTAL TIME SPENT RUNNING SUT"
    print restartTime, "TIME SPENT RESTARTING"
    print reduceTime, "TIME SPENT REDUCING TEST CASES"
    if config.multiple:
        print failCount,"FAILED"
        print repeatCount,"REPEATS OF FAILURES"
        print len(failures),"ACTUAL DISTINCT FAILURES"
        print 
        n = 0
        for (test, err) in failures:
            print "FAILURE",n
            sut.prettyPrintTest(test)
            n += 1
            if err != None:
                print "ERROR:", err
                print "TRACEBACK:"
                traceback.print_tb(err[2])
        i = -1
        if config.compareFails: # Comparison feature normally not useful, just for researching normalization
            for test1 in failures:
                i += 1
                j = -1
                for test2 in failures:
                    j += 1
                    if (j > i):
                        print "COMPARING FAILURE",i,"AND FAILURE",j
                        for k in xrange(0,max(len(test1),len(test2))):
                            if k >= len(test1):
                                print "STEP",k,"-->",test2[k][0]
                            elif k >= len(test2):
                                print "STEP",k,test1[k][0],"-->"                        
                            elif test1[k] != test2[k]:
                                print "STEP",k,test1[k][0],"-->",test2[k][0]
            
    if not config.nocover:
        print len(sut.allBranches()),"BRANCHES COVERED"
        print len(sut.allStatements()),"STATEMENTS COVERED"

if __name__ == '__main__':
    main()
