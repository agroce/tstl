from __future__ import print_function
import os
import subprocess
import glob
import time
import py_compile
import sys
from unittest import TestCase

class TestAVL(TestCase):
    def test_examples(self):
        dnull = open(os.devnull,'w')
        
        os.chdir("examples/avl")
        
        r = subprocess.call(["tstl","avlbuggy.tstl"])
        self.assertTrue(r == 0)

        r = subprocess.call(["tstl_rt","--noCover"])

        self.assertTrue(r == 256)

        
