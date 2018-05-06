from __future__ import print_function

import sys
import traceback
import os
import time

# Appending current working directory to sys.path
# So that user can run randomtester from the directory where sut.py is located
current_working_dir = os.getcwd()
sys.path.append(current_working_dir)

if "--help" not in sys.argv:
    import sut as SUT


def trace_lines(frame, event, arg):
    if event != 'line':
        return
    co = frame.f_code
    func_name = co.co_name
    line_no = frame.f_lineno
    print('   %s line %s' % (func_name, line_no))
    sys.stdout.flush()


def trace_calls(frame, event, arg):
    if event != 'call':
        return
    co = frame.f_code
    func_name = co.co_name
    if func_name == 'write':
        # Ignore write() calls from print statements
        return
    line_no = frame.f_lineno
    filename = co.co_filename
    print('Call to %s on line %s of %s' % (func_name, line_no, filename))
    sys.stdout.flush()
    return trace_lines


def main():

    if "--help" in sys.argv:
        print(
            "Usage:  tstl_replay <test file> [--noCheck] [--logging loglevel] [--verbose] [--showActions] [--coverage]"
            + " [--internal] [--html directory] [--delay secs] [--trace] [--afl] [--aflswarm]")
        print("Options:")
        print("--noCheck:      do not run property checks")
        print("--logging:      set the logging level for the test")
        print("--verbose:      run with verbose action output")
        print("--hideOpaque:   hide opaque values in verbose actions")
        print("--showActions:  show all actions")
        print("--coverage:     report code coverage")
        print("--internal:     report detailed code coverage information")
        print("--html:         produce HTML report on coverage")
        print("--delay:        delay to inject between steps")
        print("--trace:        trace lines executed (does not work with SUTs compiled with coverage)")
        print("--afl:          test is in afl format")
        print("--aflswarm:     test is in afl swarm format")
        sys.exit(0)

    sut = SUT.sut()

    if not (("--coverage" in sys.argv) or ("--internal" in sys.argv)):
        try:
            sut.stopCoverage()
        except BaseException:
            pass

    if ("--trace" in sys.argv):
        goodToTrace = False
        try:
            sut.stopCoverage()
        except BaseException:
            goodToTrace = True
        if not goodToTrace:
            print(
                "CANNOT TRACE WHEN SUT IS COMPILED WITH COVERAGE.  REBUILD WITH --noCover")
            sys.exit(1)

    rout = open("replay.out", 'w')

    file = sys.argv[1]
    nocheck = "--noCheck" in sys.argv
    verbose = "--verbose" in sys.argv
    logLevel = None
    if "--logging" in sys.argv:
        lastWasLogging = False
        for line in sys.argv:
            if lastWasLogging:
                logLevel = int(line)
            if line == "--logging":
                lastWasLogging = True
            else:
                lastWasLogging = False

    delay = None
    if "--delay" in sys.argv:
        lastWasDelay = False
        for line in sys.argv:
            if lastWasDelay:
                delay = float(line)
            if line == "--delay":
                lastWasDelay = True
            else:
                lastWasDelay = False

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

    sut.restart()
    if logLevel is not None:
        sut.setLog(logLevel)
    i = 0
    if verbose:
        sut.verbose(True)
    if "--hideOpaque" in sys.argv:
        sut.verboseOpaque(False)
    if "--afl" not in sys.argv:
        with open(file, 'r') as f:
            theTest = f.readlines()
    else:
        readTest = sut.loadTest(
            file, afl=True, swarm=("--aflswarm" in sys.argv))
        theTest = map(lambda x: x[0] + "\n", readTest)
    for line in theTest:
        name = line[:-1]
        if name == "<<RESTART>>":
            if "--showActions" in sys.argv:
                print("<<RESTART>>")
            # print "RESTART"
            rout.write("<<RESTART>>\n")
            rout.flush()
            sut.restart()
        else:
            if verbose:
                print("STEP #" + str(i) + ":", end=' ')
            rout.write(line)
            rout.flush()
            action = sut.playable(name)
            if "--showActions" in sys.argv:
                print(sut.prettyName(action[0]))
            if action[1]():  # check the guard
                if "--trace" in sys.argv:
                    sys.settrace(trace_calls)
                stepOk = sut.safely(action)
                if "--trace" in sys.argv:
                    sys.settrace(None)
                if not stepOk:
                    print("FAILED STEP")
                    print(sut.failure())
                    traceback.print_tb(sut.failure()[2], file=sys.stdout)
                    if "--internal" in sys.argv:
                        sut.internalReport()

                    if "--coverage" in sys.argv:
                        print(sut.report("coverage.out"), "PERCENT COVERED")

                    if htmlOut is not None:
                        sut.htmlReport(htmlOut)
                    sys.exit(255)
            if not nocheck:
                checkResult = sut.check()
                if not checkResult:
                    print("FAILED PROPERTY")
                    print(sut.failure())
                    traceback.print_tb(sut.failure()[2], file=sys.stdout)
                    if "--internal" in sys.argv:
                        sut.internalReport()

                    if "--coverage" in sys.argv:
                        print(sut.report("coverage.out"), "PERCENT COVERED")

                    if htmlOut is not None:
                        sut.htmlReport(htmlOut)

                    sys.exit(255)
            if delay is not None:
                time.sleep(delay)
        i += 1

    rout.write("TEST REPLAYED SUCCESSFULLY\n")
    rout.close()
    if "--internal" in sys.argv:
        sut.internalReport()

    if "--coverage" in sys.argv:
        print(sut.report("coverage.out"), "PERCENT COVERED")

    if htmlOut is not None:
        sut.htmlReport(htmlOut)

    sys.exit(0)
