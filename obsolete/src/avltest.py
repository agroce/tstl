import avl
import random
import sys
import coverage
import time

NTESTS = int(sys.argv[1])
TLEN = int(sys.argv[2])
MAX_VAL = int(sys.argv[3])

test = ["a"]
ref = {}

start = time.time()

branchesHit = set()

cov = coverage.coverage(branch=True, source = ["avl.py"])
cov.start()

try:
    for t in xrange(0,NTESTS):
        test = ["b"]
        ref = {}
        a = avl.AVLTree()
        for s in xrange(0,TLEN):
            op = random.choice(["insert","delete","inorder_traverse"])
            test.append(op)
            if op == "insert":
                val = random.randrange(0,MAX_VAL)
                test.append(val)
                a.insert(val)
                ref[val] = True
            if op == "delete":
                val = random.randrange(0,MAX_VAL)
                test.append(val)
                a.delete(val)
                if val in ref:
                    del ref[val]
            if op == "inorder_traverse":
                tl = a.inorder_traverse()
                assert (sorted(ref.keys()) == tl)
        currBranches = cov.collector.get_arc_data()
        for src_file, arcs in currBranches.iteritems():
            for arc in arcs:
                branch = (src_file, arc)
                if branch not in branchesHit:
                    branchesHit.add(branch)
                    elapsed = time.time()-start
                    print elapsed,len(branchesHit),branch
                    newBranch = True        
                
except:
    print "THE POOR TEST FAILED:"
    for s in test:
        print s

cov.stop()
cov.html_report()

print "ALL DONE"
