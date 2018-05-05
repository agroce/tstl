from __future__ import print_function

import sys
import time
import traceback
import argparse
import os
from collections import namedtuple

# Appending current working directory to sys.path
# So that user can run randomtester from the directory where sut.py is located
current_working_dir = os.getcwd()
sys.path.append(current_working_dir)

if "--help" not in sys.argv:
    import sut as SUT


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--depth',
        type=int,
        default=5,
        help='Depth to explore model (default 5).')
    parser.add_argument(
        '--recursive',
        type=int,
        default=0,
        help='How many recursive levels of exploration to try (default 0).')
    parser.add_argument('-n', '--noCover', action='store_true',
                        help="Don't check code coverage.")
    parser.add_argument('-o',
                        '--output',
                        type=str,
                        default="smallcheck." + str(os.getpid()) + ".test",
                        help="Filename to save failing test(s).")
    parser.add_argument('-v',
                        '--verbose',
                        type=str,
                        default=None,
                        help="Verbosity level.")
    parser.add_argument('-M', '--multiple', action='store_true',
                        help="Allow multiple failures.")
    parser.add_argument('--noCheck', action='store_true',
                        help='Do not check properties.')
    parser.add_argument('--reverse', action='store_true',
                        help='Reverse order.')
    parser.add_argument('--visited', action='store_true',
                        help='Keep track of visited states.')
    parser.add_argument('--visitedList', action='store_true',
                        help='Keep track of visited states using list.')

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


def main():

    parsed_args, parser = parse_args()
    config = make_config(parsed_args, parser)
    print(('Running TSTL "smallcheck" using config={}'.format(config)))

    sut = SUT.sut()

    coveringTests = []
    failingTests = None

    if config.multiple:
        failingTests = []

    if config.noCover:
        try:
            sut.stopCoverage()
        except BaseException:
            pass
        coveringTests = None

    visited = None

    if config.visited:
        visited = {}
    if config.visitedList:
        visited = []

    start = time.time()

    r = True

    try:
        r = sut.exploreFromHere(config.depth, checkProp=not config.noCheck,
                                stopFail=not config.multiple,
                                gatherFail=failingTests, gatherCover=coveringTests,
                                verbose=config.verbose, reverse=config.reverse,
                                visited=visited)

        print("FINISHED EXPLORATION TO DEPTH", config.depth,
              "IN", time.time() - start, "SECONDS")

        if not config.noCover and (config.multiple or r):
            recur = config.recursive
            newCovered = list(coveringTests)
            i = 0
            while (recur > 0):
                i += 1
                print("STARTING RECURSIVE EXPLORATION RUN #" + str(i))
                recur -= 1
                newNewCovered = []
                for t in newCovered:
                    print("EXPLORING FROM COVERING TEST:")
                    sut.prettyPrintTest(t)
                    sut.replay(t, catchUncaught=True, checkProp=not config.noCheck)
                    r = sut.exploreFromHere(config.depth, checkProp=not config.noCheck,
                                            stopFail=not config.multiple,
                                            gatherFail=failingTests, gatherCover=newNewCovered,
                                            verbose=config.verbose, reverse=config.reverse,
                                            visited=visited)
                    if not r and not config.multiple:
                        recur = 0
                        break
                coveringTests.extend(newNewCovered)
                newCovered = newNewCovered

    except KeyboardInterrupt:
        print("INTERRUPTED BY USER")

    print("TOTAL RUNTIME FOR SMALLCHECK:", time.time() - start)

    if coveringTests is not None:
        i = 0
        for t in coveringTests:
            fn = config.output.replace(".test", "." + str(i) + ".test")
            if config.verbose:
                print("SAVING COVERING TEST AS", fn)
            i += 1
            sut.saveTest(t, fn)
        print("SAVED", len(coveringTests), "COVERING TESTS WITH PREFIX",
              config.output.replace(".test", ""))

    if not r and not config.multiple:
        print("STOPPING DUE TO FAILED TEST.")
        f = sut.failure()
        print("ERROR:", f)
        print("TRACEBACK:")
        traceback.print_tb(f[2], file=sys.stdout)
        sut.prettyPrintTest(sut.test())
        print("SAVING FAILED TEST AS", "fail." + config.output)
        sut.saveTest(sut.test(), "fail." + config.output)
        sys.exit(255)

    if config.multiple and (len(failingTests) > 0):
        i = 0
        for t in failingTests:
            fn = "fail." + config.output.replace(".test", "." + str(i) + ".test")
            if config.verbose:
                print("SAVING FAILED TEST AS", fn)
            i += 1
            sut.saveTest(t, fn)
        print("SAVED", len(failingTests), "FAILING TESTS WITH PREFIX fail." +
              config.output.replace(".test", ""))
        sys.exit(255)

    sys.exit(0)
