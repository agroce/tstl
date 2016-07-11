import scipy
import scipy.stats

import sut
import glob

def pruneByFailure(list,fails,f):
    i = 0
    pruned = []
    for v in list:
        if fails[i] == f:
            pruned.append(list[i])
        i += 1
    return pruned

sut = sut.sut()

failInOrder = []
lengths = {}
times = {}
actions = {}
failures = {}

allFullTests = {}
allReducedTests = {}
allNormalizedTests = {}

allFullActions = []
allReducedActions = []
allNormalizedActions = []

for s in [lengths,times,actions]:
    s["reduced"] = []
    s["normalized"] = []
    s["full"] = []

for t in ["full","reduced","normalized"]:
    failures[t] = {}

for base in glob.glob("*.normalized"):
    for l in open(base.replace("normalized","failure")):
        fail = l[:-1]
    for ft in ["full","reduced","normalized"]:
        if fail not in failures[ft]:
            failures[ft][fail] = []
    failInOrder.append(fail)
    t = sut.loadTest(base.replace("normalized","full"))
    allFullTests[sut.captureReplay(t)] = True
    if t not in failures["full"][fail]:
        failures["full"][fail].append(t)
    r = sut.loadTest(base.replace("normalized","reduced"))
    allReducedTests[sut.captureReplay(r)] = True    
    if r not in failures["reduced"][fail]:
        failures["reduced"][fail].append(r)    
    n = sut.loadTest(base)
    allNormalizedTests[sut.captureReplay(n)] = True    
    if n not in failures["normalized"][fail]:
        failures["normalized"][fail].append(n)
    for s in t:
        if sut.actionClass(s) not in allFullActions:
            allFullActions.append(sut.actionClass(s))
    lengths["full"].append(len(t))
    actions["full"].append(len(set(map(sut.actionClass,t))))
    times["full"].append(0.0)
    for s in r:
        if sut.actionClass(s) not in allReducedActions:
            allReducedActions.append(sut.actionClass(s))    
    lengths["reduced"].append(len(r))
    actions["reduced"].append(len(set(map(sut.actionClass,r))))
    for s in n:
        if sut.actionClass(s) not in allNormalizedActions:
            allNormalizedActions.append(sut.actionClass(s))    
    lengths["normalized"].append(len(n))
    actions["normalized"].append(len(set(map(sut.actionClass,n))))
    for l in open(base.replace("normalized","reducetime")):
        rtime = float(l)
    times["reduced"].append(rtime)        
    for l in open(base.replace("normalized","normtime")):
        ntime = float(l)          
    times["normalized"].append(ntime)

print len(lengths["full"]),"TESTS"
    
for stat in [("LENGTH",lengths),("ACTIONS",actions),("TIME",times)]:
    print "="*50
    print stat[0]
    for st in ["reduced","normalized","full"]:
        print st,"MEAN:",scipy.mean(stat[1][st]),"MEDIAN:",scipy.median(stat[1][st]),"SDEV:",scipy.std(stat[1][st])
        for st2 in ["reduced","normalized","full"]:
            if st2 > st:
                print st,"VS",st2,
                print scipy.stats.wilcoxon(stat[1][st],stat[1][st2])
print "="*50
print

print len(failures["full"]),"FAILURES"
for f in failures["full"]:
    print "*"*50
    print "full",len(failures["full"][f]),
    print "reduced",len(failures["reduced"][f]),
    print "normalized",len(failures["normalized"][f]),":",f
    if len(failures["full"][f]) > 1:
        prunedLengths = {}
        prunedActions = {}
        for rtype in ["full","reduced","normalized"]:
            prunedLengths[rtype] = pruneByFailure(lengths[rtype],failInOrder,f)
            prunedActions[rtype] = pruneByFailure(actions[rtype],failInOrder,f)
            print rtype, "LENGTH MEAN:",scipy.mean(prunedLengths[rtype]),"MEDIAN:",scipy.median(prunedLengths[rtype]),"MIN:",min(prunedLengths[rtype]),"MAX:",max(prunedLengths[rtype]), "STD:", scipy.std(prunedLengths[rtype])        
            print rtype, "ACTION MEAN:",scipy.mean(prunedActions[rtype]),"MEDIAN:",scipy.median(prunedActions[rtype]),"MIN:",min(prunedActions[rtype]),"MAX:",max(prunedActions[rtype]), "STD:", scipy.std(prunedActions[rtype])
    else:
        prunedLengths = {}
        prunedActions = {}
        for rtype in ["full","reduced","normalized"]:
            prunedLengths[rtype] = pruneByFailure(lengths[rtype],failInOrder,f)
            prunedActions[rtype] = pruneByFailure(actions[rtype],failInOrder,f)
            print rtype, "LENGTH:",scipy.mean(prunedLengths[rtype]),
            print "ACTION:",scipy.mean(prunedActions[rtype]),"  ",
        print
    if scipy.mean(prunedLengths["reduced"]) == scipy.mean(prunedLengths["normalized"]):
        print "NO MEAN REDUCTION IN LENGTH"
    if scipy.mean(prunedActions["reduced"]) == scipy.mean(prunedActions["normalized"]):
        print "NO MEAN REDUCTION IN ACTIONS"        


print "="*50
print
print len(allFullTests),"FULL TESTS"
print len(allReducedTests),"REDUCED TESTS"
print len(allNormalizedTests),"NORMALIZED TESTS"


print "="*50    
print
print len(allFullActions),"ACTIONS IN FULL TESTS"
print len(allReducedActions),"ACTIONS IN REDUCED TESTS"
print len(allNormalizedActions),"ACTIONS IN NORMALIZED TESTS"

print "="*50
print "REMOVED FROM FULL TO REDUCED:"
for a in allFullActions:
    if a not in allReducedActions:
        print "[[",a,"]]",
print

print
print "="*50
print "REMOVED FROM REDUCED TO NORMALIZED"
for a in allReducedActions:
    if a not in allNormalizedActions:
        print "[[",a,"]]",
print
print
