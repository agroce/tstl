import sut as SUT
import random
import time
import sys
import traceback
import argparse
import os
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
        f = t.failure()
        print "ERROR:",f
        print "TRACEBACK:"
        traceback.print_tb(f[2])
    else:
        print "Handling new coverage for quick testing"
        snew = t.newCurrStatements()
        for s in snew:
            print "NEW STATEMENT",s
        bnew = t.newCurrBranches()
        for b in bnew:
            print "NEW BRANCH",b
        trep = t.replay(test)
        sremove = []
        scov = t.currStatements()
        for s in snew:
            if s not in scov:
                print "REMOVING",s
                sremove.append(s)
        for s in sremove:
            snew.remove(s)
        bremove = []
        bcov = t.currBranches()
        for b in bnew:
            if b not in bcov:
                print "REMOVING",b
                bremove.append(b)
        for b in bremove:
            bnew.remove(b)
        beforeReduceS = set(t.allStatements())
        beforeReduceB = set(t.allBranches())
    print "Original test has",len(test),"steps"
    cloudMatch = False
    if not config.full:
        if not checkFail:
            failProp = t.fails
        else:
            failProp = t.failsCheck
        if newCov:
            failProp = t.coversAll(snew,bnew)
        print "REDUCING..."
        startReduce = time.time()
        original = test
        test = t.reduce(test, failProp, True, config.keep)
        print "Reduced test has",len(test),"steps"
        print "REDUCED IN",time.time()-startReduce,"SECONDS"
        i = 0
        for s in test:
            print "STEP",i,t.prettyName(s[0])
            i += 1
        if config.essentials:
            print "FINDING ESSENTIAL ELEMENTS OF REDUCED TEST"
            (canRemove, cannotRemove) = t.reduceEssentials(test, original, failProp, True, config.keep)
            print len(canRemove),len(cannotRemove)
            for (c,reducec) in canRemove:
                print "CAN BE REMOVED:",map(lambda x:x[0], c)
                i = 0
                for s in reducec:
                    print t.prettyName(s[0]),"# STEP",i
                    i += 1
        sys.stdout.flush()
        if config.normalize:
            startSimplify = time.time()
            print "NORMALIZING..."
            test = t.normalize(test, failProp, True, config.keep, verbose = True, speed = config.speed)
            print "Normalized test has",len(test),"steps"
            print "NORMALIZED IN",time.time()-startSimplify,"SECONDS"
        if (config.gendepth != None) and (test not in failures) and (test not in cloudFailures):
            startCheckCloud = time.time()
            print "GENERATING GENERALIZATION CLOUD"
            (cloudFound,matchTest,thisCloud) = t.generalize(test, failProp, silent=True, returnCollect=True, depth=config.gendepth, targets = allClouds)
            print "CLOUD GENERATED IN",time.time()-startCheckCloud,"SECONDS"
            print "CLOUD LENGTH =",len(thisCloud)
            if cloudFound:
                print "CLOUD MATCH",
                faili = 0
                for cfailbase in failures:
                    cfail = t.captureReplay(cfailbase)
                    if matchTest in failCloud[cfail]:
                        print "THIS TEST CAN BE CONVERTED TO:"
                        i = 0
                        for s in t.replayable(matchTest):
                            print t.prettyName(s[0]),"  # STEP",i
                            i += 1
                        print "MATCHING FAILURE",faili
                        break
                    faili += 1
                cloudMatch = True
                cloudFailures.append(test)
        if config.generalize and (test not in failures):
            startGeneralize = time.time()
            print "GENERALIZING..."
            t.generalize(test, failProp, verbose = True)
            print "GENERALIZED IN",time.time()-startGeneralize,"SECONDS"            
        reduceTime += time.time()-startReduce

    i = 0
    if ((config.output != None) and (test not in failures)) or (config.quickTests):
        outname = config.output
        if config.quickTests:
            for s in t.allStatements():
                if s not in beforeReduceS:
                    print "NEW STATEMENT FROM REDUCTION",s
            for b in t.allBranches():
                if b not in beforeReduceB:
                    print "NEW BRANCH FROM REDUCTION",b
            outname = "quicktest." + str(quickCount)
            quickCount += 1
        if config.multiple:
            outname += ("." + str(failCount))
        outf = open(outname,'w')
    else:
        outf = None
    if config.failedLogging != None:
        t.setLog(config.failedLogging)
    print
    print "FINAL VERSION OF TEST, WITH LOGGED REPLAY:"
    for s in test:
        print t.prettyName(s[0]),"  # STEP",i
        t.safely(s)
        i += 1
        if outf != None:
            outf.write(t.serializable(s)+"\n")
    if not newCov:
        f = t.failure()
        print "ERROR:",f
        print "TRACEBACK:"
        traceback.print_tb(f[2])
    sys.stdout.flush()
    if outf != None:
        outf.close()
    if config.multiple:
        if (test in failures) or (test in cloudFailures) or cloudMatch:
            print "NEW FAILURE IS IDENTICAL TO PREVIOUSLY FOUND FAILURE, NOT STORING"
            repeatCount += 1
        else:
            failures.append(test)
            if config.gendepth != None:
                failCloud[t.captureReplay(test)] = thisCloud
                for c in thisCloud:
                    allClouds[c] = True
            print "FAILURE IS NEW, STORING; NOW",len(failures),"DISTINCT FAILURES"

    
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

