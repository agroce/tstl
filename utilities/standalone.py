import sys
import sut as SUT

testFile = sys.argv[1]
sutFile = sys.argv[2]
outFile = sys.argv[3]

checkProps = "--check" in sys.argv
checkRefs = "--refs" in sys.argv

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
startReload = False
startInit = False

reloadCode = []
initCode = []

for l in open(sutFile):
    if "END STANDALONE CODE" in l:
        startPrelim = False
    if "END CHECK CODE" in l:
        startCheck = False
    if "END RELOAD CODE" in l:
        startReload = False
    if "END INITIALIZATION CODE" in l:
        startInit = False
    if startPrelim:
        outf.write(l)
    if startCheck:
        outf.write(globalCheck(t.prettyName(l.replace("# GLOBAL ", "global "))))
    if startReload:
        reloadCode.append(l.lstrip())
    if startInit:
        initCode.append(l.lstrip())
    if "BEGIN STANDALONE CODE" in l:
        startPrelim = True
    if checkProps and ("BEGIN CHECK CODE" in l):
        startCheck = True
        outf.write("\n\ndef check():\n")
    if "BEGIN RELOAD CODE" in l:
        startReload = True
    if "BEGIN INITIALIZATION CODE" in l:
        startInit = True
    

outf.write("\n\n")

for i in initCode:
    outf.write(t.prettyName(i))

outf.write("\n\n")

for l in open(testFile):
    if l == "<<RESTART>>":
        outf.write("\n# RESTART\n\n")
        for r in reloadCode:
            outf.write(r)
        for i in initCode:
            outf.write(i)
    name = l[:-1]
    if t.getPreCode(name) != None:
        for p in t.getPreCode(name):
            outf.write(t.prettyName(p) + "\n")
    if t.getOkExceptions(name) == "":
        outf.write(t.prettyName(name) + "\n")
    else:
        outf.write("try:\n")
        outf.write("  " + t.prettyName(name) + "\n")
        outf.write("except (" + t.getOkExceptions(name) + "):\n")
        outf.write("  pass\n")
    if t.getPropCode(name) != None:
        outf.write("assert " + t.prettyName(t.getPropCode(name)) + "\n")
    if checkRefs:
        if t.getRefCode(name) != None:
            for r in t.getRefCode(name):
                outf.write(t.prettyName(r) + "\n")        
    if checkProps:
        outf.write("check()\n")


outf.write('\n\nprint "TEST COMPLETED SUCCESSFULLY"\n')
outf.close()
