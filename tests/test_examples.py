from __future__ import print_function
import os
import subprocess
import glob
import time
import py_compile
import sys
from unittest import TestCase


class TestExamples(TestCase):
    def setUp(self):
        os.chdir("examples")

    def tearDown(self):
        if os.path.basename(os.getcwd()) == "examples":
            os.chdir("..")
        else:
            os.chdir("../..")

    def test_examples(self):
        PY3 = sys.version_info[0] == 3

        noTests = False

        skipTravis = [
            "redis",
            "simplejson",
            "solc",
            "sortedcontainers",
            "pystan"]

        skipPY3 = [
            "microjson",
            "XML",
            "turtle"]

        justCompile = [
            "gmpy2",
            "arcpy",
            "tstl",
            "stringh",
            "pyfakefs",
            "turtle",
            "bidict",
            "numpy",
            "z3",
            "osquery",
            "datarray_inference",
            "dateutil",
            "tictactoe"]

        if PY3:
            justCompile.extend(skipPY3)

        compileFailures = []
        expectedCompile = []
        bytecodeFailures = []
        expectedBytecode = ['arcpy/arcpy1.tstl', 'arcpy/arcpy5.tstl']
        timeoutFailures = []
        expectedTimeout = ['arrow/arrow.tstl']
        testingFailures = []
        expectedTesting = []
        freeTestingFailures = []
        expectedFreeTesting = []

        for f in os.listdir("."):
            if os.path.isdir(f):
                os.chdir(f)
                print("=" * 80)
                for t in glob.glob("*.tstl"):
                    print(f + "/" + t, end=":  ")
                    print("COMPILING", end="...")
                    sys.stdout.flush()
                    tstlCmd = ["tstl", t]
                    if "tensorflow" in f:
                        tstlCmd += ["--noReload"]
                    r = subprocess.call(tstlCmd)
                    if r != 0:
                        print("FAILED TO COMPILE!")
                        compileFailures.append(f + "/" + t)
                        print()
                        os.remove("sut.py")
                        continue
                    if (os.getenv("TRAVIS") == "TRUE") and (f in skipTravis):
                        print("OK")
                        continue
                    print("COMPILING TO BYTECODE", end="...")
                    sys.stdout.flush()
                    try:
                        start = time.time()
                        py_compile.compile("sut.py", doraise=True)
                        print("NEEDED", round(time.time() - start, 2), "SECONDS", end="...")
                    except py_compile.PyCompileError as e:
                        print("BYTECODE COMPILATION FAILED!")
                        print(e)
                        bytecodeFailures.append(f + "/" + t)
                        print()
                        os.remove("sut.py")
                        continue
                    skipThis = False
                    for jc in justCompile:
                        if jc in f:
                            skipThis = True
                            break
                    if noTests or skipThis or (f == "c"):
                        print("OK!")
                        os.remove("sut.py")
                        try:
                            os.remove("sut.pyc")
                        except OSError:
                            pass
                        continue
                    print("RUNNING", end="...")
                    sys.stdout.flush()
                    rtCmd = [
                        "tstl_rt",
                        "--timeout",
                        "45",
                        "--timedProgress",
                        "10",
                        "--noCheck",
                        "--uncaught",
                        "--silentSUT"]
                    start = time.time()
                    p = subprocess.Popen(rtCmd)
                    # Big timeout is for huge coverage dumps like sympy
                    while (p.poll() is None) and ((time.time() - start) < 180):
                        time.sleep(1)
                    if p.poll() is None:
                        p.terminate()
                        print("TIMEOUT!")
                        timeoutFailures.append(f + "/" + t)
                    else:
                        r = p.returncode
                        if r != 0:
                            print("FAILED DURING UNFAILABLE TESTING!")
                            testingFailures.append(f + "/" + t)
                        else:
                            print("OK!")
                    sys.stdout.flush()
                    rtCmd = [
                        "tstl_rt",
                        "--timeout",
                        "25",
                        "--timedProgress",
                        "10",
                        "--noCover",
                        "--output",
                        ".freefail",
                        "--silentSUT"]
                    start = time.time()
                    with open(os.devnull, 'w') as dnull:
                        p = subprocess.Popen(rtCmd, stdout=dnull)
                    # Big timeout is for huge coverage dumps like sympy
                    while (p.poll() is None) and ((time.time() - start) < 180):
                        time.sleep(1)
                    if p.poll() is None:
                        p.terminate()
                        print("TIMEOUT DURING FREE TESTING!")
                        timeoutFailures.append(f + "/" + t)
                    else:
                        r = p.returncode
                        if r not in [0, 255]:
                            print("FAILURE DURING FREE TESTING!")
                            freeTestingFailures.append(f + "/" + t)
                        else:
                            if r == 255:
                                rr1 = subprocess.call(["tstl_reduce",
                                                       ".freefail",
                                                       ".freesmall",
                                                       "--verbose",
                                                       "True"])
                                self.assertEqual(rr1, 0)
                                rr2 = subprocess.call(["tstl_replay",
                                                       ".freesmall"])
                                self.assertEqual(rr2, 255)
                    os.remove("sut.py")
                    try:
                        os.remove("sut.pyc")
                    except OSError:
                        pass
                os.chdir("..")
                sys.stdout.flush()

        print("COMPILATION FAILURES:", compileFailures)
        print("BYTECODE COMPILATION FAILURES:", bytecodeFailures)
        print("TIMEOUTS:", timeoutFailures)
        print("TESTING FAILURES:", testingFailures)
        print("FREE TESTING FAILURES:", freeTestingFailures)
        self.assertTrue(sorted(compileFailures) == sorted(expectedCompile))
        # These aren't even running, so need subset
        self.assertTrue(set(bytecodeFailures).issubset(set(expectedBytecode)))
        self.assertTrue(set(timeoutFailures).issubset(set(expectedTimeout)))
        self.assertTrue(set(testingFailures).issubset(set(expectedTesting)))
        self.assertTrue(set(freeTestingFailures).issubset(set(expectedFreeTesting)))
