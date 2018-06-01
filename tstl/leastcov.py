import sut
import random

sut = sut.sut()
R = random.Random()

training = []
counts = {}

N = 500
L = 100

sut.restart()

for i in range(0, N):
    print "TEST", i
    sut.standardSwarm(R)
    (t, ok) = sut.makeTest(L, R)
    for b in sut.currBranches():
        if b not in counts:
            counts[b] = 1
        else:
            counts[b] += 1
    training.append((set(sut.currBranches()), set(sut.swarmConfig())))

for b in sorted(counts.values(), key=lambda x:  counts[x]):
    print b, counts[b]
