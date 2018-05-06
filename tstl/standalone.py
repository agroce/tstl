from __future__ import print_function

import sys
import os

# Appending current working directory to sys.path
# So that user can run randomtester from the directory where sut.py is located
current_working_dir = os.getcwd()
sys.path.append(current_working_dir)

if "--help" not in sys.argv:
    import sut as SUT


def main():

    if "--help" in sys.argv:
        print("Usage:  tstl_standalone <test file> <output Python file> [<sut file>]",
              "[--noCheck] [--noRefs] [--regression] [--verbose]")
        print("  default for <sut file> is sut.py")
        print("Options:")
        print(" --noCheck:      do not include property checks")
        print(" --noRefs:       do not include reference actions")
        print(" --regression:   produce a regression test that captures values")
        print(" --verbose:      produce a verbose test that shows actions taken")
        sys.exit(0)

    testFile = sys.argv[1]
    outFile = sys.argv[2]
    if (len(sys.argv) > 3) and (".py" in sys.argv[3]):
        sutFile = sys.argv[3]
    else:
        sutFile = "sut.py"

    checkProps = "--noCheck" not in sys.argv
    checkRefs = "--noRefs" not in sys.argv
    makeRegression = "--regression" in sys.argv
    verbose = "--verbose" in sys.argv

    t = SUT.sut()

    def globalCheck(str):
        if " # CHECK POOL INIT" not in str:
            return str

        newStr = str.replace("(", '("')
        newStr = newStr.replace(" is not None)", '" in globals())')
        return newStr.replace("# CHECK POOL INIT", "")

    outf = open(outFile, 'w')
    startPrelim = False
    startCheck = False
    startReload = False
    startInit = False

    reloadCode = []
    initCode = []

    outf.write("from __future__ import print_function\n\n")

    for line in open(sutFile):
        if "END STANDALONE CODE" in line:
            startPrelim = False
        if "END CHECK CODE" in line:
            startCheck = False
        if "END RELOAD CODE" in line:
            startReload = False
        if "END INITIALIZATION CODE" in line:
            startInit = False
        if startPrelim:
            outf.write(line)
        if startCheck:
            outf.write(globalCheck(t.prettyName(
                line.replace("# GLOBAL ", "global "))))
        if startReload:
            reloadCode.append(line.lstrip())
        if startInit:
            initCode.append(line.lstrip())
        if "BEGIN STANDALONE CODE" in line:
            startPrelim = True
        if checkProps and ("BEGIN CHECK CODE" in line):
            startCheck = True
            outf.write("\n\ndef check():\n")
        if "BEGIN RELOAD CODE" in line:
            startReload = True
        if "BEGIN INITIALIZATION CODE" in line:
            startInit = True

    outf.write("\n\n")

    for i in initCode:
        outf.write(t.prettyName(i))

    outf.write("\n\n")

    for line in open(testFile):
        if line == "<<RESTART>>":
            if makeRegression:
                t.restart()
            outf.write("\n# RESTART\n\n")
            for r in reloadCode:
                outf.write(r)
            for i in initCode:
                outf.write(i)
        name = line[:-1]
        if t.getPreCode(name) is not None:
            for p in t.getPreCode(name):
                outf.write(t.prettyName(p) + "\n")
        if makeRegression:
            t.safely(t.playable(name))
        if verbose:
            outf.write("print ('''" + t.prettyName(name) + "''')\n")
        if t.getOkExceptions(name) == "":
            outf.write(t.prettyName(name) + "\n")
        else:
            outf.write("try:\n")
            outf.write("  " + t.prettyName(name) + "\n")
            outf.write("except (" + t.getOkExceptions(name) + "):\n")
            outf.write("  pass\n")
        if t.getPropCode(name) is not None:
            outf.write("assert " + t.prettyName(t.getPropCode(name)) + "\n")
        if checkRefs:
            if t.getRefCode(name) is not None:
                for r in t.getRefCode(name):
                    outf.write("try:\n")
                    outf.write("  " + t.prettyName(r) + "\n")
                    outf.write("except:\n")
                    outf.write("  pass\n")
        if checkProps:
            outf.write("check()\n")
        if makeRegression:
            v = t.shallowState()
            for (p, vals) in v:
                if t.prettyName(p) not in name:
                    continue
                if p in t.opaque():
                    continue
                if t.abstraction(p) is not None:
                    absFun = t.abstraction(p)
                else:
                    absFun = ""
                for i in vals:
                    if vals[i] is not None:
                        pname = t.prettyName(p + "[" + str(i) + "]")
                        outf.write(
                            "assert (repr(" +
                            absFun +
                            "(" +
                            pname +
                            ')) == (' +
                            repr(
                                repr(
                                    vals[i])) +
                            '))\n')

    outf.write('\n\nprint ("TEST COMPLETED SUCCESSFULLY")\n')
    outf.close()
