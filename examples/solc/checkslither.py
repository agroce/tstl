import glob
import subprocess
import sys
import os
import time

dnull = open(os.devnull,'w')

outputs = {}

handled = []
lastLen = 0

SHORT = 200

while True:
    gc = glob.glob("goodcontract.*.sol")
    if len(gc) > lastLen:
        print "HANDLING",len(gc)-lastLen,"NEW INPUTS..."
        lastLen = len(gc)
    else:
        time.sleep(60)
        continue

    allContracts = set([(sorted(outputs[(f,ef)],key=lambda x:len(x[1])))[0][1] for (f,ef) in outputs.keys()])

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
                subprocess.call(["python","/Users/alex/slither/slither.py","fuzz.ast.json","--solc-ast","--debug"],stdout=f,stderr=ef)
        with open("slither.out",'r') as f:
            with open("slither.err",'r') as ef:
                output = (f.read(),ef.read())
                toutput = (output[0][-SHORT:],output[1][-SHORT:])
            if toutput not in outputs:
                outputs[toutput] = [(c,input,output)]
            else:
                outputs[toutput].append((c,input,output))

    print "ANALYZED",lastLen,"TOTAL CONTRACTS"
    print

    newContracts = set([(sorted(outputs[(f,ef)],key=lambda x:len(x[1])))[0][1] for (f,ef) in outputs.keys()])

    if allContracts == newContracts:
        continue
    
    for (f,ef) in outputs:
        print "=" * 50
        print "OUTPUT:",f
        print "ERROR: ",ef
        csort = sorted(outputs[(f,ef)],key=lambda x:len(x[1]))
        if csort[0][2] != (f,ef):
            print csort[0][2]
        print "*"*20
        print "FILE:",csort[0][0]
        print len(csort[0][1]),"CHARS"
        if len(csort[0][1]) < 400:
            print "CODE:"
            print csort[0][1]
        print "*"*20
        if len(csort) > 1:
            print "ALSO:",map(lambda x:x[0],csort[1:])

    time.sleep(60)
