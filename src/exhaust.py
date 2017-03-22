import sut as SUT
import sys
import random
import time
import os
import math
from collections import defaultdict

def main():
    R = random.Random()
    
    repeats = 0
    
    pid = str(os.getpid())
    
    depth = int(sys.argv[1])
    
    sut = SUT.sut()
    
    taken = defaultdict(lambda: 0)
    takenClass = defaultdict(lambda: 0)
    allTaken = defaultdict(lambda: 0)
    allTakenClass = defaultdict(lambda: 0)
    takenPath = defaultdict(lambda: 0)
    takenFull = {}

    start = time.time()
    lastEpoch = 0
    
    count = 0
    sut.standardSwarm(R)
    print sut.swarmConfig()
    totalPaths = int(math.pow(len(sut.actions()),depth))
    print totalPaths,"UPPER BOUND ON POSSIBLE TESTS"
    while count < totalPaths:
        sut.restart()
        path = []
        i = 0
        count += 1        
        while len(path) < depth:
            possible = sut.actions()
            possible = sorted(possible,
                                  key = lambda act:(
                                      allTakenClass[sut.actionClass(act)],
                                      allTaken[act[0]],
                                      takenClass[(sut.actionClass(act),i)],                                      
                                      taken[(act[0],i)]
                                      )
                                  )

            a = None
            for act in possible:
                if act[1]():
                    a = act
                    break
            a = sut.randomEnabled(R)
            if a == None:
                print "DEADLOCK!"
                break
            path.append(a)
            #takenPath[sut.captureReplay(path)] += 1
            taken[(a[0],i)] += 1            
            takenClass[(sut.actionClass(a),i)] += 1         
            allTaken[(a[0])] += 1
            allTakenClass[sut.actionClass(a)] += 1            
            ok = sut.safely(a)
            if not ok:
                print "FALIURE IN TEST",count
                sut.saveTest(path,"failure.exhaust." + pid + ".test")                
                sut.prettyPrintTest(path)
                print sut.failure()
                sys.exit(255)
            if not ("--noCheck" in sys.argv):
                okCheck = sut.check()
                if not okCheck:
                    print "PROPERTY VIOLATION IN TEST",count
                    sut.saveTest(path,"failure.exhaust." + pid + ".test")
                    sut.prettyPrintTest(path)
                    print sut.failure()
                    sys.exit(255)
            i += 1
        if ("--ultraVerbose" in sys.argv):
            print "="*25
            sut.prettyPrintTest(path)
        p = sut.captureReplay(path)
        if p in takenFull:
            repeats += 1
        takenFull[p] = True
        epoch = int((time.time()-start)/2)
        if epoch > lastEpoch:
            lastEpoch = epoch
            print time.time()-start,"ELAPSED",count,"TESTS",repeats,"REPEATS",
            if not ("--noCover" in sys.argv):
                print "[",len(sut.allStatements()),"stmts",len(sut.allBranches()),"branches ]",
            print
            if ("--verbose" in sys.argv):
                print "*"*50
                print "PATH #",count
                sut.prettyPrintTest(path)
                print
                print "COUNTS:"
                print "="*20
                for c in sorted(allTakenClass.keys(),key = lambda ac: allTakenClass[ac]):
                    print c,allTakenClass[c]
                print "="*20                
                for a in sorted(allTaken.keys(),key = lambda act: allTaken[act]):
                    print a,allTaken[a]

    print repeats,"TOTAL REPEATED TESTS",len(takenFull),"DISTINCT TESTS"

main()
