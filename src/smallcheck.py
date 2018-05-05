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
    parser.add_argument('-M', '--multiple', action='store_true',
                        help="Allow multiple failures.")
    parser.add_argument('--noCheck', action='store_true',
                        help='Do not check properties.')

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

    r = sut.exploreFromHere(config.depth, checkProp=not config.noCheck,
                            stopFail=not config.multiple,
                            gatherFail=failingTests, gatherCover=coveringTests, verbose=True)

    if coveringTests is not None:
        i = 0
        for t in coveringTests:
            fn = config.output.replace(".test", "." + str(i) + ".test")
            print("SAVING COVERING TEST AS", fn)
            i += 1
            sut.saveTest(t, fn)
        sys.exit(255)

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

    if config.multiple and (len(gatherFail) > 0):
        i = 0
        for t in gatherFail:
            fn = "fail." + config.output.replace(".test", "." + str(i) + ".test")
            print("SAVING FAILED TEST AS", fn)
            i += 1
            sut.saveTest(t, fn)
        sys.exit(255)
