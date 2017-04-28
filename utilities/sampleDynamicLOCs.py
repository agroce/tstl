import sys
import sut
import random
import inspect
import time
import scipy

def traceLOC(frame,event,arg):
    global lastLOCs,lastFuncs,verbose
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
    if verbose:
        print "==>",n,co.co_filename,loc
    lastLOCs += loc
    return traceLOC

SUT = sut.sut()
R = random.Random()

try:
    SUT.stopCoverage()
except:
    pass

actLOCs = {}
N = len(SUT.actions())
numClasses = len(set(SUT.actionClasses()))
print "CONSTRUCTING ESTIMATE FOR",numClasses,"CLASSES"

start = time.time()
TIMEOUT = int(sys.argv[1])

while (time.time()-start < TIMEOUT):
    if len(actLOCs) < numClasses:
        act = SUT.randomEnabledPred(R,N,lambda act:SUT.actionClass(act) not in actLOCs)
    else:
        act = SUT.randomEnabled(R)
    c = SUT.actionClass(act)
    if c not in actLOCs:
        print "ACTION:",c
        lastLOCs = 0
        lastFuncs = {}
        verbose = True
        sys.settrace(traceLOC)
        SUT.safely(act)
        sys.settrace(None)
        print c,lastLOCs
        actLOCs[c] = [lastLOCs]
        print "NOW COMPLETED ESTIMATE FOR",len(actLOCs),"OUT OF",numClasses,"CLASSES"
        if numClasses - len(actLOCs) < 10:
            for c in SUT.actionClasses():
                if c not in actLOCs:
                    print "MISSING",c
        print "="*20
    else:
        lastLOCs = 0
        lastFuncs = {}
        verbose = False
        sys.settrace(traceLOC)
        SUT.safely(act)
        sys.settrace(None)
        actLOCs[c].append(lastLOCs)

print "*"*60

total = 0.0
num0 = 0

print "FINAL RESULTS:"

actMeans = {}

for c in SUT.actionClasses():
    if c not in actLOCs:
        print "MISSING SAMPLE DATA FOR:",c
        actLOCs[c] = []
        actMeans[c] = 0
    else:
        actMeans[c] = scipy.mean(actLOCs[c])        
    print c,"SAMPLES:",len(actLOCs[c]),"MEAN:",actMeans[c],"STD:",scipy.std(actLOCs[c])
    total += actMeans[c]
    if actMeans[c] == 0.0:
        num0 += 1
        
if len(sys.argv) < 3:
    baseline = 0.2
else:
    baseline = float(sys.argv[2])

leftover = 1-baseline

P = []

for c in SUT.actionClasses():
    if actMeans[c] == 0.0:
        P.append((baseline/num0,c))
    else:
        P.append(((actMeans[c]/total)*leftover,c))

        
pf = open("locsample.probs",'w')
    
for (p,a) in sorted(P,key=lambda x:x[0]):
    pf.write(a + " %%%% " + str(p) + "\n")

pf.close()
