import sut as SUT
import random
import time
import sys
import traceback
import argparse
import os
from collections import namedtuple
import covertool

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--depth', type=int, default=100,
                        help='Maximum search depth (100 default).')
    parser.add_argument('-t', '--timeout', type=int, default=3600,
                        help='Timeout in seconds (3600 default).')
    parser.add_argument('-s', '--seed', type=int, default=None,
                        help='Random seed (default = None).')
    parser.add_argument('-m', '--maxtests', type=int, default=-1,
                        help='Maximum #tests to run (-1 = infinite default).')    
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
print('Random testing using config={}'.format(config))

start = time.time()
elapsed = time.time()-start

t = SUT.t()

covertool.clearCoverage()

ntests = 0
while (config.maxtests == -1) or (ntests < config.maxtests):
    ntests += 1

    t.restart()
    test = []

    print ntests, len(covertool.getCoverage())

    for s in xrange(0,config.depth):
        a = random.choice(t.enabled())
        test.append(a[0])
        
        cov = covertool.getCoverage()
        
        try:
            a[2]()
        except:
            pass
        
        covNew = covertool.getCoverage()
        if len(covNew) > len(cov):
            elapsed = time.time()-start
            print "FOUND NEW BRANCH", elapsed, len(covNew)

        try:
            t.check()
        except:
            _,_,tb = sys.exc_info()
            traceback.print_tb(tb)
            tbInfo = traceback.extract_tb(tb)
            filename,line,func,text = tbInfo[-1]
            print "TEST:"
            for step in test:
                print step 
            print "EXITING DUE TO FAILED TEST"
            sys.exit(1)
            
        elapsed = time.time() - start
        if elapsed > config.timeout:
            print "EXITING DUE TO TIMEOUT"
            print ntests, "EXECUTED"
            sys.exit(2)
            break

print ntests, "EXECUTED"


