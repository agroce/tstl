import sut
import sys
import random

sut = sut.sut()
classes = []
nacts = len(sut.actions())
for a in sut.actions():
    if sut.actionClass(a) not in classes:
        classes.append(sut.actionClass(a))

#print len(classes)        

n = int(sys.argv[1])
corpfile = sys.argv[2]
outfile = sys.argv[3]

tests = []
test = []
for l in open(corpfile):
    if ("="*50) in l:
        tests.append(test)
        test = []
    test.append(l[:-1])
#print len(tests)
#print tests[0]

chains = {}

for t in tests:
    for pos in xrange(n+1,len(t)):
        prefix = tuple(t[pos-n:pos])
        #print prefix,"==>",t[pos]
        if prefix not in chains:
            chains[prefix] = []
        chains[prefix].append(t[pos])

mout = open(outfile,'w')
mout.write(str(n)+"\n")
        
for c in chains:
        print "PREFIX:",c
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
                print suffix,counts[suffix]/total
                mout.write(str(counts[suffix]/total) + " %%%% "+suffix+"\n")

mout.close()
