from __future__ import print_function

import sys
import time
import traceback
import argparse
import os
import subprocess
import random
from collections import namedtuple

# Appending current working directory to sys.path
# So that user can run randomtester from the directory where sut.py is located
current_working_dir = os.getcwd()
sys.path.append(current_working_dir)

if "--help" not in sys.argv:
    import sut as SUT


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('infile', metavar='filename', type=str, default=None,
                        help='Path to the test to be reduced.')
    parser.add_argument('outfile', metavar='filename', type=str, default=None,
                        help='Path to the test to be reduced.')
    parser.add_argument('--noCheck', action='store_true',
                        help='Do not check properties.')
    parser.add_argument('--noReduce', action='store_true',
                        help="Do not reduce the test.")
    parser.add_argument('--noNormalize', action='store_true',
                        help="Do not normalize/simplify test.")
    parser.add_argument('--noAlpha', action='store_true',
                        help="Do not alpha convert test.")
    parser.add_argument(
        '--matchException',
        action='store_true',
        help='Force test to fail with same exception as original (does not work for sandboxes).')
    parser.add_argument(
        '--coverage',
        action='store_true',
        help='Reduce with respect to maintaining code coverage, not failure.')
    parser.add_argument(
        '--coverMore',
        action='store_true',
        help='Only allow reductions that increase code coverage.')
    parser.add_argument(
        '--checkDeterminism',
        action='store_true',
        help='Reduce with respect to test being deterministic (final state).')
    parser.add_argument(
        '--checkStepDeterminism',
        action='store_true',
        help='Reduce with respect to test being deterministic (visible value).')
    parser.add_argument('--determinismDelay', type=float, default=1.0,
                        help='Time delay for nondeterminism check.')
    parser.add_argument(
        '--determinismDelay0',
        type=float,
        default=None,
        help='Time delay for INITIAL run in nondeterminism check.')
    parser.add_argument(
        '--determinismTries',
        type=int,
        default=1,
        help='Number of times to check for nondeterministic behavior.')
    parser.add_argument(
        '--checkProcessDeterminism',
        action='store_true',
        help='Reduce with respect to test being process deterministic.')
    parser.add_argument(
        '--iterate',
        action='store_true',
        help='Use iterative approach to check process determinism.')
    parser.add_argument('--probability', type=float, default=None,
                        help='Ensure predicate fails with this probability.')
    parser.add_argument(
        '--samples',
        type=int,
        default=10,
        help='Use this many samples to check probability (default 10).')
    parser.add_argument(
        '--replications',
        type=int,
        default=1,
        help='Use this many replications to check probability (default 1).')
    parser.add_argument(
        '-k',
        '--keepLast',
        action='store_true',
        help="Keep last action the same when reducing/normalizing: slippage avoidance heuristic.")
    parser.add_argument(
        '--noPruneGuards',
        action='store_true',
        help="Do not prune based on guards (useful in determinism checks)")
    parser.add_argument(
        '--uncaught',
        action='store_true',
        help='Allow uncaught exceptions in actions (for coverage-based reduction).')
    parser.add_argument(
        '--ddmin',
        action='store_true',
        help="Use standard binary-search-like delta-debugging, not greedy one-step method.")
    parser.add_argument(
        '--decompose',
        action='store_true',
        help="Perform decomposition by coverage (assumes coverage based reduction).  Produces multiple tests.")
    parser.add_argument('-M', '--multiple', action='store_true',
                        help="Produce multiple reductions.")
    parser.add_argument(
        '--recursive',
        type=int,
        default=1,
        help='How many recursive levels of comb-block to apply (default 1).')
    parser.add_argument(
        '--limit',
        type=int,
        default=None,
        help='Limit on combinations generated in comb-block (default None).')
    parser.add_argument('--random', action='store_true',
                        help="Randomize order of reductions.")
    parser.add_argument('--seed', type=int, default=None,
                        help='Random seed (default = None).')
    parser.add_argument('--verbose', type=str, default=None,
                        help='Level of verbosity for reduction.')
    parser.add_argument('--sandbox', action='store_true',
                        help="Use sandbox reduction.")
    parser.add_argument('--quietSandbox', action='store_true',
                        help="Run sandbox in a quieter mode.")
    parser.add_argument(
        '--timeout',
        type=int,
        default=None,
        help='Timeout for sandbox reductions (only works on unix-like systems).')
    parser.add_argument('--afl', action='store_true',
                        help="Read in tests in afl format.")
    parser.add_argument('--aflswarm', action='store_true',
                        help="afl tests are in swarm format.")
    parser.add_argument('--writeafl', action='store_true',
                        help="Write out tests in afl format.")

    parsed_args = parser.parse_args(sys.argv[1:])
    return (parsed_args, parser)


