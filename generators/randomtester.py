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
    parser.add_argument('-C', '--canonize', action='store_true',
                        help="Canonize/simplify after reduction.")
    parser.add_argument('-e', '--speed', type=str, default="FAST",
                        help='Canonization/simplification speed (default = FAST).')    
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
    parser.add_argument('-c', '--coverfile', type=str, default="coverage.out",
                        help="File to write coverage report to ('coverage.out' default).")
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

def handle_failure(test, msg, checkFail):
    global failCount, reduceTime, repeatCount, failures

    sys.stdout.flush()
    
    failCount += 1
    print msg
    f = t.failure()
    print "ERROR:",f
    print "TRACEBACK:"
    traceback.print_tb(f[2])

    print "Original test has",len(test),"steps"
    if not config.full:
        if not checkFail:
            failProp = t.fails
        else:
            failProp = t.failsCheck
        print "REDUCING..."
        startReduce = time.time()
        test = t.reduce(test, failProp, True, config.keep)
        print "Reduced test has",len(test),"steps"
        print "REDUCED IN",time.time()-startReduce,"SECONDS"
        i = 0
        for s in test:
            print "STEP",i,s[0]
            i += 1
        sys.stdout.flush()
        if config.canonize:
            startSimplify = time.time()
            print "SIMPLIFYING..."
            test = t.simplify(test, failProp, True, config.keep, verbose = True, speed = config.speed)
            print "Simplified test has",len(test),"steps"
            print "SIMPLIFIED IN",time.time()-startSimplify,"SECONDS"
        reduceTime += time.time()-startReduce

    i = 0
    if config.output != None:
        outname = config.output
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
        print "STEP",i,s[0]
        t.safely(s)
        i += 1
        if outf != None:
            outf.write(t.serializeable(s)+"\n")
    sys.stdout.flush()
    if outf != None:
        outf.close()
    if config.multiple:
        if test in failures:
            print "NEW FAILURE IS IDENTICAL TO PREVIOUSLY FOUND FAILURE, NOT STORING"
            repeatCount += 1
        else:
            failures.append(test)
            print "FAILURE IS NEW, STORING; NOW",len(failures),"DISTINCT FAILURES"

    
parsed_args, parser = parse_args()
config = make_config(parsed_args, parser)
print('Random testing using config={}'.format(config))

R = random.Random(config.seed)

start = time.time()
elapsed = time.time()-start

failCount = 0
repeatCount = 0
failures = []

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

while (config.maxtests == -1) or (ntests < config.maxtests):
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
        
        if elapsed > config.timeout:
            print "STOPPING TEST DUE TO TIMEOUT, TERMINATED AT LENGTH",len(test)
            break
    if config.replayable:
        currtest.close()
    if (not config.multiple) and (failCount > 0):
        break
    if elapsed > config.timeout:
        print "STOPPING TESTING DUE TO TIMEOUT"
        break        

if config.total:
    fulltest.close()
    
if not config.nocover:
    print t.report(config.coverfile),"PERCENT COVERED"

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
    n = 0
    for test in failures:
        print "FAILURE",n
        i = 0
        for s in test:
            print "STEP",i,s[0]
            i += 1
        n += 1
    i = -1
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
