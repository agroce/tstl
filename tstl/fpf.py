from __future__ import print_function

import sys
import traceback
import argparse
import os
import glob
from collections import namedtuple
from scipy.spatial.distance import euclidean

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
    parser.add_argument('--ignoreLast', action='store_true',
                        help='Do not use last action in computing ranking.')
    parser.add_argument('--useFailures', action='store_true',
                        help='Use the failure output to help distinguish bugs.')
    parser.add_argument('--abstractStrings', action='store_true',
                        help='Abstract away strings in exceptions.')
    parser.add_argument('--ignoreContaining', type=str, default=None,
                        help='Ignore tests with provided string(s) in an action (separate strings with ";;").')

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


def vector(test, sut):
    v = []
    for ac in sorted(sut.actionClasses()):
        count = 0
        for s in test:
            if sut.actionClass(s) == ac:
                count += 1
        v.append(count)
    return v


def main():

    parsed_args, parser = parse_args()
    config = make_config(parsed_args, parser)
    print(('Triaging using config={}'.format(config)))

    if config.ignoreContaining is not None:
        ignoredStrings = config.ignoreContaining.split(";;")

    sut = SUT.sut()

    try:
        sut.stopCoverage()
    except BaseException:
        pass

    numTests = 0.0
    numInvalid = 0
    numPassing = 0

    failingTests = {}

    if config.useFailures:
        sigs = {}

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
                for istr in ignoredStrings:
                    if istr in s[0]:
                        foundString = True
                        break
                if foundString:
                    break
            if foundString:
                continue
        if not config.noCheck:
            fails = sut.failsAny(t)
        else:
            fails = sut.fails(t)
        if fails:
            ft = list(sut.test())
            v = vector(ft, sut)
            if config.useFailures:
                e = repr(sut.failure())
                e = e[:e.find("<traceback object at 0x")] + ")"
                sig = noDigits(e)
                if config.abstractStrings:
                    sig = noStrings(sig)
                if sig in sigs:
                    sigs[sig].append(fn)
                else:
                    sigs[sig] = [fn]
            if not config.ignoreLast:
                vlast = []
                for ac in sorted(sut.actionClasses()):
                    if sut.actionClass(ft[-1]) == ac:
                        vlast.append(1.0)
                    else:
                        vlast.append(0.0)
                v.extend(vlast)

            failingTests[fn] = (ft, v, sut.failure())
        else:
            numPassing += 1

    if config.useFailures:
        sk = sorted(sigs.keys())
        for fn in failingTests:
            vsig = []
            for sig in sk:
                if fn in sigs[sig]:
                    vsig.append(1.0)
                else:
                    vsig.append(0.0)
            _, v, _ = failingTests[fn]
            v.extend(vsig)

    distances = {}
    for fn in failingTests:
        distances[fn] = {}
    for fn1 in failingTests:
        for fn2 in failingTests:
            if fn1 == fn2:
                distances[fn1][fn2] = 0.0
                continue
            if fn1 > fn2:
                continue
            distances[fn1][fn2] = euclidean(failingTests[fn1][1], failingTests[fn2][1])
            distances[fn2][fn1] = distances[fn1][fn2]

    chosen = failingTests.keys()[0]
    print("=" * 80)
    print(1, chosen)
    if config.showTests:
        print()
        sut.prettyPrintTest(failingTests[chosen][0])
        f = failingTests[chosen][2]
        print("EXCEPTION:", repr(f))
        print("FAILURE:")
        traceback.print_tb(f[2], file=sys.stdout)

    ranked = [chosen]
    while len(ranked) != len(failingTests):
        chosen = None
        maxMinD = 0.0
        for fn in failingTests:
            d = []
            for r in ranked:
                d.append(distances[fn][r])
            minD = min(d)
            if minD > maxMinD:
                chosen = fn
                maxMinD = minD
        if chosen is None:
            print("ALL REMAINING TESTS ARE ZERO DISTANCE FROM A RANKED TEST")
            break
        ranked.append(chosen)
        print("=" * 80)
        print(len(ranked), chosen, maxMinD)
        if config.showTests:
            print()
            sut.prettyPrintTest(failingTests[chosen][0])
            print()
            f = failingTests[chosen][2]
            print("EXCEPTION:", repr(f))
            print("FAILURE:")
            traceback.print_tb(f[2], file=sys.stdout)

    print()
    print("*" * 80)
    print(int(numTests), "TOTAL FAILING TESTS")
    if numInvalid > 0:
        print(numInvalid, "TOTAL INVALID TESTS")
    if numPassing > 0:
        print(numPassing, "TOTAL PASSING TESTS")
