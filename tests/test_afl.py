from __future__ import print_function
import os
import subprocess
import glob
from unittest import TestCase


class TestAFL(TestCase):
    def setUp(self):
        os.chdir("examples/hypothesis_heaps")

    def tearDown(self):
        os.chdir("../..")

    def test_AFL(self):
        dnull = open(os.devnull, 'w')

        r = subprocess.call(["tstl", "heaps.tstl"], stdout=dnull)
        self.assertEqual(r, 0)

        r = subprocess.call(
            ["tstl_afl_fuzz", "--corpusBudget", "30", "--timeout", "300"])
        self.assertEqual(r, 0)

        self.assertTrue(glob.glob("afltest.*") != [])
