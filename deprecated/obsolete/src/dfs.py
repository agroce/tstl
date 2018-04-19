import sut
import random
import sys

maxdepth = int(sys.argv[1])

t = sut.t()

visited = []

def dfs(trail, depth):
    if depth >= maxdepth:
        return
    old = t.state()
    if old in visited:
        return
    visited.append(old)
    next = t.enabled()
    for a in next:
        newtrail = list(trail)
        newtrail.append(a)
        t.backtrack(old)
        a[2]()
        if (not t.check()):
            print "Property failed!"
            (_,_,tb) = t.failure()
            traceback.print_tb(tb)
            print "TEST:"
            for step in (newtrail):
                print step[0] 
        dfs(newtrail, depth+1)
    print depth, len(visited)


t.restart()
dfs([],0)
