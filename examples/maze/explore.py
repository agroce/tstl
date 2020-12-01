from __future_ import print_function
import sut
import random
import sys

sut = sut.sut()

R = random.Random()

seen = []
seen.append(sut.state())

i = 0

PATIENCE = 20

bored = 0

while True:
    if bored > PATIENCE:
        sut.restart()
        seen = []
        seen.append(sut.state())
        i = 0
    old = sut.state()
    act = sut.randomEnabled(R)
    ok = sut.safely(act)
    if not ok:
        print("DONE!")
        print(seen)
        sut.prettyPrintTest(sut.test())
        sys.exit(0)
    new = sut.state()[:-1]
    if new in seen:
        bored += 1
        sut.backtrack(old)
    else:
        bored = 0
        seen.append(new)
        i += 1
        print(i,len(seen),sut.prettyName(act[0]))
        
