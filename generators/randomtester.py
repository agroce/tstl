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
    parser.add_argument('-k', '--keep', action='store_true',
                        help="Keep last action the same when reducing.")
    parser.add_argument('-o', '--output', type=str, default=None,
                        help="Filename to save failing test(s).")
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
    global failCount
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
        test = t.reduce(test, failProp, True, config.keep)
        print "Reduced test has",len(test),"steps"

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
    for s in test:
        print "STEP",i,s[0]
        t.safely(s)
        i += 1
        if outf != None:
            outf.write(t.serializeable(s)+"\n")
    if outf != None:
        outf.close()
    
parsed_args, parser = parse_args()
config = make_config(parsed_args, parser)
print('Random testing using config={}'.format(config))

R = random.Random(config.seed)

start = time.time()
elapsed = time.time()-start

failCount = 0

t = SUT.sut()
if config.logging != None:
    t.setLog(config.logging)

tacts = t.actions()
a = None
sawNew = False

nops = 0
ntests = 0
optime = 0.0
while (config.maxtests == -1) or (ntests < config.maxtests):
    ntests += 1

    t.restart()
    test = []

    for s in xrange(0,config.depth):

        acts = tacts
        while True:
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

        if tryStutter:
            print "STUTTERING WITH",a[0]
        test.append(a)
        nops += 1

        opstart = time.time()
        stepOk = t.safely(a)
        optime += (time.time()-opstart)
        if tryStutter:
            print "DONE STUTTERING"
        if (not config.uncaught) and (not stepOk):
            handle_failure(test, "UNCAUGHT EXCEPTION", False)
            if not config.multiple:
                print "STOPPING TESTING DUE TO FAILED TEST"
            break
                
        if (not config.ignoreprops) and (not t.check()):
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
    if (not config.multiple) and (failCount > 0):
        break
    if elapsed > config.timeout:
        print "STOPPING TESTING DUE TO TIMEOUT"
        break        

if not config.nocover:
    print t.report(config.coverfile),"PERCENT COVERED"

    if config.html:
        t.htmlReport(config.html)

print ntests, "EXECUTED"
print nops, "TOTAL TEST OPERATIONS"
print optime, "TIME SPENT EXECUTING TEST OPERATIONS"
if config.multiple:
    print failCount,"FAILED"
if not config.nocover:
    print len(t.allBranches()),"BRANCHES COVERED"
    print len(t.allStatements()),"STATEMENTS COVERED"
