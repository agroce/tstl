import sys
import sut as SUT
import subprocess
import time

infile = sys.argv[1]
outfile = sys.argv[2]
simpfile = sys.argv[3]

print "REDUCING",infile,"TO",outfile,"THEN NORMALIZING TO",simpfile

def sandboxReplay(test):
    print "ATTEMPTING SANDBOX REPLAY WITH",len(test),"STEPS"
    tmptest = open("tmptest.txt",'w')
    for s in test:
        tmptest.write(s[0] + "\n")
    tmptest.close()
    start = time.time()
    subprocess.call(["python","../../utilities/replay.py","tmptest.txt"])
    print "ELAPSED:",time.time()-start
    for l in open("replay.out"):
        if "TEST REPLAYED SUCCESSFULLY" in l:
            print "TEST SUCCEEDS"
            return False
    print "TEST FAILS"
    bestreduce = open("bestreduce.txt",'w')
    for l in open("tmptest.txt"):
        bestreduce.write(l)
    bestreduce.close()
    return True

t = SUT.sut()

print "READING TEST CASE..."

test = []
for l in open(infile):
    name = l[:-1]
    test.append(t.playable(name))

print "REDUCING..."

reduced = t.reduce(test, sandboxReplay)

reduceF = open(outfile,'w')
print "REDUCED:"
i = 0
for s in reduced:
    print t.prettyName(s[0]),"# STEP",i
    reduceF.write(s[0] + "\n")
reduceF.close()

simplified = t.normalize(reduced, sandboxReplay, distLimit=4)
simpF = open(simpfile,'w')
i = 0
for s in simplified:
    print t.prettyName(s[0]),"# STEP",i
    simpF.write(s[0]+"\n")
simpF.close()

t.generalize(simplified, sandboxReplay, distLimit=4)
    