t = SUT.sut()
if config.logging != None:
    t.setLog(config.logging)

tacts = t.actions()
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
    t.restart()
    restartTime += time.time() - startRestart
    test = []

    if config.total:
        fulltest.write("<<RESTART>>\n")
    
    if config.replayable:
        currtest = open("currtest.txt",'w')

    for s in xrange(0,config.depth):
        if config.verbose:
            print "GENERATING STEP",s
        
        startGuard = time.time()
        acts = tacts
        while True:
            elapsed = time.time() - start

            if elapsed > config.timeout:
                break
            
            tryStutter = (a != None)
            if tryStutter:
                if (config.stutter == None) and (not config.greedyStutter):
                    tryStutter = False
            if tryStutter:
                if (config.stutter == None) or (R.random() > config.stutter):
                    tryStutter = False
                if (config.greedyStutter) and sawNew:
                    print "TRYING TO STUTTER DUE TO COVERAGE GAIN"
                    tryStutter = True
            if not tryStutter:
                if len(acts) == 1:
                    p = 0
                else:    
                    p = R.randint(0,len(acts)-1)
                a = acts[p]
            if a[1]():
                break
            else:
                a = None
            acts = acts[:p] + acts[p+1:]
        guardTime += time.time()-startGuard
        elapsed = time.time() - start
        if elapsed > config.timeout:
            print "STOPPING TEST DUE TO TIMEOUT, TERMINATED AT LENGTH",len(test)
            break
            
        if tryStutter:
            print "STUTTERING WITH",a[0]
        test.append(a)
        nops += 1

        if config.replayable:
            currtest.write(a[0] + "\n")
            currtest.flush()

        if config.total:
            fulltest.write(a[0] + "\n")
            fulltest.flush()            

        if config.verbose:
            print "ACTION:",t.prettyName(a[0])
            
        startOp = time.time()
        stepOk = t.safely(a)
        opTime += (time.time()-startOp)
        if tryStutter:
            print "DONE STUTTERING"
        if (not config.uncaught) and (not stepOk):
            handle_failure(test, "UNCAUGHT EXCEPTION", False)
            if not config.multiple:
                print "STOPPING TESTING DUE TO FAILED TEST"
            break

        startCheck = time.time()
        if not config.ignoreprops:
            checkResult = t.check()
            checkTime += time.time()-startCheck
        if not checkResult:
            handle_failure(test, "PROPERLY VIOLATION", True)
            if not config.multiple:
                print "STOPPING TESTING DUE TO FAILED TEST"
            break
            
        elapsed = time.time() - start
        if config.running:
            if t.newBranches() != set([]):
                print "ACTION:",a[0],tryStutter
                for b in t.newBranches():
                    print elapsed,len(t.allBranches()),"New branch",b
                sawNew = True
            else:
                sawNew = False
            if t.newStatements() != set([]):
                print "ACTION:",a[0],tryStutter
                for s in t.newStatements():
                    print elapsed,len(t.allStatements()),"New statement",s
                sawNew = True
            else:
                sawNew = False                

        if elapsed > config.timeout:
            print "STOPPING TEST DUE TO TIMEOUT, TERMINATED AT LENGTH",len(test)
            break
        
    if config.replayable:
        currtest.close()
    if config.quickTests:
        if (t.newCurrBranches() != set([])) or (t.newCurrStatements() != set([])):
            handle_failure(test, "NEW COVERAGE", False, newCov=True)
    if (not config.multiple) and (failCount > 0):
        break
    if elapsed > config.timeout:
        print "STOPPING TESTING DUE TO TIMEOUT"
        break        

if config.total:
    fulltest.close()
    
if not config.nocover:
    t.restart()
    print t.report(config.coverfile),"PERCENT COVERED"

    if config.internal:
        t.internalReport()
    
    if config.html:
        t.htmlReport(config.html)

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
    for test in failures:
        print "FAILURE",n
        i = 0
        for s in test:
            print "STEP",i,s[0]
            i += 1
        n += 1
    i = -1
    if False:
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
    print len(t.allBranches()),"BRANCHES COVERED"
    print len(t.allStatements()),"STATEMENTS COVERED"
