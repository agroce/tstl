import glob
import subprocess
import sys
import os
import time

dnull = open(os.devnull,'w')

outputs = {}

handled = []
lastLen = 0

while True:
    gc = glob.glob("goodcontract.*.sol")
    if len(gc) > lastLen:
        print "HANDLING",len(gc)-lastLen,"NEW INPUTS..."
        lastLen = len(gc)
    else:
        time.sleep(60)
        continue

    for c in gc:
        if c in handled:
            continue
        else:
            handled.append(c)
        with open(c) as f:
            input = f.read()
        with open("fuzz.ast.json",'w') as f:
            subprocess.call(["solc",c,"--ast-json"],stdout=f,stderr=dnull)
        with open("slither.out",'w') as f:
            with open("slither.err",'w') as ef:        
                subprocess.call(["python","slither.py","fuzz.ast.json","--solc-ast"],stdout=f,stderr=ef)
        with open("slither.out",'r') as f:
            with open("slither.err",'r') as ef:
                output = (f.read(),ef.read())
            if output not in outputs:
                outputs[output] = [(c,input)]
            else:
                outputs[output].append((c,input))

    print "ANALYZED",lastLen,"TOTAL CONTRACTS"
    print
                
    for (f,ef) in outputs:
        print "=" * 50
        print "OUTPUT:",f
        print "ERROR: ",ef
        csort = sorted(outputs[(f,ef)],key=lambda x:len(x[1]))
        print "*"*20
        print "FILE:",csort[0][0]
        print csort[0][1]
        print "*"*20
        if len(csort) > 1:
            print "ALSO:",map(lambda x:x[0],csort[1:])

    time.sleep(60)
