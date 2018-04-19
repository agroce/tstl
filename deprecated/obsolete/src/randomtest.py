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

if config.seed != None:
    mrandom = random.Random(config.seed)
else:
    mrandom = random.Random()

start = time.time()
elapsed = time.time()-start

seenvalues = []
def foo(code, text):
    if text in seenvalues:
        return
    seenvalues.append(text)
    print "NEW VALUE FOR V:",text 

t = SUT.t()

ntests = 0
test = []
while (config.maxtests == -1) or (ntests < config.maxtests):
    ntests += 1

    print "STARTING NEW TEST"
#    print "OLD TEST WAS:"
#    nstep = 0
#    for s in test:
#        nstep += 1
#        print "STEP",nstep,":",s
    t.restart()
    test = []
    full = []

    for s in xrange(0,config.depth):
        a = mrandom.choice(t.enabled())
        (text, guard, action) = a
        test.append(text)
        full.append(a)
#        print s,text

        try:
            action()
        except:
                _,_,tb = sys.exc_info()
                traceback.print_tb(tb)
                print "TEST:"
                for step in test:
                    print step 
                print "EXITING DUE TO FAILED TEST"
                print len(test)
                print "REDUCING..."
                newtest = t.reduce(full, t.fails)
                t.restart()
                t.logAll()
                for step in newtest:
                    print step[0]
                    if not t.safely(step[2]):
                        print t.failure()
                        _,_,tb = t.failure()
                        traceback.print_tb(tb)
                print len(newtest)    
                sys.exit(1)

        if not t.check():
            print "Property failed!"
            (_,_,tb) = t.failure()
            traceback.print_tb(tb)
            print "TEST:"
            for step in test:
                print step 
            print len(test)
            print "REDUCING..."
            newtest = t.reduce(full, t.failsCheck)
            t.restart()
            t.logAll()
            for step in newtest:
                print step[0]
                if not t.safely(step[2]):
                    print t.failure()
                    _,_,tb = t.failure()
                    traceback.print_tb(tb)
            print len(newtest)    
            print "EXITING DUE TO FAILED TEST"
            sys.exit(1)
            
        elapsed = time.time() - start
        if elapsed > config.timeout:
            print "EXITING DUE TO TIMEOUT"
            print ntests, "EXECUTED"
            t.report()
            sys.exit(2)

t.report()

print ntests, "EXECUTED"


