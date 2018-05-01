from __future__ import print_function
import os
import subprocess
import glob
import time
import py_compile
import sys
from unittest import TestCase

class TestExamples(TestCase):
    def test_examples(self):
        os.chdir("examples")
        
        noTests = True

        compileFailures = []
        expectedCompile = []
        bytecodeFailures = []
        expectedBytecode = ['arcpy/arcpy1.tstl','arcpy/arcpy5.tstl']
        timeoutFailures = []
        expectedTimeout = ['arrow/arrow.tstl']
        testingFailures = []
        expectedTesting = []

        justCompile = ["gmpy2","arcpy"]

        for f in os.listdir("."):
            if os.path.isdir(f):
                os.chdir(f)
                print ("="*80)
                for t in glob.glob("*.tstl"):
                    print (f+"/"+t,end=":  ")
                    print ("COMPILING",end="...")
                    sys.stdout.flush()
                    tstlCmd = ["tstl",t]
                    if "tensorflow" in f:
                        tstlCmd += ["--noReload"]
                    with open(".output",'w') as ef:
                        r = subprocess.call(tstlCmd,stdout=ef,stderr=ef)
                    if r != 0:
                        print ("FAILED TO COMPILE!")
                        with open(".output",'r') as ef:
                            print (ef.read())
                        compileFailures.append(f+"/"+t)
                        print ()
                        os.remove("sut.py")
                        continue
                    print ("COMPILING TO BYTECODE",end="...")
                    sys.stdout.flush()
                    try:
                        start = time.time()
                        py_compile.compile("sut.py",doraise=True)
                        print ("NEEDED",round(time.time()-start,2),"SECONDS",end="...")
                    except py_compile.PyCompileError as e:
                        print ("BYTECODE COMPILATION FAILED!")
                        print (e)
                        bytecodeFailures.append(f+"/"+t)
                        print ()
                        os.remove("sut.py")
                        continue
                    skipThis = False
                    for jc in justCompile:
                        if jc in f:
                            skipThis = True
                            break
                    if noTests or skipThis or (f == "c"):
                            print ("OK!")
                            os.remove("sut.py")
                            os.remove("sut.pyc")
                            continue
                    print ("RUNNING",end="...")
                    sys.stdout.flush()
                    rtCmd = ["tstl_rt","--timeout","10","--noCheck","--uncaught","--noCover"]
                    start = time.time()
                    with open(".output",'w') as ef:
                        p = subprocess.Popen(rtCmd,stdout=ef,stderr=ef)
                    while (p.poll() is None) and ((time.time()-start) < 25):
                        time.sleep(1)
                    if p.poll() is None:
                        p.terminate()
                        print ("TIMEOUT!")
                        with open(".output",'r') as ef:
                            print (ef.read())
                        timeoutFailures.append(f+"/"+t)
                    else:
                        r = p.returncode
                        if r != 0:
                            print ("FAILED TO TEST!")
                            with open(".output",'r') as ef:
                                print (ef.read())
                            testingFailures.append(f+"/"+t)
                        else:
                            print ("OK!")
                    os.remove("sut.py")
                    os.remove("sut.pyc")
                    os.remove(".output")
                os.chdir("..")
                sys.stdout.flush()

        print ("COMPILATION FAILURES:",compileFailures)
        print ("BYTECODE COMPILATION FAILURES:",bytecodeFailures)
        print ("TIMEOUTS:",timeoutFailures)
        print ("TESTING FAILURES:",testingFailures)
        self.assertTrue(sorted(compileFailures) == sorted(expectedCompile))
        self.assertTrue(sorted(bytecodeFailures) == sorted(expectedBytecode))
        # These aren't even running, so need subset
        self.assertTrue(set(timeoutFailures).issubset(set(expectedTimeout)))
        self.assertTrue(set(testingFailures).issubset(set(expectedTesting)))
