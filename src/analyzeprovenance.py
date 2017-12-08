from __future__ import print_function

import glob
import sys
import sut

sut = sut.sut()

highLevel = {}
lowLevel = {}

for f in glob.glob(sys.argv[1]):
    try:
        t = sut.loadTest(f)
    except KeyError:
        continue
    #print f
    for s in t:
        if len(s) > 3:
            src = s[3]
            high = src.split(":")[0]
            if high in highLevel:
                highLevel[high].append(f)
            else:
                highLevel[high] = [f]
            if src in lowLevel:
                lowLevel[src].append(f)
            else:
                lowLevel[src] = [f]

sources =  {}
for f in set(highLevel.keys()):
    sources[f] = sut.loadTest(f)
                
print("DETAILED PROVENANCE SUMMARY:")
                
lsrcs = sorted(list(lowLevel.keys()), key=lambda x:len(lowLevel[x]))

print()
print()
print("BY ACTION CLASS:")

classes = {}
for s in lsrcs:
    ss = s.split(":")
    srcAct = sources[ss[0]][int(ss[1])]
    print(s,len(lowLevel[s]),sut.prettyName(srcAct[0]))
    c = sut.actionClass(srcAct)
    if c in classes:
        classes[c].extend(lowLevel[s])
    else:
        classes[c] = lowLevel[s]

csrcs = sorted(list(classes.keys()),key=lambda x:len(classes[x]))

for c in csrcs:
    print(c,len(classes[c]))

    
print()
print()
    
print("FILE LEVEL PROVENANCE SUMMARY:")

hsrcs = sorted(list(highLevel.keys()), key=lambda x:len(highLevel[x]))

for s in hsrcs:
    print(s,len(highLevel[s]))

