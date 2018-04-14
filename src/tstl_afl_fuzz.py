from __future__ import print_function

import sys
import time
import traceback
import argparse
import os
import subprocess
import random
from collections import namedtuple

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--timeout', type=int, default=86400,
                        help='Total time budget for testing')
    parser.add_argument('--corpusBudget', type=int, default=600,
                        help='Time budget for generating a corpus to get afl started (default 5 minutes)')    
    parser.add_argument('--aflTimeout', type=int, default=5000,
                        help='afl timeout (default 5000)')    
    parser.add_argument('--input', type=str, default="aflinputs",
                        help='Where to put corpus files (default aflinputs)')
    parser.add_argument('--output', type=str, default="afloutputs",
                        help='Where to put afl fuzzing output (default afloutputs)')
    parser.add_argument('--noCheck', action='store_true',                            
                        help='Do not check properties')
    parser.add_argument('--depth', type=int, default=100,
                        help='Test depth for corpus construction (default 100)')
    parser.add_argument('--swarm', action='store_true',                            
                        help='Use swarm testing.')
    parser.add_argument('--noCover', action='store_true',                            
                        help='Do not use coverage to guide corpus tests')                 
    parser.add_argument('--noReduce', action='store_true',                            
                        help='Do not reduce corpus tests')
    parser.add_argument('--skipFails', action='store_true',                            
                        help='Skip over failed tests during corpus generation')    
    parser.add_argument('--thorough', action='store_true',                            
                        help='Include afl deterministic steps (slows things down A LOT)')    
    parser.add_argument('--instrumentAll', action='store_true',                            
                        help='Instrument TSTL harness as well (usually not a good idea)')    
    
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

    if not os.path.exists(config.input):
        os.mkdir(config.input)

    start = time.time()
    corpusCmd = "tstl_aflcorpus " + config.input + " " + str(config.depth) + " " + str(config.corpusBudget)
    if config.swarm:
        corpusCmd += " --swarm"
    if config.noCheck:
        corpusCmd += " --noCheck"        
    if config.noCover:
        corpusCmd += " --noCover"
    if config.noReduce:
        corpusCmd += " --noReduce"
    if config.skipFails:
        corpusCmd += " --skipFails"                
    P = subprocess.Popen([corpusCmd], shell=True)
    while (time.time() - start) < config.corpusBudget:
        time.sleep(1)
    if P.poll() != None:
        P.kill()
        print ("KILLED TSTL CORPUS GENERATION")
    
    aflCmd = "py-afl-fuzz -t " + str(config.aflTimeout) + " -i " + config.input + " -o " + config.output
    if not config.thorough:
        aflCmd += " -d"
    aflCmd += " -- tstl_afl"
    if config.swarm:
        aflCmd += " --swarm"
    if config.noCheck:
        aflCmd += " --noCheck"
    if not config.instrumentAll:
        os.putenv("PYTHON_AFL_TSTL","TRUE")
    else:
        os.unsetenv("PYTHON_AFL_TEST")
    print ("RUNNING AFL WITH COMMAND LINE:",aflCmd)        
    start = time.time()
    P = subprocess.Popen([aflCmd], shell=True)
    while (time.time() - start) < (config.timeout - config.corpusBudget):
        time.sleep(1)
    P.kill()
    print("KILLED AFL SUBPROCESS")
    print("DONE TESTING")
