import sut
import random
import sys

sut = sut.sut()

R = random.Random()

seen = []
seen.append(sut.state())

i = 0

while True:
    old = sut.state()
    act = sut.randomEnabled(R)
    ok = sut.safely(act)
    if not ok:
        print "DONE!"
        print seen
        sut.prettyPrintTest(sut.test())
        sys.exit(0)
    new = sut.state()[:-1]
    if new in seen:
        sut.backtrack(old)
    else:
        seen.append(new)
        i += 1
        print i,len(seen),sut.prettyName(act[0])
        
