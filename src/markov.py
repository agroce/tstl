from __future__ import print_function

import sys
import os

# Appending current working directory to sys.path
# So that user can run randomtester from the directory where sut.py is located
current_working_dir = os.getcwd()
sys.path.append(current_working_dir)

if not "--help" in sys.argv:
    import sut as SUT

def main():

    if "--help" in sys.argv:
        print("Usage:  tstl_markov <outfile> <prefix size> <test files> [--notRaw]")
        print("Options:")
        print(" --notRaw:      corpus files are not raw TSTL tests, but action classes")
        sys.exit(0)
    
    sut = SUT.sut()
    classes = []
    nacts = len(sut.actions())
    for a in sut.actions():
        if sut.actionClass(a) not in classes:
            classes.append(sut.actionClass(a))

    #print len(classes)        

    n = int(sys.argv[2])
    outfile = sys.argv[1]
    corpfiles = sys.argv[3:]
    corpfiles = [x for x in corpfiles if x != "--notRaw"]

    tests = []
    test = []

    for f in corpfiles:
        for l in open(f):
            if "--notRaw" in sys.argv:
                test.append(l[:-1])
            else:
                test.append(sut.actionClass(sut.playable(l[:-1])))
        if test != []:
            tests.append(test)
            test = []

    chains = {}

    for t in tests:
        for pos in range(n+1,len(t)):
            prefix = tuple(t[pos-n:pos])
            #print prefix,"==>",t[pos]
            if prefix not in chains:
                chains[prefix] = []
            chains[prefix].append(t[pos])

    mout = open(outfile,'w')
    mout.write(str(n)+"\n")

    for c in chains:
            print("PREFIX:",c)
            mout.write("START CLASS\n")
            for ac in c:
                mout.write(ac+"\n")
            mout.write("END CLASS\n")
            counts = {}
            total = 0.0
            for suffix in chains[c]:
                    total += 1
                    if suffix not in counts:
                            counts[suffix] = 0
                    counts[suffix] += 1
            for suffix in counts:
                    print(suffix,counts[suffix]/total)
                    mout.write(str(counts[suffix]/total) + " %%%% "+suffix+"\n")

    mout.close()
