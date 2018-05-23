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
    parser.add_argument('prefix', metavar='filename', type=str, default=None,
                        help='Prefix for output files.')
    parser.add_argument('--confidence', type=float, default=0.95,
                        help='Confidence level to use (default 0.95 = 95%).')
    parser.add_argument('--cutoff', type=float, default=1.0,
                        help='Frequency at which to start ignoring targets (default = 1.0).')
    parser.add_argument('--minHits', type=int, default=0,
                        help='Minimum number of hits before analyzing a target (default = 0).')

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

    verbose = False

    try:
        sut.stopCoverage()
    except BaseException:
        pass

    numTests = 0

    mode = "CONFIG"
    entryClasses = []
    entryBranches = []
    entryStatements = []

    count = {}
    branches = set([])
    statements = set([])

    hits = {}

    print("READING DATA...")
    for line in open(config.swarmData):
        if "::::" in line:
            if mode == "CONFIG":
                ac = line.split("::::")[1][:-1]
                entryClasses.append(ac)
                if ac in count:
                    count[ac] += 1
                else:
                    count[ac] = 1
            elif mode == "BRANCHES":
                b = eval(line.split("::::")[1][:-1])
                entryBranches.append(b)
                if b in count:
                    count[b] += 1
                else:
                    count[b] = 1
                    hits[b] = []
                branches.add(b)
            elif mode == "STATEMENTS":
                s = eval(line.split("::::")[1][:-1])
                entryStatements.append(s)
                if s in count:
                    count[s] += 1
                else:
                    count[s] = 1
                    hits[s] = []
                statements.add(s)
        elif "CONFIG:" in line:
            if entryClasses != []:
                numTests += 1
                for b in entryBranches:
                    hits[b].append(entryClasses)
                for s in entryStatements:
                    hits[s].append(entryClasses)
                entryClasses = []
                entryBranches = []
                entryStatements = []
                mode = "CONFIG"
        elif "BRANCHES:" in line:
            mode = "BRANCHES"
        elif "STATEMENTS:" in line:
            mode = "STATEMENTS"
    numTests += 1
    for b in entryBranches:
        hits[b].append(entryClasses)
    for s in entryStatements:
        hits[s].append(entryClasses)
    print("DONE")

    eqClasses = {}

    targets = branches.union(statements)
    print("ANALYZING", len(targets), "TARGETS")

    analyzed = 0

    for target in targets:

        if float(count[target])/numTests >= config.cutoff:
            analyzed += 1
            continue

        triggers = []
        suppressors = []

        hitT = hits[target]
        if len(hitT) < config.minHits:
            analyzed += 1
            continue

        for ac in sut.actionClasses():
            rate = float(count[ac]) / numTests
            if rate == 1.0:
                # Neither a suppressor nor trigger if present in every test!
                continue
            chits = 0
            for t in hitT:
                if ac in t:
                    chits += 1

            low, high = proportion_confint(chits, len(hitT), method='wilson', alpha=1 - config.confidence)

            if low > rate:
                triggers.append(ac)
            if high < rate:
                suppressors.append(ac)

        signature = (tuple(sorted(triggers)), tuple(sorted(suppressors)))
        data = (target, count[target])
        analyzed += 1
        if signature not in eqClasses:
            if verbose:
                print("NEW EQUIVALENCE CLASS AFTER ANALYZING", analyzed, "TARGETS")
                print("NOW", len(eqClasses), "EQUIVALENCE CLASSES")
                print("TRIGGERS:", triggers)
                print("SUPPRESSORS:", suppressors)
                print("TARGET:", target)
                print("FREQUENCY:", count[target])
            eqClasses[signature] = (triggers, suppressors, [data])
        else:
            eqClasses[signature][2].append(data)

    pcount = 0
    with open(config.prefix + ".classes", 'w') as cfile:
        for c in sorted(eqClasses.keys(), key=lambda x: min(map(lambda y: y[1], eqClasses[x][2]))):
            triggers, suppressors, targets = eqClasses[c]
            if (triggers == []) and (suppressors == []):
                continue  # Ignore the no-data class
            print("=" * 80)
            print("# TARGETS:", len(targets))
            print("MINIMUM FREQUENCY:", min(map(lambda x: x[1], targets)))
            print("TRIGGERS:", triggers)
            print("SUPPRESSORS:", suppressors)
            cfile.write("TRIGGERS:\n")
            cp = {}
            for t in triggers:
                cfile.write(t + "\n")
                cp[t] = 1.0
            cfile.write("SUPPRESSORS:\n")
            for s in suppressors:
                cfile.write(s + "\n")
                cp[s] = 0.0
            cfile.write("TARGETS:\n")
            for t in targets:
                cfile.write(repr(t[0]) + " :::: " + str(t[1]) + "\n")
            cfile.write("FILE: " + config.prefix + "." + str(pcount) + ".prob\n")
            sut.writeProbFile(config.prefix + "." + str(pcount) + ".prob", cp)
            pcount += 1
