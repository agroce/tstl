import sys
import sut
import random
import inspect
import time

def traceLOC(frame,event,arg):
    global lastLOCs,lastFuncs,onlyFirst
    if event != "call":
        return traceLOC
    co = frame.f_code
    n = co.co_name
    if (n, co.co_filename) in lastFuncs:
        #print n,co.co_filename,"ALREADY ADDED"
        return traceLOC
    lastFuncs[(n,co.co_filename)] = True
    if co.co_filename == sut.__file__.replace(".pyc",".py"):
        #print n,"FROM SUT"
        return traceLOC
    loc = len(inspect.getsourcelines(co)[0])
    print "==>",n,co.co_filename,loc
    lastLOCs += loc
    if not onlyFirst:
        return traceLOC
    else:
        return None

SUT = sut.sut()
R = random.Random()

try:
    SUT.stopCoverage()
except:
    pass

actLOCs = {}
N = len(SUT.actions())
numClasses = len(SUT.actionClasses())
print "CONSTRUCTING ESTIMATE FOR",numClasses,"CLASSES"

start = time.time()
TIMEOUT = int(sys.argv[1])
onlyFirst = "--onlyFirst" in sys.argv

while (len(actLOCs) != numClasses) and (time.time()-start < TIMEOUT):
    act = SUT.randomEnabledPred(R,N,lambda act:SUT.actionClass(act) not in actLOCs)
    c = SUT.actionClass(act)
    if c not in actLOCs:
        print "ACTION:",c
        lastLOCs = 0
        lastFuncs = {}
        sys.settrace(traceLOC)
        SUT.safely(act)
        sys.settrace(None)
        print c,lastLOCs
        actLOCs[c] = lastLOCs
        print "NOW COMPLETED ESTIMATE FOR",len(actLOCs),"OUT OF",numClasses,"CLASSES"
        if numClasses - len(actLOCs) < 10:
            for c in SUT.actionClasses():
                if c not in actLOCs:
                    print "MISSING",c
        print "="*20
    else:
        SUT.safely(act)

print "*"*60

total = 0.0
num0 = 0

for c in SUT.actionClasses():
    if c not in actLOCs:
        actLOCs[c] = 0
    print c,actLOCs[c]
    total += actLOCs[c]
    if actLOCs[c] == 0:
        num0 += 1
        
if len(sys.argv) < 3:
    baseline = 0.2
else:
    baseline = float(sys.argv[2])

leftover = 1-baseline

P = []

for c in SUT.actionClasses():
    if actLOCs[c] == 0:
        P.append((baseline/num0,c))
    else:
        P.append(((actLOCs[c]/total)*leftover,c))

        
if not onlyFirst:
    pf = open("loc.probs",'w')
else:
    pf = open("firstloc.probs",'w')
    
for (p,a) in sorted(P,key=lambda x:x[0]):
    pf.write(a + " %%%% " + str(p) + "\n")

pf.close()
