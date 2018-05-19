from __future__ import print_function

import sys
import traceback
import argparse
import os
import glob
from collections import namedtuple

# Appending current working directory to sys.path
# So that user can run randomtester from the directory where sut.py is located
current_working_dir = os.getcwd()
sys.path.append(current_working_dir)

if "--help" not in sys.argv:
    import sut as SUT


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('testglob', metavar='filename', type=str, default=None,
                        help='Glob for tests to run.')
    parser.add_argument('--noCheck', action='store_true',
                        help='Do not check properties.')
    parser.add_argument('--showTests', action='store_true',
                        help='Show the tests.')
    parser.add_argument('--abstractStrings', action='store_true',
                        help='Abstract away strings in exceptions.')
    parser.add_argument('--ignoreContaining', type=str, default=None,
                        help='Ignore tests with provided string in an action.')
    parser.add_argument('--actionClasses', action='store_true',
                        help='Use set of action classes in test as part of signature.')

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


def noDigits(str):
    return "".join(filter(lambda x: not x.isdigit(), str))


def noStrings(str):
    noStrStr = ""
    inQuote = False
    for c in str:
        if inQuote:
            if c == "'":
                noStrStr += c
                inQuote = False
        else:
            noStrStr += c
            if c == "'":
                inQuote = True
    return noStrStr


def main():

    parsed_args, parser = parse_args()
    config = make_config(parsed_args, parser)
    print(('Triaging using config={}'.format(config)))

    sut = SUT.sut()

    try:
        sut.stopCoverage()
    except BaseException:
        pass

    signatures = {}

    numTests = 0.0
    numInvalid = 0
    numPassing = 0
    for fn in glob.glob(config.testglob):
        try:
            t = sut.loadTest(fn)
        except BaseException:
            print("INVALID TEST CASE:", fn)
            numInvalid += 1
            continue
        if config.ignoreContaining is not None:
            foundString = False
            for s in t:
                if config.ignoreContaining in s[0]:
                    foundString = True
                    break
            if foundString:
                continue
        if not config.noCheck:
            fails = sut.failsAny(t)
        else:
            fails = sut.fails(t)
        if fails:
            numTests += 1
            e = repr(sut.failure())
            e = e[:e.find("<traceback object at 0x")] + ")"
            line = sut.test()[-1][0]
            tline = t[-1][0]
            if line != tline:
                print("TEST", fn, "FAILS BEFORE END OF TEST")
            sig = (noDigits(e), noDigits(line))
            if config.abstractStrings:
                sig = (noStrings(sig[0]), sig[1])
            if config.actionClasses:
                sig += (repr(set(map(sut.actionClass, t))), )
            if (sig not in signatures):
                signatures[sig] = (fn, t, sut.failure(),
                                   sut.prettyName(t[-1][0]), 1)
            elif (len(t) < len(signatures[sig][1])):
                signatures[sig] = (fn, t, sut.failure(), sut.prettyName(
                    t[-1][0]), signatures[sig][4] + 1)
            else:
                (sfn, st, sf, sp, count) = signatures[sig]
                signatures[sig] = (sfn, st, sf, sp, count + 1)
        else:
            numPassing += 1

    for sig in sorted(
            signatures.keys(),
            key=lambda x: signatures[x][4],
            reverse=True):
        print("=" * 80)
        print("TEST:", signatures[sig][0], "LENGTH:", len(signatures[sig][1]))
        print("OPERATION:", signatures[sig][3])
        if config.actionClasses:
            print("ACTION CLASSES:", set(map(lambda x: sut.prettyName(x[0]), signatures[sig][1])))
        print("EXCEPTION:", repr(signatures[sig][2]))
        print("FAILURE:")
        traceback.print_tb(signatures[sig][2][2], file=sys.stdout)
        print("COUNT:", signatures[sig][4],
              "(" + str(round(signatures[sig][4]/numTests, 2) * 100) + "%)")
        if config.showTests:
            sut.prettyPrintTest(signatures[sig][1])
    print()
    print("*" * 80)
    print(int(numTests), "TOTAL FAILING TESTS")
    if numInvalid > 0:
        print(numInvalid, "TOTAL INVALID TESTS")
    if numPassing > 0:
        print(numPassing, "TOTAL PASSING TESTS")
