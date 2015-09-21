import sys
import sut as SUT

testFile = sys.argv[1]
sutFile = sys.argv[2]
outFile = sys.argv[3]

outf = open(outFile,'w')
startWrite = False
for l in open(sutFile):
    if "END STANDALONE CODE" in l:
        break
    if startWrite:
        outf.write(l)
    if "BEGIN STANDALONE CODE" in l:
        startWrite = True

outf.write("\n\n")
    
t = SUT.sut()
    
for l in open(testFile):
    outf.write(t.prettyName(l[:-1]) + "\n")

outf.close()
