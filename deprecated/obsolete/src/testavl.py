import avl
import random
import sys
import coverage
import time
import numpy

start = time.time()

branchesHit = set()

maxval = int(sys.argv[1])
testlen = int(sys.argv[2])
numtests = int(sys.argv[3])

cov = coverage.coverage(branch=True, source=["avl.py"])

cov.start()

for t in xrange(0,numtests):
    a = avl.AVLTree()
    test = []
    ref = set()
    for s in xrange(0,testlen):
        h = a.height
        n = len(ref)

        if (n > 0):
            if not (h <= (numpy.log2(n)+1)):
                print h
                print n
                print (numpy.log2(n))
                sys.exit(0)

        op = random.choice(["add","del","find"])
        val = random.randrange(0,maxval)
        test.append((op,val))
        if op == "add":
            a.insert(val)
            ref.add(val)
        elif op == "del":
            a.delete(val)
            ref.discard(val)
        elif op == "find":
            assert (a.find(val) == (val in ref))

        currBranches = cov.collector.get_arc_data()
        for src_file, arcs in currBranches.iteritems():
            for arc in arcs:
                branch = (src_file, arc)
                if branch not in branchesHit:
                    branchesHit.add(branch)
                    elapsed = time.time()-start
                    print elapsed,len(branchesHit),branch
    avlitems = a.inorder_traverse()
    setitems = []
    for item in ref:
        setitems.append(item)
    setitems = sorted(setitems)
    assert (avlitems == setitems)
