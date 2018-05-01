from __future__ import print_function

import sys
import time
import argparse
import os
import subprocess
import glob
from collections import namedtuple


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--timeout', type=int, default=86400,
                        help='Total time budget for testing')
    parser.add_argument(
        '--corpusBudget',
        type=int,
        default=600,
        help='Time budget for generating a corpus to get afl started (default 5 minutes)')
    parser.add_argument('--aflTimeout', type=str, default="5000",
                        help='afl timeout (default 5000)')
    parser.add_argument('--autoTimeout', action='store_true',
                        help='Use automatic calibration to determine timeout')
    parser.add_argument('--aflMemory', type=str, default="4096",
                        help='afl memory limit (default 4096)')
    parser.add_argument('--autoMemory', action='store_true',
                        help='Use automatic calibration to determine memory')
    parser.add_argument('--input', type=str, default="aflinputs",
                        help='Where to put corpus files (default aflinputs)')
    parser.add_argument(
        '--output',
        type=str,
        default="afloutputs",
        help='Where to put afl fuzzing output (default afloutputs)')
    parser.add_argument(
        '--resume',
        action='store_true',
        help='Resume interrupted fuzzing; ignores --input, --output should point to old session')
    parser.add_argument(
        '--burst',
        action='store_true',
        help='Build corpus in burst mode; overrides most other corpus options')
    parser.add_argument('--noCheck', action='store_true',
                        help='Do not check properties')
    parser.add_argument(
        '--depth',
        type=int,
        default=100,
        help='Test depth for corpus construction (default 100)')
    parser.add_argument('--quiet', action='store_true',
                        help='Redirect afl-fuzz to /dev/null.')
    parser.add_argument('--swarm', action='store_true',
                        help='Use swarm testing.')
    parser.add_argument('--noCover', action='store_true',
                        help='Do not use coverage to guide corpus tests')
    parser.add_argument('--noReduce', action='store_true',
                        help='Do not reduce corpus tests')
    parser.add_argument('--skipFails', action='store_true',
                        help='Skip over failed tests during corpus generation')
    parser.add_argument(
        '--thorough',
        action='store_true',
        help='Include afl deterministic steps (slows things down A LOT)')
    parser.add_argument(
        '--instrumentAll',
        action='store_true',
        help='Instrument TSTL harness as well (usually not a good idea)')
    parser.add_argument(
        '--persist',
        action='store_true',
        help='Use persistent mode (experimental and not recommended')

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
    print(('Fuzzing with afl using config={}'.format(config)))

    if not config.resume:
        if not os.path.exists(config.input):
            os.mkdir(config.input)

        if config.burst:
            corpusTimeout = 60
        else:
            corpusTimeout = config.corpusBudget

        if corpusTimeout:
            start = time.time()
            corpusCmd = ["tstl_aflcorpus", config.input,
                         str(config.depth), str(config.corpusBudget)]
            if config.burst:
                corpusCmd += ["--burst"]
            if config.swarm:
                corpusCmd += ["--swarm"]
            if config.noCheck:
                corpusCmd += ["--noCheck"]
            if config.noCover:
                corpusCmd += ["--noCover"]
            if config.noReduce:
                corpusCmd += ["--noReduce"]
            if config.skipFails:
                corpusCmd += ["--skipFails"]
            P = subprocess.Popen(corpusCmd)
            while (time.time() - start) < corpusTimeout:
                time.sleep(1)
            if P.poll() is None:
                try:
                    P.terminate()
                    P.wait()
                    print("KILLED TSTL CORPUS GENERATION")
                except OSError:
                    pass

    aflCmd = ["py-afl-fuzz"]
    if not config.autoTimeout:
        aflCmd += ["-t", config.aflTimeout]
    if not config.autoMemory:
        aflCmd += ["-m", str(config.aflMemory)]
    if not config.resume:
        aflCmd += ["-i", config.input]
    else:
        aflCmd += ["-i-"]
    aflCmd += ["-o", config.output]
    if not config.thorough:
        aflCmd += ["-d"]
    aflCmd += ["--", "tstl_afl"]
    if config.swarm:
        aflCmd += ["--swarm"]
    if config.noCheck:
        aflCmd += ["--noCheck"]
    if config.persist:
        aflCmd += ["--persist"]
    aflCmdStr = " ".join(aflCmd)
    if not config.instrumentAll:
        os.putenv("PYTHON_AFL_TSTL", "TRUE")
        aflCmdStr = "PYTHON_AFL_TSTL=TRUE " + aflCmdStr
    elif os.getenv("PYTHON_AFL_TSTL") is not None:
        os.unsetenv("PYTHON_AFL_TSTL")
        aflCmdStr = "env -u PYTHON_AFL_TSTL " + aflCmdStr
    print("RUNNING AFL WITH COMMAND LINE:", aflCmdStr)
    start = time.time()
    if not config.quiet:
        P = subprocess.Popen(aflCmd)
    else:
        with open(os.devnull, 'w') as dnull:
            P = subprocess.Popen(aflCmd, stdout=dnull)
    originalFails = glob.glob("aflfail.*")
    while (time.time() - start) < (config.timeout - config.corpusBudget):
        if config.quiet:
            newGlob = glob.glob("aflfail.*")
            failDiff = len(newGlob) - len(originalFails)
            if failDiff > 0:
                print(failDiff, "NEW FAILING TESTS GENERATED; NOW", len(originalFails) + failDiff, "FAILING TESTS")
                originalFails = newGlob
        time.sleep(1)
    P.terminate()
    P.wait()
    print("KILLED AFL SUBPROCESS")
    print("DONE TESTING")
