import sut
import random

t = sut.t()

LEN = 2000
N = 1000

states = []

for n in xrange(0,N):
    t.restart()
    for s in xrange(0,LEN):
        action = random.choice(t.enabled())
        action[2]()
        assert(t.check())
        if t.state() not in states:
            print "NEW STATE!!!",t.state()
            states.append(t.state())
        else:
            if (random.random() < 0.15):
                t.backtrack(random.choice(states))
        assert(t.check())
