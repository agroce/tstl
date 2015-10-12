import sut
import random

t = sut.t()

LEN = 2000
N = 1000

for n in range(0,N):
    t.restart()
    for s in range(0,LEN):
        oldstate = t.state()
        nxt = []
        for action in t.enabled():
            action[2]()
            assert(t.check())
            fitness = 0
            avl1 = t.p_AVL[0]
            avl2 = t.p_AVL[1]
            if avl1 != None:
                fitness = len(avl1.inorder_traverse())
            if avl2 != None:
                fitness = max(fitness, len(avl2.inorder_traverse()))
            nxt.append((action, fitness))
            t.backtrack(oldstate)
        sortedacts = sorted(nxt, key=lambda x : x[1], reverse = True)
        print(sortedacts[0])
        sortedacts[0][0][2]()
