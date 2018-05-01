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
        self.assertEqual(r,0)

        r = subprocess.call(["tstl_rt","--noCover"])
        self.assertEqual(r,255)

        r = subprocess.call(["tstl_rt","--swarm"])
        self.assertEqual(r,255)

        r = subprocess.call(["tstl_rt","--exploit","0.8","--Pmutate","0.8"])
        self.assertEqual(r,255)

        r = subprocess.call(["tstl_rt","--multiple","--timeout","60"])
        self.assertEqual(r,255)                        

        os.chdir("../..")
        
