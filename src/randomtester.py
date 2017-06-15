import os
import sys
import math
import random
import time
import traceback
import argparse
import glob
import datetime
from collections import namedtuple

# Appending current working directory to sys.path
# So that user can run randomtester from the directory where sut.py is located
current_working_dir = os.getcwd()
sys.path.append(current_working_dir)

import sut as SUT

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--timeout', type=int, default=3600,
                        help='Timeout in seconds (3600 default).')
    parser.add_argument('-s', '--seed', type=int, default=None,
                        help='Random seed (default = None).')    
    parser.add_argument('-d', '--depth', type=int, default=100,
                        help='Maximum search depth (100 default).')
    parser.add_argument('-w', '--swarm', action='store_true',
                        help="Turn on standard swarm testing.")
    parser.add_argument('-r', '--running', action='store_true',
                        help="Produce running branch coverage report.")    
    parser.add_argument('--normalize', action='store_true',
                        help="Normalize/simplify after reduction.")
    parser.add_argument('--generalize', action='store_true',
                        help="Generalize tests.")
    parser.add_argument('-n', '--noCover', action='store_true',
                        help="Don't produce a coverage report at the end.")
    parser.add_argument('--html', type=str, default=None,
                        help="Write HTML report (directory to write to, None/no html report by default).")    
    parser.add_argument('-m', '--maxTests', type=int, default=-1,
                        help='Maximum #tests to run (-1 = infinite default).')
    parser.add_argument('-o', '--output', type=str, default="failure."+str(os.getpid())+".test",
                        help="Filename to save failing test(s).")
    parser.add_argument('-M', '--multiple', action='store_true',
                        help="Allow multiple failures.")
    parser.add_argument('--replayable', action='store_true',
                        help="Keep replayable file of current test, in case of crash.")
    parser.add_argument('--total', action='store_true',
                        help="Keep a file with ALL TESTING ACTIONS in case of crash.")    
    parser.add_argument('--noCheck', action='store_true',                            
                        help='Do not check properties.')
    parser.add_argument('--uncaught', action='store_true',
                        help='Allow uncaught exceptions in actions.')
    parser.add_argument('-q', '--quickTests', action='store_true',
                        help="Produce quick tests for coverage (save a test for each newly reached coverage target).")
    parser.add_argument('--readQuick', action='store_true',
                        help="Read existing quick tests (and add to them if producing quick tests).")        
    parser.add_argument('--localize', action='store_true',
                        help="Produce fault localization (Ochai formula) if there are any failing tests.")
    parser.add_argument('--full', action='store_true',
                        help="Don't reduce -- report full failing test.")
    parser.add_argument('-l', '--logging', type=int, default=None,
                        help="Set logging level")
    parser.add_argument('--failedLogging', type=int, default=None,
                        help="Set failed test case logging level")        
    parser.add_argument('--progress', action='store_true',
                        help="Turn on progress report.")
    parser.add_argument('--timedProgress', type=int, default=30,
                        help="Turn on progress reports at x second intervals (default = 30 seconds).")
    parser.add_argument('--enumerateEnabled', action='store_true',
                        help="Instead of guessing enabled actions, enumerate them; can speed testing greatly for cases where almost all actions are usually disabled.")
    parser.add_argument('--noEnumerateEnabled', action='store_true',
                        help="Turn off enumeration of enabled actions in SUTs compiled to default to that behavior.")
    parser.add_argument('-k', '--keepLast', action='store_true',
                        help="Keep last action the same when reducing/normalizing: slippage avoidance heuristic.")
    parser.add_argument('--swarmP', type=float, default=0.5,
                        help="Swarm inclusion probability.")
    parser.add_argument('--computeFeatureStats', action="store_true",
                        help="When using swarm testing, compute coverage triggers and suppressors")
    parser.add_argument('--highLowSwarm', type=float, default=None,
                        help="Apply high/low probability swarm testing with high portion of action being P.")
    parser.add_argument('--swarmProbs', type=str, default=None,
                        help="File with probabilities for any kind of swarm.")
    parser.add_argument('--swarmSwitch', type=int, default=None,
                        help="How many times to switch swarm config during each test.")
    parser.add_argument('--swarmLength', type=int, default=None,
                        help="How long a swarm config persists (only relevant with --swarmSwitch).")
    parser.add_argument('--probs', type=str, default=None,
                        help="Guide testing by an action class probability file.")
    parser.add_argument('--LOCProbs', action='store_true',
                        help="Guide testing by approximate relative lines of top-level code called by actions.")
    parser.add_argument('--LOCBaseline', type=float, default=0.2,
                        help="Baseline probability for actions that do not seem to call any SUT code.")  
    parser.add_argument('--markov', type=str, default=None,
                        help="Guide testing by a Markov model file.")
    parser.add_argument('-x', '--exploit', type=float, default=None,
                        help="Probability to exploit stored coverage tests.")
    parser.add_argument('-X', '--startExploit', type=int, default=0,
                        help="Time at which exploitation starts.")
    parser.add_argument("--verboseExploit",action='store_true',
                        help="Exploitation is verbose (info on pool, etc.).")    
    parser.add_argument("--reducePool",action='store_true',
                        help="Reduce tests by their new coverage before adding to exploitation pool.")
    parser.add_argument('--exploitCeiling', type=float, default=0.1,
                        help="Max ratio to mean coverage count for exploitation.")
    parser.add_argument('--Pmutate', type=float, default=0.0,
                        help="Probability to mutate exploited tests (default = 0.0 -- no mutation).")
    parser.add_argument('--Pcrossover', type=float, default=0.2,
                        help="Probability to try crossover when mutating exploited tests (default = 0.2).")
    parser.add_argument("--useHints",action='store_true',
                        help="Use hint values (utility to maximize) as another cause for exploitation.")
    parser.add_argument("--noCoverageExploit",action="store_true",
                        help="Do not use coverage in exploitation (only useful with heuristic hints).")
    parser.add_argument("--exploitBestHint",type=int,default=1,
                        help="How many of the best heuristic values to put in active pool for exploitation.")    
    parser.add_argument('--internal', action='store_true',
                        help="Produce internal coverage report at the end, as sanity check on coverage.py results.")    
    parser.add_argument('--coverFile', type=str, default="coverage.out",
                        help="File to write coverage report to ('coverage.out' default).")
    parser.add_argument('--noExceptionMatch', action='store_true',
                        help="Do not force exceptions in reduced / normalized failures to match.")        
    parser.add_argument('-v', '--verbose', action='store_true',
                        help="Run in verbose mode.")
    parser.add_argument('--silentFail', action='store_true',
                        help="Don't make failure replays verbose.")            
    parser.add_argument('--throughput', action='store_true',
                        help='Measure action throughput.')
    parser.add_argument('--profile', action='store_true',
                        help="Profile actions.")
    parser.add_argument('--stopWhenBranches', type=int, default=None,
                        help="Stop when branch coverage exceeds a given target value.")
    parser.add_argument('--stopWhenStatements', type=int, default=None,
                        help="Stop when statement coverage exceeds a given target value.")    
    parser.add_argument('--verboseActions', action='store_true',
                        help="Make test actions verbose.")
    parser.add_argument('--showActions', action='store_true',
                        help="Show actions as they run")
    parser.add_argument('--noAlphaConvert', action='store_true',
                        help="Do not alpha convert failing tests.")        
    parser.add_argument('--compareFails', action='store_true',
                        help="Compare all failing tests.")
    parser.add_argument('--noSwarmDependencies', action='store_true',
                        help="[EXPERIMENTAL] This forces swarm to not use dependencies.  Not so much experimental as just a bad idea.")
    parser.add_argument('--genDepth', type=int, default=None,
                        help = "[EXPERIMENTAL] Generalization depth for cloud overlap comparisons (default = None).")
    parser.add_argument('--stutter', type=float, default=None,
                        help="[EXPERIMENTAL] Repeat last action if still enabled with P = <stutter>.")
    parser.add_argument('--greedyStutter', action='store_true',
                        help="[EXPERIMENTAL] Repeat last action if it is enabled and improved coverage.")
    parser.add_argument('--essentials', action='store_true',
                        help="[EXPERIMENTAL] Determine essential elements in failing test.")    
    parser.add_argument('--quickAnalysis', action='store_true',
                        help="[EXPERIMENTAL] Reduce tests by branch coverage, collect action frequencies in reductions.")
    parser.add_argument('--uniqueValuesAnalysis', action='store_true',
                        help="[EXPERIMENTAL] Quick analysis based on unique values, not coverage.")    
    parser.add_argument('--fastQuickAnalysis', action='store_true',
                        help="[EXPERIMENTAL] Quick analysis skips analyzing branch/statement if previously analyzed already covers.")
    parser.add_argument('--speed', type=str, default="FAST",
                        help='[EXPERIMENTAL] Normalization/simplification speed (default = FAST).')        
    parser.add_argument('--noReassign', action='store_true',
                        help="[EXPERIMENTAL] Add noReassign rule to normalization steps.")
    parser.add_argument('--relax', action='store_true',
                        help="[EXPERIMENTAL] Use relaxed semantics (not recommended for even experts, really).")    
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
    global failCount, reduceTime, repeatCount, failures, quickCount, failCloud, cloudFailures, allClouds, localizeSFail, localizeBFail, failFileCount,fulltest
    test = list(test)
    sys.stdout.flush()
    if not newCov:
        failCount += 1
        print msg
        f = sut.failure()
        print "ERROR:",f
        print "TRACEBACK:"
        traceback.print_tb(f[2],file=sys.stdout)
        sut.saveTest(test,config.output.replace(".test",".full.test"))
    else:
        print "Handling new coverage for quick testing"
        snew = sut.newCurrStatements()
        for s in snew:
            print "NEW STATEMENT",s
        bnew = sut.newCurrBranches()
        for b in bnew:
            print "NEW BRANCH",b
        trep = sut.replay(test,catchUncaught=True,checkProp=(not config.noCheck))
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
    print "Original test has",len(test),"steps"
    cloudMatch = False
    if not config.full:
        if not checkFail:
            if config.noExceptionMatch:
                failProp = sut.fails
            else:
                failProp = lambda x: sut.fails(x,failure=f)                
        else:
            if config.noExceptionMatch:
                failProp = sut.failsCheck
            else:
                failProp = lambda x: sut.failsCheck(x,failure=f)
        if newCov:
            failProp = sut.coversAll(snew,bnew,catchUncaught=True,checkProp=(not config.noCheck))
        print "REDUCING..."
        startReduce = time.time()
        original = test
        test = sut.reduce(test, failProp, True, keepLast = config.keepLast)
        if not newCov:
            sut.saveTest(test,config.output.replace(".test",".reduced.test"))        
        print "Reduced test has",len(test),"steps"
        print "REDUCED IN",time.time()-startReduce,"SECONDS"
        if not config.noAlphaConvert:
            print "Alpha converting test..."
            test = sut.alphaConvert(test)
            if not newCov:
                sut.saveTest(test,config.output.replace(".test",".reduced.test"))                    
        sut.prettyPrintTest(test)
        if config.essentials:
            print "FINDING ESSENTIAL ELEMENTS OF REDUCED TEST"
            (canRemove, cannotRemove) = sut.reduceEssentials(test, original, failProp, True, keepLast = config.keepLast)
            print len(canRemove),len(cannotRemove)
            for (c,reducec) in canRemove:
                print "CAN BE REMOVED:",map(lambda x:x[0], c)
                i = 0
                sut.prettyPrintTest(reducec)
        sys.stdout.flush()
        if config.normalize:
            startSimplify = time.time()
            print "NORMALIZING..."
            test = sut.normalize(test, failProp, True, keepLast = config.keepLast, verbose = True, speed = config.speed, noReassigns = config.noReassign, useCache=False)
            print "Normalized test has",len(test),"steps"
            print "NORMALIZED IN",time.time()-startSimplify,"SECONDS"
            sut.saveTest(test,config.output.replace(".test",".normalized.test"))
        if (config.genDepth != None) and (test not in map(lambda x:x[0],failures)) and (test not in cloudFailures):
            startCheckCloud = time.time()
            print "GENERATING GENERALIZATION CLOUD"
            (cloudFound,matchTest,thisCloud) = sut.generalize(test, failProp, silent=True, returnCollect=True, depth=config.genDepth, targets = allClouds)
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
    if ((config.output != None) and (test not in map(lambda x:x[0],failures))) or (config.quickTests):
        outname = config.output
        if (outname != None) and config.multiple and not newCov:
            outname += ("." + str(failFileCount))
            failFileCount += 1
        if config.quickTests and newCov:
            for s in sut.allStatements():
                if s not in beforeReduceS:
                    print "NEW STATEMENT FROM REDUCTION",s
            for b in sut.allBranches():
                if b not in beforeReduceB:
                    print "NEW BRANCH FROM REDUCTION",b
            outname = "quick" + str(quickCount) + ".test"
            quickCount += 1
        print
        print "SAVING TEST AS",outname
        sut.saveTest(test,outname)
            
    if config.failedLogging != None:
        sut.setLog(config.failedLogging)
    print "FINAL VERSION OF TEST, WITH LOGGED REPLAY:"
    if not config.silentFail:
        sut.verbose(True)
    i = 0
    sut.restart()
    for s in test:
        steps = "# STEP " + str(i)
        print sut.prettyName(s[0]).ljust(80-len(steps),' '),steps
        sut.safely(s)
        if checkFail:
            sut.check()
        i += 1
    if not config.verboseActions:
        sut.verbose(False)
    if not newCov:
        if config.localize:
            for s in sut.currStatements():
                if s not in localizeSFail:
                    localizeSFail[s] = 0
                localizeSFail[s] += 1
            for b in sut.currBranches():
                if b not in localizeBFail:
                    localizeBFail[b] = 0
                localizeBFail[b] += 1
        f = sut.failure()
        if f != None:
            print "ERROR:",f
            print "TRACEBACK:"
            traceback.print_tb(f[2],file=sys.stdout)
        else:
            print "NO FAILURE!"
    sys.stdout.flush()
    if config.multiple:
        if (test in map(lambda x:x[0], failures)) or (test in cloudFailures) or cloudMatch:
            print "NEW FAILURE IS IDENTICAL TO PREVIOUSLY FOUND FAILURE, NOT STORING"
            repeatCount += 1
        else:
            failures.append((test,sut.failure()))
            if config.genDepth != None:
                failCloud[sut.captureReplay(test)] = thisCloud
                for c in thisCloud:
                    allClouds[c] = True
            print "FAILURE IS NEW, STORING; NOW",len(failures),"DISTINCT FAILURES"

