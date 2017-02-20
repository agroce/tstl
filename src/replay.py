import sys
import traceback
import os

# Appending current working directory to sys.path
# So that user can run randomtester from the directory where sut.py is located
current_working_dir = os.getcwd()
sys.path.append(current_working_dir)

import sut as SUT

def main():


    if "--help" in sys.argv:
        print "Usage:  tstl_replay <test file> [--noCheck] [--logging loglevel] [--verbose]"
        print "Options:"
        print " --noCheck:      do not run property checks"
        print " --logging:      set the logging level for the test"
        print " --verbose:      run with verbose action output"
        sys.exit(0)
    
    rout = open("replay.out",'w')

    file = sys.argv[1]
    nocheck = "--noCheck" in sys.argv
    verbose = "--verbose" in sys.argv
    logLevel = None
    if "--logging" in sys.argv:
        lastWasLogging = False
        for l in sys.argv:
            if lastWasLogging:
                logLevel = int(l)
            if l == "--logging":
                lastWasLogging = True

    t = SUT.sut()
    t.restart()
    if logLevel != None:
        t.setLog(logLevel)
    i = 0
    if verbose:
        t.verbose(True)
    for l in open(file):
        name = l[:-1]
        if name == "<<RESTART>>":
            #print "RESTART"
            rout.write("RESTART\n")
            t.restart()
        else:
            if verbose:
                print "STEP",i,t.prettyName(name)
            rout.write("STEP " + str(i) + ": " + name + "\n")
            action = t.playable(name)
            if action[1](): # check the guard
                stepOk = t.safely(action)
                if not stepOk:
                    print "FAILED STEP"
                    print t.failure()
                    traceback.print_tb(t.failure()[2],file=sys.stdout)
                    sys.exit(255)
            if not nocheck:
                checkResult = t.check()
                if not checkResult:
                    print "FAILED PROPERTY"
                    print t.failure()
                    traceback.print_tb(t.failure()[2],file=sys.stdout)
                    sys.exit(255)                
        i += 1

    rout.write("TEST REPLAYED SUCCESSFULLY\n")
    rout.close()
    sys.exit(0)
