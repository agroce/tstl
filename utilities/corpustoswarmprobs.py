import sut
import sys
import random
import glob

sut = sut.sut()
classes = []
nacts = len(sut.actions())
for a in sut.actions():
    if sut.actionClass(a) not in classes:
        classes.append(sut.actionClass(a))

#print len(classes)        

corpfile = sys.argv[1]
outfile = sys.argv[2]

tests = []
test = []

if "--prefix" in sys.argv:
    for f in glob.glob(corpfile+".*"):
        for l in open(f):
            if "--raw" not in sys.argv:
                test.append(l[:-1])
            else:
                test.append(sut.actionClass(sut.playable(l[:-1])))
        if test != []:
            tests.append(test)
            test = []
else:
    for l in open(corpfile):
        if ("="*50) in l:
            tests.append(test)
            test = []
        if "--raw" not in sys.argv:
            test.append(l[:-1])
        else:
            test.append(sut.actionClass(sut.playable(l[:-1])))
#print len(tests)
#print tests[0]

totals = {}
for c in classes:
    totals[c] = 0

for t in tests:
    for c in classes:
        if c in t:
            totals[c] += 1

mout = open(outfile,'w')
        
for c in classes:
    P = totals[c] / (len(tests) * 1.0)
    mout.write(c + " %%%% " + str(P) + "\n")

mout.close()