def make_config(pargs, parser):
    """
    Process the raw arguments, returning a namedtuple object holding the
    entire configuration, if everything parses correctly.
    """
    pdict = pargs.__dict__
    # create a namedtuple object for fast attribute lookup
    key_list = list(pdict.keys())
    arg_list = [pdict[k] for k in key_list]
    Config = namedtuple('Config', key_list)
    nt_config = Config(*arg_list)
    return nt_config


def sandboxReplay(test):
    global timeout
    if "--quietSandbox" not in sys.argv:
        print("ATTEMPTING SANDBOX REPLAY WITH", len(test), "STEPS")
    tmpName = "tmptest." + str(os.getpid()) + ".test"
    tmptest = open(tmpName, 'w')
    for s in test:
        tmptest.write(s[0] + "\n")
    tmptest.close()
    cmd = "tstl_replay " + tmpName
    if "--noCheck" in sys.argv:
        cmd += " --noCheck"
    if timeout is not None:
        cmd = "ulimit -t " + timeout + "; " + cmd
    start = time.time()
    subprocess.call([cmd], shell=True)
    if "--quietSandbox" not in sys.argv:
        print("ELAPSED:", time.time() - start)
    for l in open("replay.out"):
        if "TEST REPLAYED SUCCESSFULLY" in l:
            if "--quietSandbox" not in sys.argv:
                print("TEST SUCCEEDS")
            return False
    if "--quietSandbox" not in sys.argv:
        print("TEST FAILS")
    print("SANDBOX RUN FAILS: TEST LENGTH NOW", len(test))
    bestreduce = open("lastreduction." + str(os.getpid()) + ".test", 'w')
    for l in open(tmpName):
        bestreduce.write(l)
    bestreduce.close()
    return True