def buildActivePool():
    global activePool, reducePool

    activePool = []

    if not config.noCoverageExploit:
        if config.reducePool and len(reducePool) != 0:
            for (t,bs,ss) in reducePool:
                if config.verbose or config.verboseExploit:
                    print "REDUCING POOL TEST FROM",len(t),"STEPS...",
                r = sut.reduce(t,sut.coversAll(ss,bs,checkProp=not(config.noCheck)),verbose=False)
                if config.verbose or config.verboseExploit:            
                    print "TO",len(r),"STEPS:"
                    sut.prettyPrintTest(r)
                    print
                sut.replay(r)
                fullPool.append((r,set(sut.currBranches()), set(sut.currStatements())))
                # Have to make sure if we got some new coverage out of this it's in the coverage map
                # Also need to make sure quickTests know about it
                # Some statistics may be inaccurate, though
                newBranches = set([])
                newStatements = set([])
                for b in sut.currBranches():
                    if b not in branchCoverageCount:
                        newBranches.add(b)
                        branchCoverageCount[b] = 1
                    else:
                        branchCoverageCount[b] += 1
                for s in sut.currStatements():
                    if s not in statementCoverageCount:
                        newStatements.add(s)
                        statementCoverageCount[s] = 1
                    else:
                        statementCoverageCount[s] += 1                     
                if len(newBranches) > 0 or len(newStatements) > 0:
                    sut.newCurrStatements().update(newStatements)
                    sut.newCurrBranches().update(newBranches)
                    # Collect the quick test
                    handle_failure(r,"NEW COVERAGE", False, newCov=True)
            # At this point all of reducePool is in fullPool
            reducePool = []

        if len(branchCoverageCount) >= 1:
            meanBranch = sum(branchCoverageCount.values()) / (len(branchCoverageCount) * 1.0)
        else:
            meanBranch = 0.0
        if len(statementCoverageCount) >= 1:
            meanStatement = sum(statementCoverageCount.values()) / (len(statementCoverageCount) * 1.0)
        else:
            meanStatement = 0.0
        bThreshold = meanBranch * config.exploitCeiling
        sThreshold = meanStatement * config.exploitCeiling
        if config.verbose or config.verboseExploit:
            print "MEAN BRANCH",meanBranch,"THRESHOLD",bThreshold,"/ MEAN STATEMENT",meanStatement,"THRESHOLD",sThreshold
            print len(filter(lambda x:x <= bThreshold, branchCoverageCount.values())),
            print "BRANCHES OF INTEREST OUT OF",len(branchCoverageCount),"/",
            print len(filter(lambda x:x <= sThreshold, statementCoverageCount.values())),
            print "STATEMENTS OF INTEREST OUT OF",len(statementCoverageCount)
        for (t,bs,ss) in fullPool:
            added = False
            for b in bs:
                if b not in branchCoverageCount:
                    branchCoverageCount[b] = 1 # covered during a failure or reduction
                if branchCoverageCount[b] <= bThreshold:
                    activePool.append(t)
                    added = True
                    break
            if not added:
                for s in ss:
                    if s not in statementCoverageCount:
                        statementCoverageCount[s] = 1 # covered during a failure or reduction
                    if statementCoverageCount[s] <= sThreshold:
                        activePool.append(t)
                        added = True
                        break


    # for now a stupid fixed last-n is used, since we know higher values are at the end
    if config.useHints:
        activePool.extend(map(lambda x:x[0],hintPool[-config.exploitBestHint:]))
                
    if config.verbose or config.verboseExploit:
        print 'FULL POOL SIZE',len(fullPool)+len(hintPool),'ACTIVE POOL SIZE',len(activePool)
    if (config.verbose or config.verboseExploit) and (len(activePool) < 10) and (len(activePool) > 0):
        print "ACTIVE POOL:"
        for t in activePool:
            print "="*30
            sut.prettyPrintTest(t)
            
