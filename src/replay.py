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
        print "Usage:  tstl_replay <test file> [--noCheck] [--logging loglevel] [--verbose] [--coverage] [--internal] [--html directory]"
        print "Options:"
        print "--noCheck:      do not run property checks"
        print "--logging:      set the logging level for the test"
        print "--verbose:      run with verbose action output"
        print "--coverage:     report code coverage"        
        print "--internal:     report detailed code coverage information"
        print "--html:         produce HTML report on coverage"
        sys.exit(0)
    
    if not (("--coverage" in sys.argv) or ("--internal" in sys.argv)):
        try:
            sut.stopCoverage()
        except:
            pass

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
            else:
                lastWasLogging = False

    htmlOut = None
    lastWasHtml = False
    for f in sys.argv[1:]:
        if lastWasHtml:
            htmlOut = f
            lastWasHtml = False
        elif f == "--html":
            lastWasHtml = True
        else:
            lastWasHtml = False
                
    sut = SUT.sut()
    sut.restart()
    if logLevel != None:
        sut.setLog(logLevel)
    i = 0
    if verbose:
        sut.verbose(True)
    for l in open(file):
        name = l[:-1]
        if name == "<<RESTART>>":
            #print "RESTART"
            rout.write("RESTART\n")
            sut.restart()
        else:
            if verbose:
                print "STEP #"+str(i)+":",
            rout.write("STEP " + str(i) + ": " + name + "\n")
            action = sut.playable(name)
            if action[1](): # check the guard
                stepOk = sut.safely(action)
                if not stepOk:
                    print "FAILED STEP"
                    print sut.failure()
                    traceback.print_tb(sut.failure()[2],file=sys.stdout)
                    if "--internal" in sys.argv:
                        sut.internalReport()
                        
                    if "--coverage" in sys.argv:
                        print sut.report("coverage.out"),"PERCENT COVERED"    

                    if htmlOut != None:
                        sut.htmlReport(htmlOut)                        
                    sys.exit(255)
            if not nocheck:
                checkResult = sut.check()
                if not checkResult:
                    print "FAILED PROPERTY"
                    print sut.failure()
                    traceback.print_tb(sut.failure()[2],file=sys.stdout)
                    if "--internal" in sys.argv:
                        sut.internalReport()
                        
                    if "--coverage" in sys.argv:
                        print sut.report("coverage.out"),"PERCENT COVERED"    

                    if htmlOut != None:
                        sut.htmlReport(htmlOut)
                        
                    sys.exit(255)                
        i += 1

    rout.write("TEST REPLAYED SUCCESSFULLY\n")
    rout.close()
    if "--internal" in sys.argv:
        sut.internalReport()
        
    if "--coverage" in sys.argv:
        print sut.report("coverage.out"),"PERCENT COVERED"    

    if htmlOut != None:
        sut.htmlReport(htmlOut)
        
    sys.exit(0)