def main():

    global timeout

    parsed_args, parser = parse_args()
    config = make_config(parsed_args, parser)
    print(('Reducing using config={}'.format(config)))

    sut = SUT.sut()

    timeout = config.timeout

    if not ((config.coverage) or (config.coverMore) or (config.decompose)):
        try:
            sut.stopCoverage()
        except BaseException:
            pass

    R = None
    if config.random:
        R = random.Random()

        if config.seed is not None:
            R.seed(config.seed)

    r = sut.loadTest(config.infile, afl=config.afl, swarm=config.aflswarm)

    f = None

    if config.matchException:
        print("EXECUTING TEST TO OBTAIN FAILURE FOR EXCEPTION MATCHING...")
        assert sut.fails(r)
        f = sut.failure()
        print("ERROR:", f)
        print("TRACEBACK:")
        traceback.print_tb(f[2], file=sys.stdout)

    if not config.sandbox:
        pred = (lambda x: sut.failsCheck(x, failure=f))
        if config.noCheck:
            pred = (lambda x: sut.fails(x, failure=f))
    else:
        pred = sandboxReplay

    if config.coverage or config.coverMore or (
            config.decompose and not config.noNormalize):
        print("EXECUTING TEST TO OBTAIN COVERAGE FOR CAUSE REDUCTION...")
        sut.replay(r, checkProp=not config.noCheck,
                   catchUncaught=config.uncaught)
        b = set(sut.currBranches())
        s = set(sut.currStatements())
        print("PRESERVING", len(b), "BRANCHES AND", len(s), "STATEMENTS")
        if config.coverMore:
            pred = sut.coversMore(
                s,
                b,
                checkProp=not config.noCheck,
                catchUncaught=config.uncaught)
        else:
            pred = sut.coversAll(
                s,
                b,
                checkProp=not config.noCheck,
                catchUncaught=config.uncaught)

    if config.checkDeterminism:
        pred = (
            lambda t: sut.nondeterministic(
                t,
                delay=config.determinismDelay,
                tries=config.determinismTries,
                delay0=config.determinismDelay0))

    if config.checkStepDeterminism:
        pred = (
            lambda t: sut.stepNondeterministic(
                t,
                delay=config.determinismDelay,
                tries=config.determinismTries,
                delay0=config.determinismDelay0))

    if config.checkProcessDeterminism:
        pred = (
            lambda t: sut.processNondeterministic(
                t,
                delay=config.determinismDelay,
                tries=config.determinismTries,
                iterate=config.iterate))

    if config.probability is not None:
        Ppred = pred
        pred = (
            lambda t: sut.forceP(
                t,
                Ppred,
                P=config.probability,
                samples=config.samples,
                replications=config.replications))

    print("STARTING WITH TEST OF LENGTH", len(r))
    if not config.noReduce:
        start = time.time()
        print("REDUCING...")
        if (not config.multiple) and (not config.decompose):
            r = sut.reduce(
                r,
                pred,
                verbose=config.verbose,
                tryFast=not config.ddmin,
                keepLast=config.keepLast,
                pruneGuards=not config.noPruneGuards,
                rgen=R)
        elif config.multiple:
            rs = sut.reductions(
                r,
                pred,
                verbose=config.verbose,
                recursive=config.recursive,
                limit=config.limit,
                keepLast=config.keepLast,
                pruneGuards=not config.noPruneGuards,
                tryFast=not config.ddmin)
        elif config.decompose:
            print("DECOMPOSING...")
            rs = sut.coverDecompose(
                r,
                verbose=config.verbose,
                checkProp=not config.noCheck,
                catchUncaught=config.uncaught)
        print("REDUCED IN", time.time() - start, "SECONDS")
        if (not config.multiple) and (not config.decompose):
            print("NEW LENGTH", len(r))
        else:
            print("NEW LENGTHS", list(map(len, rs)))
    if not config.noAlpha:
        print("ALPHA CONVERTING...")
        if (not config.multiple) and (not config.decompose):
            r = sut.alphaConvert(r)
        else:
            rs = list(map(sut.alphaConvert, rs))
    if not config.noNormalize:
        start = time.time()
        print("NORMALIZING...")
        if (not config.multiple) and (not config.decompose):
            r = sut.normalize(
                r,
                pred,
                verbose=config.verbose,
                keepLast=config.keepLast,
                pruneGuards=not config.noPruneGuards,
                tryFast=not config.ddmin)
        else:
            newrs = []
            for r in rs:
                f = None

                if config.matchException:
                    print("EXECUTING TEST TO OBTAIN FAILURE FOR EXCEPTION MATCHING...")
                    assert sut.fails(r)
                    f = sut.failure()
                    print("ERROR:", f)
                    print("TRACEBACK:")
                    traceback.print_tb(f[2], file=sys.stdout)

                if not config.sandbox:
                    pred = (lambda x: sut.failsCheck(x, failure=f))
                    if not config.noCheck:
                        pred = (lambda x: sut.fails(x, failure=f))
                else:
                    pred = sandboxReplay

                if config.coverage or config.coverMore or (
                        config.decompose and not config.noNormalize):
                    print("EXECUTING TEST TO OBTAIN COVERAGE FOR CAUSE REDUCTION...")
                    sut.replay(r, checkProp=not config.noCheck,
                               catchUncaught=config.uncaught)
                    b = set(sut.currBranches())
                    s = set(sut.currStatements())
                    print("PRESERVING", len(b),
                          "BRANCHES AND", len(s), "STATEMENTS")
                    if config.coverMore:
                        pred = sut.coversMore(
                            s, b, checkProp=not config.noCheck, catchUncaught=config.uncaught)
                    else:
                        pred = sut.coversAll(
                            s, b, checkProp=not config.noCheck, catchUncaught=config.uncaught)

                newrs.append(
                    sut.normalize(
                        r,
                        pred,
                        verbose=config.verbose,
                        keepLast=config.keepLast,
                        pruneGuards=not config.noPruneGuards,
                        tryFast=not config.ddmin))
            rs = newrs
        print("NORMALIZED IN", time.time() - start, "SECONDS")
        if (not config.multiple) and (not config.decompose):
            print("NEW LENGTH", len(r))
        else:
            print("NEW LENGTHS", list(map(len, rs)))
    if (not config.multiple) and (not config.decompose):
        sut.saveTest(r, config.outfile, afl=config.writeafl)
        sut.prettyPrintTest(r)
        print()
        print("TEST WRITTEN TO", config.outfile)
    else:
        i = 0
        for r in rs:
            print("TEST #" + str(i) + ":")
            sut.saveTest(r, config.outfile + "." + str(i) +
                         ".test", afl=config.writeafl)
            sut.prettyPrintTest(r)
            print()
            print("TEST WRITTEN TO", config.outfile + "." + str(i))
            print()
            i += 1
