import sut as SUT
import random
import time
import sys
import traceback
import argparse
import os
import SUTDD
from collections import namedtuple

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--depth', type=int, default=100,
                        help='Maximum search depth (100 default).')
    parser.add_argument('-s', '--seed', type=int, default=None,
                        help='Random seed (default = None).')
    parser.add_argument('-m', '--maxtests', type=int, default=-1,
                        help='Maximum #tests to run (-1 = infinite default).')
    parser.add_argument('-p', '--prereduce', action='store_true',
                        help='Pre-reduce.')
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
    
parsed_args, parser = parse_args()
config = make_config(parsed_args, parser)
print('Random testing using config={}'.format(config))

if config.seed != None:
    random.seed(config.seed)

start = time.time()
elapsed = time.time()-start

t = SUT.t()
ntests = 0

tests = []
branches = []

zellerDD = lambda (test, pred): SUTDD.DDreduce(t, test, pred, keepLast = False)
alex = lambda (test, pred): t.reduce(test, pred, keepLast = False)
alexPrune = lambda (test, pred): t.reduce(test, pred, pruneGuards = True, keepLast = False)
reducers = [("Alex", alex, None),
            ("Alex(pruning)", alexPrune, None),
            ("Zeller", zellerDD, None)]

print "GENERATING TESTS..."
while (config.maxtests == -1) or (ntests < config.maxtests):
    ntests += 1
    print "TEST",ntests
    t.restart()
    test = []

    for s in xrange(0,config.depth):
        a = random.choice(t.enabled())
        elapsed = time.time() - start
#        print s, elapsed, a[0]
        sys.stdout.flush()
        test.append(a)
        t.safely(a[2])

    bs = t.currBranches()
    tests.append((test,bs))
    for b in bs:
        if b not in branches:
            branches.append(b)

random.shuffle(branches)
branches = branches[0:15]

print "REDUCING..."
for (name, r, reset) in reducers:
    print "REDUCER",name
    sys.stdout.flush()
    totallen = 0.0
    totalshortlen = 0.0
    totaltests = 0.0
    maxlen = 0
    maxshortlen = 0
    minlen = config.depth+1
    minshortlen = config.depth+1
    start = time.time()
    for b in branches:
        print "BRANCH", b
        totalbranchtests = 0.0
        totalbranchlen = 0.0
        maxbranchlen = 0
        minbranchlen = config.depth+1
        if reset != None:
            reset()
        for (test, tbranches) in tests:
            if b in tbranches:
                def covered():
                    return b in t.currBranches()
                bpred = t.coversBranches([b], catchUncaught=True)
                if not bpred(test):
                    print b
                    print test
                assert bpred(test)
                if config.prereduce:
                    short = t.replayUntil(test, covered, catchUncaught=True)
                    assert bpred(short)
                    totalshortlen += len(short)
                    if len(short) > maxshortlen:
                        maxshortlen = len(short)
                    if len(short) < minshortlen:
                        minshortlen = len(short)
                    red = r((short,bpred))
                else:
                    red = r((test,bpred))
                assert bpred(red)
                if len(red) > maxlen:
                    maxlen = len(red)
                if len(red) < minlen:
                    minlen = len(red)
                totallen += len(red)
                totaltests += 1.0
                if len(red) > maxbranchlen:
                    maxbranchlen = len(red)
                if len(red) < minbranchlen:
                    minbranchlen = len(red)
                totalbranchlen += len(red)
                totalbranchtests += 1.0
                if (totaltests % 100) == 0:
                    elapsed = time.time()-start
                    print elapsed, totaltests, "REDUCED"
                    sys.stdout.flush()
        elapsed = time.time()-start
        print elapsed, "DONE WITH BRANCH: TESTS:", totalbranchtests, "AVG:", totalbranchlen/totalbranchtests, "MIN:", minbranchlen, "MAX:", maxbranchlen
    elapsed = time.time()-start
    print "TIME:",elapsed,"AVG:",totallen/totaltests,"MIN:",minlen,"MAX:",maxlen,"TOTAL:",int(totaltests)
    sys.stdout.flush()
if config.prereduce:
    print "STARTING AVG:", totalshortlen / totaltests, "MIN STARTING:", minshortlen, "MAX STARTING:", maxshortlen

print ntests, "EXECUTED"


