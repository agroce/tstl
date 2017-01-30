import sut
import sys
import random
import glob

# Appending current working directory to sys.path
# So that user can run randomtester from the directory where sut.py is located
current_working_dir = os.getcwd()
sys.path.append(current_working_dir)

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

if "--prefix" in sys.argv:
    for f in glob.glob(corpfile+"*.*"):
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
