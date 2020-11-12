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
        if (os.getenv("TRAVIS") == "TRUE") and (
                os.getenv("TASK") != "EXAMPLES"):
            return

        PY3 = sys.version_info[0] == 3

        noTests = False

        skipTravis = [
            "redis",
            "simplejson",
            "solc",
            "vyper",
            "sortedcontainers",
            "pystan"]

        skipPY3 = [
            "XML",
            "microjson",
            "rsa",
            "turtle"]

        justCompile = [
            "AVL",
            "arcpy",
            "arrow",
            "biopython",
            "c",
            "datarray_inference",
            "dateutil",
            "gmpy2",
            "hypothesis_heaps",
            "lopsided_grammar",
            "maze",
            "numpy",
            "osquery",
            "parallelsorts",
            "pyfakefs",
            "stringh",
            "sympy",
            "tensorflow",
            "tictactoe",
            "tstl",
            "turtle"]

        problemsFree = []

        testSmallcheck = True
        noSmallcheck = [
            "bidict",
            "biopython",
            "danluuexample",
            "eval",
            "rsa",
            "tensorflow"]

        shouldFail = [
            "newxml.tstl",
            "nutshell.tstl",
            "onestep.tstl",
            "statechanginginvar.tstl",
            "turtle.tstl",
            "water.tstl"]

        if PY3:
            justCompile.extend(skipPY3)

        expectedBytecode = ['arcpy/arcpy1.tstl', 'arcpy/arcpy5.tstl']

        for f in os.listdir("."):
            if os.path.isdir(f):
                if ((os.getenv("TRAVIS") == "TRUE") and
                        (os.getenv("SUBTASK") != "JUSTCOMPILE") and (f in justCompile)):
                    continue
                if ((os.getenv("TRAVIS") == "TRUE") and
                        (os.getenv("SUBTASK") == "JUSTCOMPILE") and (f not in justCompile)):
                    continue
                if ((os.getenv("TRAVIS") == "TRUE") and
                        (os.getenv("SUBTASK") == "SMALL") and (f in noSmallcheck)):
                    continue
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
                    self.assertEqual(r, 0)
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
                        self.assertTrue((f + "/" + t) in expectedBytecode)
                        continue
                    if (noTests or (f in justCompile) or
                        ((os.getenv("TRAVIS") == "TRUE") and
                         (os.getenv("SUBTASK") == "JUSTCOMPILE"))):
                        print("OK!")
                        os.remove("sut.py")
                        try:
                            os.remove("sut.pyc")
                        except OSError:
                            pass
                        continue
                    print("RUNNING", end="...")
                    sys.stdout.flush()
                    if (os.getenv("TRAVIS") != "TRUE") or (os.getenv("SUBTASK") == "NOBUGS"):
                        rtCmd = [
                            "tstl_rt",
                            "--timeout",
                            "16",
                            "--timedProgress",
                            "5",
                            "--noCheck",
                            "--uncaught",
                            "--silentSUT"]
                        start = time.time()
                        p = subprocess.Popen(rtCmd)
                        # Big timeout is for huge coverage dumps like sympy
                        while (
                                p.poll() is None) and (
                                (time.time() - start) < 300):
                            time.sleep(1)
                        self.assertNotEqual(p.poll(), None)
                        r = p.returncode
                        self.assertEqual(r, 0)
                        print("OK!")
                        sys.stdout.flush()
                    if (os.getenv("TRAVIS") != "TRUE") or (os.getenv("SUBTASK") == "FREE"):
                        rtCmd = [
                            "tstl_rt",
                            "--timeout",
                            "16",
                            "--timedProgress",
                            "5",
                            "--noCover",
                            "--output",
                            ".freefail.test",
                            "--keepLast",
                            "--silentSUT"]
                        start = time.time()
                        if f not in problemsFree:
                            with open(os.devnull, 'w') as dnull:
                                p = subprocess.Popen(rtCmd, stdout=dnull)
                        else:
                            p = subprocess.Popen(rtCmd)
                        # Big timeout is for huge coverage dumps like sympy
                        while (
                                p.poll() is None) and (
                                (time.time() - start) < 300):
                            time.sleep(1)
                        self.assertNotEqual(p.poll(), None)
                        r = p.returncode
                        if t in shouldFail:
                            self.assertEqual(r, 255)
                        self.assertTrue(r in [0, 255])
                        if r == 255:
                            rr0 = subprocess.call(["tstl_replay",
                                                   ".freefail.test"])
                            self.assertEqual(rr0, 255)
                            if t == "onestep.tstl":
                                with open(".freefail.test", 'r') as ff:
                                    self.assertEqual(len(ff.readlines()), 1)
                            rr1 = subprocess.call(["tstl_reduce",
                                                   ".freefail.full.test",
                                                   ".freesmall.test",
                                                   "--verbose",
                                                   "True"])
                            self.assertEqual(rr1, 0)
                            if t == "onestep.tstl":
                                with open(".freesmall.test", 'r') as ff:
                                    self.assertEqual(len(ff.readlines()), 1)
                            rr2 = subprocess.call(["tstl_replay",
                                                   ".freesmall.test"])
                            self.assertEqual(rr2, 255)
                    if (testSmallcheck and (f not in noSmallcheck) and
                            ((os.getenv("TRAVIS") != "TRUE") or (os.getenv("SUBTASK") == "SMALL"))):
                        scCmd = [
                            "tstl_smallcheck",
                            "--depth",
                            "2",
                            "--recursive",
                            "1",
                            "--multiple"]
                        start = time.time()
                        with open(os.devnull, 'w') as dnull:
                            p = subprocess.Popen(scCmd)
                        while (
                                p.poll() is None) and (
                                (time.time() - start) < 300):
                            time.sleep(1)
                        self.assertNotEqual(p.poll(), None)
                        r = p.returncode
                        self.assertTrue(r in [0, 255])
                        scCmd = [
                            "tstl_smallcheck",
                            "--depth",
                            "2",
                            "--recursive",
                            "1",
                            "--visited",
                            "--multiple"]
                        start = time.time()
                        with open(os.devnull, 'w') as dnull:
                            p = subprocess.Popen(scCmd)
                        while (
                                p.poll() is None) and (
                                (time.time() - start) < 300):
                            time.sleep(1)
                        self.assertNotEqual(p.poll(), None)
                        r = p.returncode
                        self.assertTrue(r in [0, 255])
                        scCmd = [
                            "tstl_smallcheck",
                            "--depth",
                            "2",
                            "--recursive",
                            "1",
                            "--visitedList",
                            "--reverse",
                            "--multiple"]
                        start = time.time()
                        with open(os.devnull, 'w') as dnull:
                            p = subprocess.Popen(scCmd)
                        while (
                                p.poll() is None) and (
                                (time.time() - start) < 300):
                            time.sleep(1)
                        self.assertNotEqual(p.poll(), None)
                        r = p.returncode
                        self.assertTrue(r in [0, 255])
                    os.remove("sut.py")
                    try:
                        os.remove("sut.pyc")
                    except OSError:
                        pass
                os.chdir("..")
                sys.stdout.flush()
