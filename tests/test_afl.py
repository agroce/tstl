from __future__ import print_function
import os
import subprocess
import glob
from unittest import TestCase


class TestAFL(TestCase):
    def setUp(self):
        os.chdir("examples/AVL")

    def tearDown(self):
        os.chdir("../..")

    def test_AFL(self):
        dnull = open(os.devnull, 'w')

        r = subprocess.call(["tstl", "avlbuggy.tstl"], stdout=dnull)
        self.assertEqual(r, 0)

        r = subprocess.call(
            ["tstl_afl_fuzz", "--corpusBudget", "15", "--timeout", "20", "--quiet", "--persist"], stdout=dnull)
        self.assertEqual(r, 0)

        self.assertTrue(glob.glob("aflfail.*") != [])

        for f in glob.glob("aflfail.*"):
            os.remove(f)

        r = subprocess.call(
            ["tstl_afl_fuzz", "--corpusBudget", "0", "--timeout", "20", "--quiet"])
        self.assertEqual(r, 0)

        self.assertTrue(glob.glob("aflfail.*") != [])
