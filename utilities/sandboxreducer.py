import sys
import sut as SUT
import subprocess

infile = "fulltest.txt"
outfile = "reduced.txt"
simpfile = "simplified.txt"

print "REDUCING",infile,"TO",outfile,"THEN SIMPLIFYING TO",simpfile

def sandboxReplay(test):
    print "ATTEMPTING SANDBOX REPLAY WITH",len(test),"STEPS"
    tmptest = open("tmptest.txt",'w')
    for s in test:
        tmptest.write(s[0] + "\n")
    tmptest.close()
    subprocess.call(["C:\\Python27\\ArcGIS10.3\\python.exe","replay.py","tmptest.txt"])
    for l in open("replay.out"):
        if "TEST REPLAYED SUCCESSFULLY" in l:
            print "TEST FAILS"
            return False
    print "TEST SUCCEEDS"
    return True

t = SUT.sut()

test = []
for l in open(infile):
    name = l[:-1]
    if name == "<<RESTART>>":
        test.append((name,lambda x:True,lambda x:True))
    else:
        test.append(t.playable(name))

reduced = t.reduce(test, sandboxReplay)

reduceF = open(outfile,'w')
print "REDUCED:"
i = 0
for s in reduced:
    print "STEP",i,s[0]
    reduceF.write(s[0] + "\n")
reduceF.close()

simplified = t.simplify(test, sandboxReplay)
simpF = open(simpfile,'w')
i = 0
for s in simplified:
    print "STEP",i,s[0]
    simpF.write(s[0]+"\n")
simpF.close()
