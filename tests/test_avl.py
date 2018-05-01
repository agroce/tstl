from __future__ import print_function
import os
import subprocess
import glob
from unittest import TestCase


class TestAVL(TestCase):
    def setUp(self):
        os.chdir("examples/AVL")

    def tearDown(self):
        os.chdir("../..")

    def test_AVL(self):
        dnull = open(os.devnull, 'w')

        r = subprocess.call(["tstl", "avlbuggy.tstl"], stdout=dnull)
        self.assertEqual(r, 0)

        r = subprocess.call(
            ["tstl_rt", "--noCover", "--output", ".avltest"], stdout=dnull)
        self.assertEqual(r, 255)

        r = subprocess.call(["tstl_replay", ".avltest"], stdout=dnull)
        self.assertEqual(r, 255)

        r = subprocess.call(
            ["tstl_reduce", ".avltest", ".avltest.norm"], stdout=dnull)
        self.assertEqual(r, 0)

        r = subprocess.call(
            ["tstl_replay", ".avltest.norm", "--verbose"], stdout=dnull)
        self.assertEqual(r, 255)

        r = subprocess.call(["tstl_generalize", ".avltest.norm"], stdout=dnull)
        self.assertEqual(r, 0)

        r = subprocess.call(
            ["tstl_standalone", ".avltest.norm", ".avltest.norm.py"], stdout=dnull)
        self.assertEqual(r, 0)

        r = subprocess.call(["python", ".avltest.norm.py"],
                            stdout=dnull, stderr=dnull)
        self.assertEqual(r, 1)

        r = subprocess.call(
            ["tstl_rt", "--swarm", "--output", ".avltest"], stdout=dnull)
        self.assertEqual(r, 255)

        r = subprocess.call(["tstl_rt",
                             "--exploit",
                             "0.8",
                             "--Pmutate",
                             "0.8",
                             "--output",
                             ".avltest"],
                            stdout=dnull)
        self.assertEqual(r, 255)

        r = subprocess.call(["tstl_rt",
                             "--multiple",
                             "--timeout",
                             "60",
                             "--output",
                             ".avltest"],
                            stdout=dnull)
        self.assertEqual(r, 255)

        r = subprocess.call(["tstl_rt",
                             "--multiple",
                             "--timeout",
                             "60",
                             "--noCover",
                             "--normalize",
                             "--output",
                             ".avltest"],
                            stdout=dnull)
        self.assertEqual(r, 255)

        r = subprocess.call(
            ["tstl_regress .avltest*"],
            shell=True,
            stdout=dnull)
        self.assertEqual(r, 255)

        r = subprocess.call(["tstl_triage", ".avltest*"], stdout=dnull)
        self.assertEqual(r, 0)

        r = subprocess.call(["tstl", "avlnew.tstl"], stdout=dnull)
        self.assertEqual(r, 0)

        r = subprocess.call(["tstl_rt", "--timeout", "30"], stdout=dnull)
        self.assertEqual(r, 0)

        r = subprocess.call(
            ["tstl_rt", "--timeout", "30", "--noCover"], stdout=dnull)
        self.assertEqual(r, 0)

        r = subprocess.call(
            ["tstl_rt", "--timeout", "30", "--swarm"], stdout=dnull)
        self.assertEqual(r, 0)

        r = subprocess.call(["tstl_rt",
                             "--timeout",
                             "30",
                             "--exploit",
                             "0.8",
                             "--Pmutate",
                             "0.8",
                             "--trackMaxCoverage",
                             ".avltest.maxcov"],
                            stdout=dnull)
        self.assertEqual(r, 0)

        r = subprocess.call(["tstl_standalone",
                             ".avltest.maxcov",
                             ".avltest.maxcov.py",
                             "--regression",
                             "--verbose"],
                            stdout=dnull)
        self.assertEqual(r, 0)

        r = subprocess.call(["python", ".avltest.maxcov.py"],
                            stdout=dnull)
        self.assertEqual(r, 0)

        r = subprocess.call(
            ["tstl_regress .avltest*"],
            shell=True,
            stdout=dnull)
        self.assertEqual(r, 0)

        for f in glob.glob(".avltest*"):
            os.remove(f)

        os.remove("coverage.out")
