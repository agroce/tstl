import sut
import random

t = sut.t()

nextstates = []
visited = []

t.restart()

visited = [t.state()]
frontier = [t.state()]

n = 0

while True:
    n += 1
    nextstates = []
    for s in frontier:
        t.backtrack(s)
        for action in t.enabled():
            action[2]()
            assert(t.check())
            if t.state() not in visited:
                visited.append(t.state())
                nextstates.append(t.state())
            t.backtrack(s)    
    frontier = nextstates
    print n,len(frontier),len(visited)
