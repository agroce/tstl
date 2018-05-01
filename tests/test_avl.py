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
        
        os.chdir("examples/AVL")
        
        r = subprocess.call(["tstl","avlbuggy.tstl"])
        self.assertEqual(r,0)

        r = subprocess.call(["tstl_rt","--noCover","--output",".avltest"])
        self.assertEqual(r,255)

        r = subprocess.call(["tstl_rt","--swarm","--output",".avltest"])
        self.assertEqual(r,255)

        r = subprocess.call(["tstl_rt","--exploit","0.8","--Pmutate","0.8","--output",".avltest"])
        self.assertEqual(r,255)

        r = subprocess.call(["tstl_rt","--multiple","--timeout","60","--output",".avltest"])
        self.assertEqual(r,255)

        r = subprocess.call(["tstl_rt","--multiple","--timeout","60","--noCover","--normalize","--output",".avltest"])
        self.assertEqual(r,255)                                

        for f in glob.glob(".avltest.*.test*"):
            os.remove(f)
        
        os.chdir("../..")
        
