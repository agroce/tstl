import sut
import time
import random

sut = sut.sut()
rgen = random.Random()

MEMORY = 5
TIMEOUT = 300
TEST_LENGTH = 200
PEXTEND = 0.2

goodTests = []
startTime = time.time()
while (time.time() - startTime <= TIMEOUT):
    if (len(goodTests) > 0) and (rgen.random() < PEXTEND):
        sut.backtrack(rgen.choice(goodTests)[1])
    else:
        sut.restart()
    for s in xrange(0,TEST_LENGTH):
        action = sut.randomEnabled(rgen)
        r = sut.safely(action)
        if len(sut.newBranches()) > 0:
            print time.time(),len(sut.allBranches()),'NEW BRANCHES:', sut.newBranches()
        if MEMORY > 0:
            goodTests.append((sut.state(), sut.currBranches()))
            goodTests = sorted(goodTests, reverse=True)[:MEMORY]

