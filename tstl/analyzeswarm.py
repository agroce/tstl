from __future__ import print_function

import sys
import argparse
import os
from collections import namedtuple
from statsmodels.stats.proportion import proportion_confint

# Appending current working directory to sys.path
# So that user can run randomtester from the directory where sut.py is located
current_working_dir = os.getcwd()
sys.path.append(current_working_dir)

if "--help" not in sys.argv:
    import sut as SUT


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('swarmData', metavar='filename', type=str, default=None,
                        help='Swarm coverage data to use.')
    parser.add_argument('target', metavar='str', type=str, default=None,
                        help='Coverage target.')
    parser.add_argument('probFile', metavar='filename', type=str, default=None,
                        help='File for output probabilities.')
    parser.add_argument('--mode', type=str, default='halfswarm',
                        help='Mode: halfswarm/no-suppressors/triggersonly (default halfswarm).')
    parser.add_argument('--confidence', type=float, default=0.95,
                        help='Confidence level to use (default 0.95 = 95%).')

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
    print(('Generating swarm probabilties using config={}'.format(config)))

    sut = SUT.sut()

    try:
        sut.stopCoverage()
    except BaseException:
        pass

    target = eval(config.target)

    tests = []

    mode = "CONFIG"
    entryClasses = []
    entryBranches = []
    entryStatements = []
    for line in open(config.swarmData):
        if "::::" in line:
            if mode == "CONFIG":
                ac = line.split("::::")[1][:-1]
                entryClasses.append(ac)
            elif mode == "BRANCHES":
                b = eval(line.split("::::")[1][:-1])
                entryBranches.append(b)
            elif mode == "STATEMENTS":
                s = eval(line.split("::::")[1][:-1])
                entryStatements.append(s)
        elif "CONFIG:" in line:
            if entryClasses != []:
                tests.append((entryClasses, entryBranches, entryStatements))
                entryClasses = []
                entryBranches = []
                entryStatements = []
                mode = "CONFIG"
        elif "BRANCHES:" in line:
            mode = "BRANCHES"
        elif "STATEMENTS:" in line:
            mode = "STATEMENTS"

    count = {}

    for t in tests:
        _, branches, statements = t
        for branch in branches:
            if branch not in count:
                count[branch] = 1
            else:
                count[branch] += 1
        for stmt in statements:
            if stmt not in count:
                count[stmt] = 1
            else:
                count[stmt] += 1

    rates = {}
    for ac in sut.actionClasses():
        acCount = 0
        for t in tests:
            if ac in t[0]:
                acCount += 1
        rates[ac] = acCount / float(len(tests))

    triggers = []
    suppressors = []

    hitT = []
    for t in tests:
        if (target in t[1]) or (target in t[2]):
            hitT.append(t)

    for ac in sut.actionClasses():
        if rates[ac] == 1.0:
            # Neither a suppressor nor trigger if present in every test!
            continue
        rate = rates[ac]
        hits = 0
        for t in hitT:
            if ac in t[0]:
                hits += 1

        low, high = proportion_confint(hits, len(hitT), method='wilson', alpha=1 - config.confidence)

        if low > rate:
            triggers.append(ac)
        if high < rate:
            suppressors.append(ac)

    print("=" * 80)
    sratio = float(count[target]) / len(tests)
    print(target, count[target], "HITS", sratio, "RATIO")
    print("TRIGGERS:")
    for tr in triggers:
        print(tr, rates[tr])
    print()
    print("SUPPRESSORS:")
    for sp in suppressors:
        print(sp, rates[sp])
    print()

    cp = {}
    for ac in sut.actionClasses():
        if ac in triggers:
            cp[ac] = 1.0
        elif ac in suppressors:
            cp[ac] = 0.0
        else:
            if config.mode == "halfswarm":
                cp[ac] = 0.5
            elif config.mode == "triggers-only":
                cp[ac] = 0.0
            else:
                cp[ac] = 1.0

    sut.writeProbFile(config.probFile, cp)
