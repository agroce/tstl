import sys
import sut as SUT
import subprocess

infile = sys.argv[1]
outfile = sys.argv[2]
simpfile = sys.argv[3]

print "REDUCING",infile,"TO",outfile,"THEN SIMPLIFYING TO",simpfile

def sandboxReplay(test):
    tmptest = open("tmptest.txt",'w')
    for s in test:
        tmptest.write(s[0] + "\n")
    tmptest.close()
    outf = open("tmpout",'w')
    subprocess.call(["C:\\Python27\\ArcGIS10.3\\python.exe","replay.py","tmptest.txt"], stdout = outf)
    outf.close()
    for l in open("tmpout"):
        if "TEST REPLAYED SUCCESSFULLY" in l:
            return False
    return True

t = SUT.sut()

test = []
for l in open(infile):
    name = l[:-1]
    if name == "<<RESTART>>":
        test.append(name,lambda x:True,lambda x:True)
    else:
        test.append(t.playable(name))

reduced = t.reduce(test, sandboxReplay)

print "REDUCED:"
i = 0
for s in reduced:
    print "STEP",i,s[0]

simplified = t.simplify(test, sandboxReplay)
i = 0
for s in simplified:
    print "STEP",i,s[0]