def tryExploit():
    global fulltest, currtest
    if R.random() < config.exploit:
        buildActivePool()
        if len(activePool) == 0:
            return
        et = R.choice(activePool)
        if config.verboseExploit or config.verbose:
            print "EXPLOITING STORED TEST ENDING IN",sut.prettyName(et[-1][0])        
        if R.random() < config.Pmutate:
            if config.verboseExploit or config.verbose:
                print "MUTATING EXPLOITED TEST"
            if R.random() < config.Pcrossover:
                et2 = R.choice(activePool)
                if config.verboseExploit or config.verbose:
                    print "CROSSOVER WITH TEST ENDING IN",sut.prettyName(et2[-1][0])                          
                et = sut.crossover(et,et2,R)
            else:
                et = sut.mutate(et,R)
        sut.replay(et)
        if config.total:
            for a in sut.test():
                fulltest.write(a[0] + "\n")
                fulltest.flush()
        if config.replayable:
            currtest.close()
            currtest = open("currtest.test",'w')
            for a in sut.test():
                currtest.write(a[0] + "\n")
                currtest.flush()
            
def collectExploitable():
    global fullPool,activePool,branchCoverageCount,statementCoverageCount,localizeSFail,localizeBFail,reducePool,hintValueCounts

    if config.useHints:
        # We are assuming hints are all normalized to the same scale!
        hval = max(sut.hints())
        if (len(hintValueCounts) == 0) or (hval > max(hintValueCounts.keys())):
            if config.verbose or config.verboseExploit:
                print "COLLECTING DUE TO HIGH HEURISTIC SCORE:",hval            
            hintPool.append((list(sut.test()),hval))
        if hval in hintValueCounts:
            hintValueCounts[hval] += 1
        else:
            hintValueCounts[hval] = 1
    
    if (not config.noCoverageExploit) and ((len(sut.newBranches()) != 0) or (len(sut.newStatements()) != 0)):
        if config.verbose or config.verboseExploit:
            print "COLLECTING DUE TO NEW COVERAGE:",len(sut.newBranches()),len(sut.newStatements())
        if not config.reducePool:
            fullPool.append((list(sut.test()), set(sut.currBranches()), set(sut.currStatements())))
        else:
            # We can't reduce right now, unless we want the annoyance of saving and restoring state, since
            # we are in the middle of a test run, and we'd mess up quick test and coverage stats collection
            if config.verbose or config.verboseExploit:
                print "SAVING TEST FOR REDUCTION"
            reducePool.append((list(sut.test()),set(sut.newBranches()),set(sut.newStatements())))

