from __future__ import print_function
import os
import subprocess
import glob
from unittest import TestCase


class TestHypothesisHeap(TestCase):
    def setUp(self):
        os.chdir("examples/hypothesis_heaps")

    def tearDown(self):
        os.chdir("../..")

    def test_hypothesis_heap(self):
        if (os.getenv("TRAVIS") == "TRUE") and (os.getenv("TASK") != "HYPOTHESIS"):
            return

        dnull = open(os.devnull, 'w')

        r = subprocess.call(["tstl", "heaps.tstl"], stdout=dnull)
        self.assertEqual(r, 0)

        r = subprocess.call(
            ["tstl_rt", "--noCover", "--output", ".heap.test"])
        self.assertEqual(r, 255)

        r = subprocess.call(["tstl_replay", ".heap.test"], stdout=dnull)
        self.assertEqual(r, 255)

        r = subprocess.call(["tstl_reduce", ".heap.test",
                             ".heap.norm.test"], stdout=dnull)
        self.assertEqual(r, 0)

        r = subprocess.call(
            ["tstl_replay", ".heap.norm.test", "--verbose"], stdout=dnull)
        self.assertEqual(r, 255)

        r = subprocess.call(
            ["tstl_generalize", ".heap.norm.test"], stdout=dnull)
        self.assertEqual(r, 0)

        r = subprocess.call(
            ["tstl_standalone", ".heap.norm.test", ".heap.norm.py"], stdout=dnull)
        self.assertEqual(r, 0)

        r = subprocess.call(["python", ".heap.norm.py"],
                            stdout=dnull, stderr=dnull)
        self.assertEqual(r, 1)

        for f in glob.glob(".heap*"):
            os.remove(f)
