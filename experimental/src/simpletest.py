import random
import sut
import sys

t = sut.t()

print t.actions()
print t.enabled()

(name, guard, action) = t.enabled()[0]

print "TAKING ACTION:",name 

action()

print "TOOK THE ACTION."

print "CHECKING PROPERTIES", t.check()

print t.actions()
print t.enabled()

while True:
    t.restart()
    test = []
    for l in xrange(0,100):
        (name, guard, action) = random.choice(t.enabled())
        test.append(name)
        action()
        if (not t.check()):
            print test
            sys.exit(0)
            
