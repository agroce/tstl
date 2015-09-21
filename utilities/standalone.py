import sys
import sut as SUT

testFile = sys.argv[1]
sutFile = sys.argv[2]
outFile = sys.argv[3]

checkProps = "--check" in sys.argv

t = SUT.sut()

def globalCheck(str):
    if " # CHECK POOL INIT" not in str:
        return str
    condBegin = str.find("(")
    theCheck = str[condBegin+1:str.find(" != None):")]
    strNew = str[:condBegin+1] + '"' + theCheck + '"' + str[str.find(" != None):"):]
    strNew = strNew.replace(" != None"," in globals()")
    strNew = strNew.replace("# CHECK POOL INIT","")
    return strNew
    
outf = open(outFile,'w')
startPrelim = False
startCheck = False
for l in open(sutFile):
    if "END STANDALONE CODE" in l:
        startPrelim = False
    if "END CHECK CODE" in l:
        startCheck = False
    if startPrelim:
        outf.write(l)
    if startCheck:
        outf.write(globalCheck(t.prettyName(l.replace("# GLOBAL ", "global "))))
    if "BEGIN STANDALONE CODE" in l:
        startPrelim = True
    if checkProps and ("BEGIN CHECK CODE" in l):
        startCheck = True
        outf.write("\n\ndef check():\n")
    

outf.write("\n\n")
    
for l in open(testFile):
    outf.write(t.prettyName(l[:-1]) + "\n")
    if checkProps:
        outf.write("check()\n")

outf.close()
