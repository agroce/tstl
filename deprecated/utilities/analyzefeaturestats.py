import glob
import sut
import subprocess
import scipy
from statsmodels.stats.proportion import proportion_confint

sut = sut.sut()
actions = sut.actionClasses()

confLevel = 0.05

def featureAnalysis(data, name, confLevel, totalTests):
    totalS = 0
    totalT = 0
    totalI = 0
    allCovered = 0
    tooFew = 0

    nS = []
    nT = []
    nI = []
    
    for t in data:

        tCount = data[t][0]
        print "="*50
        print name + ":",t,tCount            
        if tCount == totalTests:
            print "COVERED BY ALL TESTS, IGNORING"
            allCovered += 1
            continue
        if tCount < 4:
            print "INSUFFICIENT HITS TO DETERMINE TRIGGERS/SUPPRESSORS"
            tooFew += 1
            continue
        nS.append(0)
        nT.append(0)
        nI.append(0)        
        triggers = []
        suppressors = []
        for a in actions:
            if a in data[t][1]:
                ahits = data[t][1][a]
            else:
                ahits = 0
            amisses = tCount - ahits
            (l,h) = proportion_confint(ahits,tCount,confLevel,method='wilson')
            if a not in aData:
                arate = 0.0
            else:
                arate = aData[a]/float(totalTests)
            if (arate == 1.0):
                pass
            elif (l > arate):
                triggers.append((a,ahits,amisses,(l,h),arate))
                nT[-1] += 1
                totalT += 1
            elif (h < arate):
                suppressors.append((a,ahits,amisses,(l,h),arate))                
                nS[-1] += 1
                totalS += 1
            else:
                nI[-1] += 1
                totalI += 1
        triggers = sorted(triggers, key=lambda ((a,ahits,amisses,(l,h),arate)) : l-arate, reverse=True)
        suppressors = sorted(suppressors, key=lambda ((a,ahits,amisses,(l,h),arate)) : arate-h, reverse=True)        
        for (a,ahits,amisses,(l,h),arate) in triggers:
            print "+",a,ahits,amisses,"WILSON:",(l,h),arate,"STRENGTH:",l-arate
        for (a,ahits,amisses,(l,h),arate) in suppressors:
            print "-",a,ahits,amisses,"WILSON:",(l,h),arate,"STRENGTH:",arate-h          
        print nT[-1],"TRIGGERS",nS[-1],"SUPPRESSORS",nI[-1],"IRRELEVANT"

    print "*" * 50
    print "COVERED BY ALL",allCovered
    print "TOO FEW HITS TO ANALYZE",tooFew
    print "REMAINING:",len(data)-(allCovered+tooFew)
    print scipy.mean(nT),scipy.median(nT),"MEAN/MEDIAN TRIGGERS"
    print scipy.mean(nS),scipy.median(nS),"MEAN/MEDIAN SUPPRESSORS"
    print scipy.mean(nI),scipy.median(nI),"MEAN/MEDIAN IRRELEVANT"        


bData = {}
sData = {}
aData = {}

totalTests = 0

b = None
s = None
for f in glob.glob("feature.stats.*"):
    rf = f
    if ".gz" in f:
        needsZipped = True
        subprocess.call(["gunzip",f])
        rf = f.replace(".gz","")
    for l in open(rf):
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
    subprocess.call(["gzip",rf])
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
featureAnalysis(bData,"BRANCH",confLevel,totalTests)

print
print "* " * 30

print "STATEMENTS:"
featureAnalysis(sData,"STATEMENT",confLevel,totalTests)
