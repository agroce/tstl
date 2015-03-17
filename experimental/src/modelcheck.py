import sut as SUT
import random
import time
import sys
import traceback
import argparse
import os
from collections import namedtuple

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--depth', type=int, default=-1,
                        help='Maximum search depth (-1=infinite default).')
    parser.add_argument('-t', '--timeout', type=int, default=3600,
                        help='Timeout in seconds (3600 default).')
    parser.add_argument('-r', '--random', action="store_true",
                        help='Randomize transition order')
    parser.add_argument('-s', '--seed', type=int, default=None,
                        help='Random seed (default = None).')
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
print('Model checking using config={}'.format(config))

if config.seed != None:
    random.seed(config.seed)

def dfs (test):
    elapsed = time.time()-start
    if (elapsed > config.timeout):
        print "EXITING DUE TO TIMEOUT"
        sys.exit(2)
    if len(test) == config.depth:
        return
    old = t.state()
    visited.append(old)
    allt = t.enabled()
    if config.random:
        random.shuffle(allt)
    for tran in t.enabled():
        newtest = list(test)
        newtest.append(tran[0])
        try:
            tran[2]()
        except:
            pass
        try:
            t.check()
        except:
            _,_,tb = sys.exc_info()
            traceback.print_tb(tb)
            tbInfo = traceback.extract_tb(tb)
            filename,line,func,text = tbInfo[-1]
            print "TEST:"
            for step in newtest:
                print step
            print "EXITING DUE TO FAILED TEST"
            sys.exit(1)
        if t.state() not in visited:
            dfs (newtest)
        t.backtrack(old)
                

start = time.time()

t = SUT.t()
t.restart()
visited = []
dfs([])

