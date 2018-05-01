from __future__ import print_function
import os
import subprocess
import glob
from unittest import TestCase


class TestAFL(TestCase):
    def test_AFL(self):
        dnull = open(os.devnull, 'w')

        os.chdir("examples/hypothesis_heaps")

        r = subprocess.call(["tstl", "heaps.tstl"], stdout=dnull)
        self.assertEqual(r, 0)

        r = subprocess.call(
            ["tstl_afl_fuzz", "--corpusBudget", "30", "--timeout", "300"], stdout=dnull)
        self.assertEqual(r, 0)

        self.assertTrue(glob.glob("afltest.*") != [])

        os.chdir("../..")
