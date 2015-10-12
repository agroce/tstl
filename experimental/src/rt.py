import sut
import random

t = sut.t()

LEN = 2000
N = 1000

for n in range(0,N):
    for s in range(0,LEN):
        action = random.choice(t.enabled())
        action[2]()
        assert(t.check())