def printStatus(elapsed,step=None):
    global sut, nops, activePool, fullPool
    print "TEST #"+str(ntests),
    if step != None:
        print "STEP #"+str(step),
    print "("+str(datetime.timedelta(seconds=elapsed))+")",(datetime.datetime.now()).ctime(),
    if not config.noCover:
        print "[",len(sut.allStatements()),"stmts",len(sut.allBranches()),"branches ]",
    if (config.exploit != None) and (config.verbose or config.verboseExploit):
        print "[ POOLS: full",len(fullPool),"active",len(activePool),"]",
    print nops, "TOTAL ACTIONS (" + str(nops/elapsed) + "/s)"
    sys.stdout.flush()
        
def main():
    global failCount,sut,config,reduceTime,quickCount,repeatCount,failures,cloudFailures,R,opTime,checkTime,guardTime,restartTime,nops,ntests,fulltest,currtest
    global failFileCount
    global fullPool,activePool,branchCoverageCount,statementCoverageCount,localizeSFail,localizeBFail,reducePool
    global hintPool, hintValueCounts
    
    parsed_args, parser = parse_args()
    config = make_config(parsed_args, parser)
    print('Random testing using config={}'.format(config))

    R = random.Random(config.seed)

    start = time.time()
    elapsed = time.time()-start

    failCount = 0
    failFileCount = 0
    quickCount = 0
    repeatCount = 0
    failures = []
    cloudFailures = []

    if config.genDepth != None:
        failCloud = {}
        allClouds = {}

    if config.exploit != None:
        fullPool = []
        reducePool = []
        activePool = []

    hintPool = []
    hintValueCounts = {}

    if config.quickAnalysis or (config.exploit != None):
        branchCoverageCount = {}
        statementCoverageCount = {}

    if config.uniqueValuesAnalysis:
        handledValues = {}
        uniquef = open("unique.corpus",'w')
        allUniquePaths = []

    sut = SUT.sut()
    if config.relax:
        sut.relax()

    # MAJOR SPEED GAIN:  IF NOT MEASURING COVERGE, NO NEED TO RECOMPILE, JUST RUN --noCover
    if config.noCover:
        try:
            sut.stopCoverage()
        except:
            pass

    if config.enumerateEnabled:
        try:
            sut.setEnumerateEnabled(True)
        except:
            pass

    if config.noEnumerateEnabled:
        try:
            sut.setEnumerateEnabled(False)
        except:
            pass        
        
    if config.verboseActions:
        sut.verbose(True)
        
    if config.readQuick:
        print "REPLAYING QUICK TESTS"
        sqrtime = time.time()
        for f in glob.glob("quick*.test"):
            fn = int(f.split("quick")[1].split(".")[0])
            if fn >= quickCount:
                quickCount = fn + 1
            t = sut.loadTest(f)
            sut.replay(t,catchUncaught=True,checkProp=(not config.noCheck))
            # quick tests are obviously good sources for exploitation
            if (config.exploit != None) and (not config.noCoverageExploit):
                for b in sut.currBranches():
                    if b not in branchCoverageCount:
                        branchCoverageCount[b] = 1
                    else:
                        branchCoverageCount[b] += 1
                for s in sut.currStatements():
                    if s not in statementCoverageCount:
                        statementCoverageCount[s] = 1
                    else:
                        statementCoverageCount[s] += 1      
                fullPool.append((t,set(sut.currBranches()), set(sut.currStatements())))
                
        print "EXECUTION TIME:",time.time()-sqrtime
        print "BRANCH COVERAGE:",len(sut.allBranches())
        print "STATEMENT COVERAGE:",len(sut.allStatements())        
                            
    if config.logging != None:
        sut.setLog(config.logging)

    if config.profile:
        profileTime = {}
        profileCount = {}
        for a in set(map(sut.actionClass, sut.actions())):
            profileTime[a] = 0.0
            profileCount[a] = 0
        
    if config.markov != None:
        nactions = len(sut.actions())
        mprobs = {}
        prefix = []
        probs = []
        inProbs = False
        readSize = False
        for l in open(config.markov):
            if not readSize:
                markovN = int(l)
                readSize = True
            elif "START CLASS" in l:
                if (prefix != []):
                    mprobs[tuple(prefix)] = probs
                prefix = []
                probs = []
                inProbs = False
            elif inProbs:
                ls = l.split("%%%%")
                prob = float(ls[0])
                ac = ls[1][1:-1]
                probs.append((prob,ac))
            elif "END CLASS" in l:
                inProbs = True
            else:
                prefix.append(l[:-1])        
        
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
        fulltest = open("fulltest.test",'w')

    if config.localize:
        localizeSFail = {}
        localizeSPass = {}        
        localizeBFail = {}
        localizeBPass = {}
        testsPassed = 0

    if config.computeFeatureStats:
        featureStatsB = {}                
        featureStatsS = {}
        featureStatsA = {}

    if config.swarmProbs != None:
        swarmClassProbs = sut.readProbFile(config.swarmProbs)
    else:
        swarmClassProbs = None

    if config.probs != None:
        classP = sut.readProbFile(config.probs,returnList=True)

    if config.LOCProbs:
        classP = sut.codeLOCProbs(baseline=config.LOCBaseline)
        
    if config.quickAnalysis:
        quickcf = open("quick.corpus",'w')
        quickCorpus = []
        quickDoneB = {}
        quickDoneS = {}        
        quickAnalysisTotal = 0
        quickAnalysisBCounts = {}
        quickAnalysisSCounts = {}            
        quickAnalysisCounts = {}
        quickClassCounts = {}
        quickAnalysisRawCounts = {}
        for c in set(map(sut.actionClass,sut.actions())):
            quickAnalysisCounts[c] = 0
            quickClassCounts[c] = 0
            quickAnalysisRawCounts[c] = 0
        quickAnalysisReducedB = {}
        quickAnalysisReducedS = {}

    if config.timedProgress:
        lastInterval = 0
        
    if config.verbose:
        print "ABOUT TO START TESTING"
        sys.stdout.flush()
        
    while (config.maxTests == -1) or (ntests < config.maxTests):
        if config.verbose:
            print "STARTING TEST",ntests
            sys.stdout.flush()
        ntests += 1

        if config.swarm:
            sut.standardSwarm(R,classProb=swarmClassProbs,P=config.swarmP, noDependencies=config.noSwarmDependencies)
            if config.progress:
                print "CONFIG:",(sut.swarmConfig())

        if config.highLowSwarm != None:
            classP = sut.highLowSwarm(R,file=config.swarmProbs,highProb=config.highLowSwarm)

        if config.swarmSwitch != None:
            lastSwitch = 0
            switches = []
            for i in xrange(0,config.swarmSwitch):
                switch = R.randrange(lastSwitch+1,config.depth-((config.swarmSwitch-i)))
                switches.append(switch)
                lastSwitch = switch
            
        startRestart = time.time()
        sut.restart()
        restartTime += time.time() - startRestart

        if config.total:
            fulltest.write("<<RESTART>>\n")
        
        if config.replayable:
            currtest = open("currtest.test",'w')

        if (config.exploit != None) and ((time.time() - start) > config.startExploit):
            tryExploit()

        testFailed = False
            
        for s in xrange(0,config.depth):
            if config.verbose:
                print "GENERATING STEP",s,
                sys.stdout.flush()
            if (config.swarmSwitch != None) and (s in switches):
                if config.highLowSwarm == None:
                    sut.standardSwarm(R,file=config.swarmProbs,P=config.swarmP, noDependencies=config.noSwarmDependencies)
                    if config.progress:
                        print "NEW CONFIG:",(sut.swarmConfig())                    
                else:
                    classP = sut.highLowSwarm(R,file=config.swarmProbs,highProb=config.highLowSwarm)

            if (config.swarmLength != None) and (((s + 1) % config.swarmLength) == 0):
                if config.highLowSwarm == None:
                    sut.standardSwarm(R,file=config.swarmProbs,P=config.swarmP, noDependencies=config.noSwarmDependencies)
                    if config.progress:
                        print "NEW CONFIG:",(sut.swarmConfig())                    
                else:
                    classP = sut.highLowSwarm(R,file=config.swarmProbs,highProb=config.highLowSwarm)                
                
            startGuard = time.time()
            tryStutter = (a != None) and (a[1]()) and ((config.stutter != None) or config.greedyStutter)

            if tryStutter:
                if (config.stutter == None) or (R.random() > config.stutter):
                    tryStutter = False
                if (config.greedyStutter) and sawNew:
                        print "TRYING TO STUTTER DUE TO COVERAGE GAIN"
                        tryStutter = True
            else:
                if config.markov == None:
                    if (config.highLowSwarm == None) and (config.probs == None) and (not config.LOCProbs):
                        a = sut.randomEnabled(R)
                    else:
                        a = sut.randomEnabledClassProbs(R,classP)
                else:
                    prefix = tuple(map(sut.actionClass,sut.test()[-markovN:]))
                    if prefix not in mprobs:
                        a = sut.randomEnabled(R)
                    else:
                        a = sut.randomEnabledClassProbs(R,mprobs[prefix])
                        if a == None:
                            a = sut.randomEnabled(R)
                        
            if a == None:
                #sut.prettyPrintTest(sut.test())
                print "WARNING: DEADLOCK (NO ENABLED ACTIONS)"
                
            guardTime += time.time()-startGuard
            elapsed = time.time() - start
            if elapsed > config.timeout:
                print "STOPPING TEST DUE TO TIMEOUT, TERMINATED AT LENGTH",len(sut.test())
                break
            if config.timedProgress != -1:
                thisInterval = int(elapsed / config.timedProgress)
                if thisInterval > lastInterval:
                    printStatus(elapsed,step=s)
                    lastInterval = thisInterval
                    sys.stdout.flush()
            if a == None:
                print "TERMINATING TEST DUE TO NO ENABLED ACTIONS"
                break                
            if tryStutter:
                print "STUTTERING WITH",a[0]
            if config.replayable:
                currtest.write(a[0] + "\n")
                currtest.flush()

            if config.total:
                fulltest.write(a[0] + "\n")
                fulltest.flush()            

            if config.verbose:
                print "ACTION:",sut.prettyName(a[0])
                sys.stdout.flush()
            startOp = time.time()
            if config.quickAnalysis:
                quickClassCounts[sut.actionClass(a)] += 1
            if config.showActions:
                print "STEP #"+str(s),sut.prettyName(a[0])
            stepOk = sut.safely(a)
            thisOpTime = time.time()-startOp
            nops += 1
            if config.profile:
                profileTime[sut.actionClass(a)] += thisOpTime
                profileCount[sut.actionClass(a)] += 1
            opTime += thisOpTime
            if sut.warning() != None:
                print "SUT WARNING:",sut.warning()            
            if tryStutter:
                print "DONE STUTTERING"
            if (stepOk or config.uncaught) and config.noCheck and (config.exploit != None):
                collectExploitable()                
            if (not config.uncaught) and (not stepOk):
                testFailed = True
                handle_failure(sut.test(), "UNCAUGHT EXCEPTION", False)
                if not config.multiple:
                    print "STOPPING TESTING DUE TO FAILED TEST"
                break
            
            startCheck = time.time()
            if not config.noCheck:
                checkResult = sut.check()
                checkTime += time.time()-startCheck
                if checkResult and (stepOk or config.uncaught) and (config.exploit != None):
                    collectExploitable()
                    
            if not checkResult:
                testFailed = True
                handle_failure(sut.test(), "PROPERLY VIOLATION", True)
                if not config.multiple:
                    print "STOPPING TESTING DUE TO FAILED TEST"
                break
            
            elapsed = time.time() - start
            if config.running:
                if sut.newBranches() != set([]):
                    print "ACTION:",sut.prettyName(a[0])
                    for b in sut.newBranches():
                        print elapsed,len(sut.allBranches()),"New branch",b
                        sys.stdout.flush()
                    sawNew = True
                else:
                    sawNew = False
                if sut.newStatements() != set([]):
                    print "ACTION:",sut.prettyName(a[0])
                    for s in sut.newStatements():
                        print elapsed,len(sut.allStatements()),"New statement",s
                        sys.stdout.flush()
                    sawNew = True
                else:
                    sawNew = False                

            if config.uniqueValuesAnalysis:
                uvals = sut.uniqueVals()
                olds = sut.state()
                currTest = list(sut.test())
                for u in uvals:
                    if u not in handledValues:
                        print "ANALYZING NEW UNIQUE VALUE:",u
                    else:
                        continue
                    r = sut.reduce(currTest, sut.coversUnique(u), keepLast=False)
                    rc = map(sut.actionClass, r)
                    sut.replay(r)
                    for ru in sut.uniqueVals():
                        handledValues[ru] = True
                    if rc not in allUniquePaths:
                        print "NEW PATH DISCOVERED"
                        allUniquePaths.append(rc)
                        for s in rc:
                            uniquef.write(s+"\n")
                        uniquef.write(("="*50)+"\n")
                        uniquef.flush()
                sut.backtrack(olds)

            if (config.stopWhenBranches != None):
                if len(sut.allBranches()) >= config.stopWhenBranches:
                    print "STOPPING TEST DUE TO REACHING BRANCH COVERAGE TARGET, TERMINATED AT LENGTH",len(sut.test()),"TIME",time.time()-start
                    break
            if config.stopWhenStatements != None:
                if len(sut.allStatements()) >= config.stopWhenStatements:
                    print "STOPPING TEST DUE TO REACHING STATEMENT COVERAGE TARGET, TERMINATED AT LENGTH",len(sut.test()),"TIME",time.time()-start
                    break                            
                                        
            if elapsed > config.timeout:
                print "STOPPING TEST DUE TO TIMEOUT, TERMINATED AT LENGTH",len(sut.test())
                break

        if (config.computeFeatureStats):
            for act in sut.swarmConfig():
                if act in featureStatsA:
                    featureStatsA[act] += 1
                else:
                    featureStatsA[act] = 1
            for b in sut.currBranches():
                if b not in featureStatsB:
                    featureStatsB[b] = [1,{}]
                else:
                    featureStatsB[b][0] += 1
                for act in sut.swarmConfig():
                    if act not in featureStatsB[b][1]:
                        featureStatsB[b][1][act] = 1
                    else:
                        featureStatsB[b][1][act] += 1
            for s in sut.currStatements():
                if s not in featureStatsS:
                    featureStatsS[s] = [1,{}]
                else:
                    featureStatsS[s][0] += 1
                for act in sut.swarmConfig():
                    if act not in featureStatsS[s][1]:
                        featureStatsS[s][1][act] = 1
                    else:
                        featureStatsS[s][1][act] += 1
            
        if (config.exploit != None) and (not config.quickAnalysis):
            for b in sut.currBranches():
                if b not in branchCoverageCount:
                    branchCoverageCount[b] = 1
                else:
                    branchCoverageCount[b] += 1
            for s in sut.currStatements():
                if s not in statementCoverageCount:
                    statementCoverageCount[s] = 1
                else:
                    statementCoverageCount[s] += 1                    

        if config.localize and not testFailed:
            testsPassed += 1
            for s in sut.currStatements():
                if s not in localizeSPass:
                    localizeSPass[s] = 0
                localizeSPass[s] += 1
            for b in sut.currBranches():
                if b not in localizeBPass:
                    localizeBPass[b] = 0
                localizeBPass[b] += 1                            
                    
        if config.quickAnalysis:
            currTest = list(sut.test())
            sut.replay(currTest)
            currB = sut.currBranches()
            currS = sut.currStatements()
            clen = len(currTest)
            #print "GATHERING QUICK ANALYSIS DATA FOR",len(currB),"BRANCHES"
            for b in currB:
                if config.fastQuickAnalysis and (b in quickDoneB):
                    continue
                print "ANALYZING BRANCH",b
                if b not in branchCoverageCount:
                    branchCoverageCount[b] = 0
                    quickAnalysisReducedB[b] = 0                    
                branchCoverageCount[b] += 1
                r = sut.reduce(currTest,sut.coversBranches([b]),keepLast=False)
                print "REDUCED FROM",clen,"TO",len(r)
                sys.stdout.flush()
                sut.replay(r)
                for br in sut.currBranches():
                    quickDoneB[br] = True
                for sr in sut.currStatements():
                    quickDoneS[sr] = True                    
                rc = map(sut.actionClass,r)
                if rc not in quickCorpus:
                    quickCorpus.append(rc)
                    for s in rc:
                        quickcf.write(s+"\n")
                    quickcf.write(("="*50)+"\n")
                    quickcf.flush()
                sut.replay(r)
                for b2 in sut.currBranches():
                    if b2 not in quickAnalysisReducedB:
                        quickAnalysisReducedB[b2] = 0
                    quickAnalysisReducedB[b2] += 1
                for s2 in sut.currStatements():
                    if s2 not in quickAnalysisReducedS:
                        quickAnalysisReducedS[s2] = 0
                    quickAnalysisReducedS[s2] += 1
                if b not in quickAnalysisBCounts:
                    quickAnalysisBCounts[b] = {}
                quickAnalysisTotal += 1
                for c in map(sut.actionClass,r):
                    quickAnalysisRawCounts[c] += 1
                for c in set(map(sut.actionClass,r)):
                    quickAnalysisCounts[c] += 1
                    if c not in quickAnalysisBCounts[b]:
                        quickAnalysisBCounts[b][c] = 0
                    quickAnalysisBCounts[b][c] += 1
                #print "GATHERING QUICK ANALYSIS DATA FOR",len(currS),"STATEMENTS"                    
            for s in currS:
                if config.fastQuickAnalysis and (s in quickDoneS):
                    continue
                if s not in statementCoverageCount:
                    statementCoverageCount[s] = 0
                    quickAnalysisReducedS[s] = 0
                statementCoverageCount[s] += 1                
                print "ANALYZING STATEMENT",s
                r = sut.reduce(currTest,sut.coversStatements([s]),keepLast=False)
                print "REDUCED FROM",clen,"TO",len(r)
                sys.stdout.flush()
                sut.replay(r)
                for br in sut.currBranches():
                    quickDoneB[br] = True
                for sr in sut.currStatements():
                    quickDoneS[sr] = True                                
                rc = map(sut.actionClass,r)
                if rc not in quickCorpus:
                    quickCorpus.append(rc)                
                sut.replay(r)
                for b2 in sut.currBranches():
                    if b2 not in quickAnalysisReducedB:
                        quickAnalysisReducedB[b2] = 0
                    quickAnalysisReducedB[b2] += 1
                for s2 in sut.currStatements():
                    quickAnalysisReducedS[s2] += 1                
                if s not in quickAnalysisSCounts:
                    quickAnalysisSCounts[s] = {}
                quickAnalysisTotal += 1
                for c in map(sut.actionClass,r):
                    quickAnalysisRawCounts[c] += 1                
                for c in set(map(sut.actionClass,r)):
                    quickAnalysisCounts[c] += 1
                    if c not in quickAnalysisSCounts[s]:
                        quickAnalysisSCounts[s][c] = 0
                    quickAnalysisSCounts[s][c] += 1                    

        if config.throughput:
            print "THROUGHPUT:",nops/(time.time()-start),"ACTIONS/SECOND"
        if config.replayable:
            currtest.close()
        if config.quickTests:
            if (sut.newCurrBranches() != set([])) or (sut.newCurrStatements() != set([])):
                handle_failure(sut.test(), "NEW COVERAGE", False, newCov=True)
        if config.progress:
            printStatus(elapsed)                
        if (not config.multiple) and (failCount > 0):
            break
        if (config.stopWhenBranches != None):
            if len(sut.allBranches()) >= config.stopWhenBranches:
                print "STOPPING TESTING DUE TO REACHING BRANCH COVERAGE TARGET"
                break
        if config.stopWhenStatements != None:
            if len(sut.allStatements()) >= config.stopWhenStatements:
                print "STOPPING TESTING DUE TO REACHING STATEMENT COVERAGE TARGET"
                break                               
        if elapsed > config.timeout:
            print "STOPPING TESTING DUE TO TIMEOUT"
            break        

    if config.total:
        fulltest.close()
        
    if not config.noCover:
        sut.restart()
        print sut.report(config.coverFile),"PERCENT COVERED"

        if config.internal:
            sut.internalReport()
        
        if config.html:
            sut.htmlReport(config.html)

    if config.uniqueValuesAnalysis:
        uniquef.close()

    if config.computeFeatureStats:
        fstatsf = open ("feature.stats."+str(os.getpid())+str(R.randrange(1000,10000)),'w')
        fstatsf.write("TESTS:"+str(ntests)+"\n")
        for act in featureStatsA:
            fstatsf.write(act + " %%ACTCOUNT%% " + str(featureStatsA[act]) + "\n")
        for b in sut.allBranches():
            fstatsf.write("BRANCH:" + str(b) + "\n")
            count = featureStatsB[b][0]
            fstatsf.write("COUNT:" + str(count) + "\n")
            for act in featureStatsB[b][1]:
                fstatsf.write(act + " %%%% " + str(featureStatsB[b][1][act]) + "\n")
        for s in sut.allStatements():
            fstatsf.write("STATEMENT:" + str(s) + "\n")
            count = featureStatsS[s][0]
            fstatsf.write("COUNT:" + str(count) + "\n")
            for act in featureStatsS[s][1]:
                fstatsf.write(act + " %%%% " + str(featureStatsS[s][1][act]) + "\n")
        fstatsf.close()
        
    if config.quickAnalysis:
        quickcf.close()
        print "*" * 70        
        print "QUICK ANALYSIS RESULTS:"
        print "*" * 70
        print "TEST PATTERNS:"
        for rc in quickCorpus:
            print "="*50
            for s in rc:
                print s
        print "*" * 70
        print "OVERALL ACTION ANALYSIS:"
        totalTaken = sum(quickClassCounts.values())
        actSort = sorted(quickAnalysisRawCounts.keys(),key=lambda x: quickAnalysisCounts.get(x,0), reverse=True)
        for a in actSort:
            print "="*50
            print "ACTION CLASS:"
            print a
            print "APPEARS",quickClassCounts[a],"TIMES IN TESTS"
            print "APPEARS",quickAnalysisRawCounts[a],"TIMES IN REDUCED TESTS"
            print "APPEARS IN",quickAnalysisCounts[a],"REDUCED TESTS ("+str(round((quickAnalysisCounts[a]/(quickAnalysisTotal*1.0))*100,2)) + "%)"
            #baselineRate = quickClassCounts[a]/(totalTaken*1.0)
            #reducedRate = quickAnalysisRawCounts[a]/(quickAnalysisTotal*1.0)
            #if reducedRate > 0.0:
            #    print "RATIO:",(baselineRate/reducedRate)
            #else:
            #    print "RATIO: INFINITE"            

        print "*" * 70            
        print "DETAILED BRANCH ANALYSIS"
        branchCoverageCountSort = sorted(branchCoverageCount.keys(), key = lambda x: branchCoverageCount[x])
        for b in branchCoverageCountSort:
            print "="*50
            print "BRANCH:",b
            baselineRate = branchCoverageCount[b]/(ntests*1.0)
            print "IN",str(round(baselineRate*100,2))+"% OF TESTS ("+str(branchCoverageCount[b])+" TESTS)"
            reducedRate = quickAnalysisReducedB[b]/(quickAnalysisTotal*1.0)
            print "IN",str(round(reducedRate*100,2))+"% OF REDUCED TESTS"
            if reducedRate > 0.0:
                print "RATIO:",(baselineRate/reducedRate)
            print "REDUCED TEST ACTION ANALYSIS:"
            sortAs = sorted(quickAnalysisBCounts[b].keys(),key=lambda x: quickAnalysisBCounts[b][x],reverse=True)            
            print branchCoverageCount[b],"TESTS"
            for a in sortAs:
                print a,str(round(quickAnalysisBCounts[b][a]/(branchCoverageCount[b]*1.0)*100,2))+"%"                                           
        print "*" * 70
        print "DETAILED STATEMENT ANALYSIS"
        statementCoverageCountSort = sorted(statementCoverageCount.keys(), key = lambda x: statementCoverageCount[x])        
        for s in statementCoverageCountSort:
            print "="*50            
            print "STATEMENT:",s
            baselineRate = statementCoverageCount[s]/(ntests*1.0)
            print "IN",str(round(baselineRate*100,2))+"% OF TESTS"
            reducedRate = quickAnalysisReducedS[s]/(quickAnalysisTotal*1.0)
            print "IN",str(round(reducedRate*100,2))+"% OF REDUCED TESTS"
            if reducedRate > 0.0:
                print "RATIO:",(baselineRate/reducedRate)
            print "REDUCED TEST ACTION ANALYSIS:"
            print statementCoverageCount[s],"TESTS"            
            sortAs = sorted(quickAnalysisSCounts[s].keys(),key=lambda x: quickAnalysisSCounts[s][x],reverse=True)
            for a in sortAs:
                print a,str(round(quickAnalysisSCounts[s][a]/(statementCoverageCount[s]*1.0)*100,2))+"%"                           
            
    print time.time()-start, "TOTAL RUNTIME"
    print ntests, "EXECUTED"
    print nops, "TOTAL TEST OPERATIONS"
    print opTime, "TIME SPENT EXECUTING TEST OPERATIONS"
    print guardTime, "TIME SPENT EVALUATING GUARDS AND CHOOSING ACTIONS"
    if not config.noCheck:
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
                traceback.print_tb(err[2],file=sys.stdout)
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

    if config.profile:
        print "ACTION PROFILE:"
        for a in sut.actionClasses():
            if profileCount[a] == 0:
                print "** ACTION CLASS ",a,"NEVER EXECUTED! **"
        
        print "<ACTION> <COUNT> <AVERAGE RUNTIME> <NORMALIZED BY MAX> <NORMALIZED BY MIN> [<TOTAL PERCENT RUNTIME>]"
        averages = []
        for a in profileTime:
            if profileCount[a] != 0:
                averages.append((a,profileTime[a]/profileCount[a]))
        averages = sorted(averages, key = lambda x: x[1])
        maxAvg = averages[-1][1]
        minAvg = averages[0][1]
        sumAvg = sum(map(lambda x: x[1], averages))
        for (a,t) in averages:
            print a,profileCount[a],t,round(t/maxAvg,2),round(t/minAvg,2),str(round((t*100.0)/sumAvg,2))+"%"
                                
    if config.localize and failCount > 0:
        scoresS = {}
        scoresB = {}
        for s in sut.allStatements():
            if s not in localizeSPass:
                localizeSPass[s] = 0
            if s not in localizeSFail:
                localizeSFail[s] = 0
            denom = math.sqrt(failCount*(localizeSFail[s]+localizeSPass[s]))
            if denom == 0.0:
                continue
            scoresS[s] = localizeSFail[s]/denom
        for b in sut.allBranches():
            if b not in localizeBPass:
                localizeBPass[b] = 0
            if b not in localizeBFail:
                localizeBFail[b] = 0
            denom = math.sqrt(failCount*(localizeBFail[b]+localizeBPass[b]))
            if denom == 0.0:
                continue            
            scoresB[b] = localizeBFail[b]/denom
        sortedS = sorted(scoresS.keys(),key = lambda x:scoresS[x])
        sortedB = sorted(scoresB.keys(),key = lambda x:scoresB[x])
        print "FAULT LOCALIZATION RESULTS:"
        for s in sortedS:
            if scoresS[s] > 0.0:
                print s, scoresS[s]
        for b in sortedB:
            if scoresB[b] > 0.0:
                print b, scoresB[b]            
            
    if not config.noCover:
        print len(sut.allBranches()),"BRANCHES COVERED"
        print len(sut.allStatements()),"STATEMENTS COVERED"

    if failCount == 0:
        sys.exit(0)
    else:
        sys.exit(255)

if __name__ == '__main__':
    main()

    
