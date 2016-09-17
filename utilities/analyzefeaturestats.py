import glob
import sut
from statsmodels.stats.proportion import proportion_confint

sut = sut.sut()
actions = sut.actionClasses()

bData = {}
sData = {}
aData = {}

totalTests = 0

b = None
s = None
for f in glob.glob("feature.stats.*"):
    for l in open(f):
        if "TESTS:" in l:
            totalTests += int(l.split(":")[1])
        if "%%ACTCOUNT%%" in l:
            a = l.split("%%ACTCOUNT%%")[0][:-1]
            acount = int(l.split("%%ACTCOUNT%%")[1])
            if a in aData:
                aData[a] += acount
            else:
                aData[a] = acount
        if ("BRANCH:" in l) or ("STATEMENT:" in l):
            if b != None:
                if b not in bData:
                    bData[b] = [0,{}]
                bData[b][0] += count
                for a in thisData:
                    if a in bData[b][1]:
                        bData[b][1][a] += thisData[a]
                    else:
                        bData[b][1][a] = thisData[a]
            if s != None:
                if s not in sData:
                    sData[s] = [0,{}]                
                sData[s][0] += count
                for a in thisData:
                    if a in sData[s][1]:
                        sData[s][1][a] += thisData[a]
                    else:
                        sData[s][1][a] = thisData[a]                        
        if "BRANCH:" in l:             
            b = eval(l.split("BRANCH:")[1])
            s = None
            thisData = {}
        if "STATEMENT:" in l:
            s = eval(l.split("STATEMENT:")[1])
            b = None
            thisData = {}      
        if "COUNT:" in l:
            count = int(l.split(":")[1])
        if "%%%%" in l:
            a = l.split("%%%%")[0][:-1]
            acount = int(l.split("%%%%")[1])
            thisData[a] = acount

    if b != None:
        if b not in bData:
            bData[b] = [0,{}]
        bData[b][0] += count
        for a in thisData:
            if a in bData[b][1]:
                bData[b][1][a] += thisData[a]
            else:
                bData[b][1][a] = thisData[a]
    if s != None:
        if s not in sData:
            sData[s] = [0,{}]                
        sData[s][0] += count
        for a in thisData:
            if a in sData[s][1]:
                sData[s][1][a] += thisData[a]
            else:
                sData[s][1][a] = thisData[a]          

print totalTests,"TESTS"    
print len(bData),"BRANCHES"
print len(sData),"STATEMENTS"

print "BRANCHES:"

totalS = 0
totalT = 0
totalI = 0
allCovered = 0
tooFew = 0

for b in bData:
    nS = 0
    nT = 0
    nI = 0
    bCount = bData[b][0]
    if bCount == totalTests:
        print "COVERED BY ALL TESTS, IGNORING"
        allCovered += 1
        continue
    if bCount < 4:
        print "TOO FEW HITS TO DETERMINE TRIGGERS/SUPPRESSORS"
        tooFew += 1
        continue
    print "="*50
    print "BRANCH:",b,bCount    
    for a in actions:
        if a in bData[b][1]:
            ahits = bData[b][1][a]
        else:
            ahits = 0
        amisses = bCount - ahits
        (l,h) = proportion_confint(ahits,bCount,0.05,method='wilson')
        if a not in aData:
            arate = 0.0
        else:
            arate = aData[a]/float(totalTests)
        if (arate == 1.0):
            pass
        elif (l > arate):
            print "ACTION:",a,ahits,amisses,"WILSON:",(l,h),arate,
            print "TRIGGER"
            nT += 1
            totalT += 1
        elif (h < arate):
            print "ACTION:",a,ahits,amisses,"WILSON:",(l,h),arate,
            print "SUPPRESSOR"
            nS += 1
            totalS += 1
        else:
            nI += 1
            totalI += 1
    print nT,"TRIGGERS",nS,"SUPPRESSORS",nI,"IRRELEVANT"

print "*" * 50
print "COVERED BY ALL",allCovered
print "TOO FEW HITS",tooFew
print "REMAINING:",len(bData)-(allCovered+tooFew)
print totalT/float(len(bData)-(allCovered+tooFew)),"MEAN TRIGGERS"
print totalS/float(len(bData)-(allCovered+tooFew)),"MEAN SUPPRESSORS"

print "* " * 30

print "STATEMENTS:"

totalS = 0
totalT = 0
totalI = 0
allCovered = 0
tooFew = 0

for b in sData:
    nS = 0
    nT = 0
    nI = 0
    bCount = sData[b][0]
    if bCount == totalTests:
        print "COVERED BY ALL TESTS, IGNORING"
        allCovered += 1
        continue
    if bCount < 4:
        print "TOO FEW HITS TO DETERMINE TRIGGERS/SUPPRESSORS"
        tooFew += 1
        continue
    print "="*50
    print "STATEMENT:",b,bCount    
    for a in actions:
        if a in sData[b][1]:
            ahits = sData[b][1][a]
        else:
            ahits = 0
        amisses = bCount - ahits
        (l,h) = proportion_confint(ahits,bCount,0.05,method='wilson')
        if a not in aData:
            arate = 0.0
        else:
            arate = aData[a]/float(totalTests)
        if (arate == 1.0):
            pass
        elif (l > arate):
            print "ACTION:",a,ahits,amisses,"WILSON:",(l,h),arate,
            print "TRIGGER"
            nT += 1
            totalT += 1
        elif (h < arate):
            print "ACTION:",a,ahits,amisses,"WILSON:",(l,h),arate,
            print "SUPPRESSOR"
            nS += 1
            totalS += 1
        else:
            nI += 1
            totalI += 1
    print nT,"TRIGGERS",nS,"SUPPRESSORS",nI,"IRRELEVANT"

print "*" * 50
print "COVERED BY ALL",allCovered
print "TOO FEW HITS",tooFew
print "REMAINING:",len(sData)-(allCovered+tooFew)
print totalT/float(len(sData)-(allCovered+tooFew)),"MEAN TRIGGERS"
print totalS/float(len(sData)-(allCovered+tooFew)),"MEAN SUPPRESSORS"
print totalI/float(len(sData)-(allCovered+tooFew)),"MEAN IRRELEVANT"
