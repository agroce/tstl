import sut as SUT
import sys

file = sys.argv[0]

t = SUT.sut()
t.restart()
i = 0
for l in open(file):
    print "STEP",i,name
    name = l[:-1]
    (_, act, guard) = t.__names[name]
    stepOk = t.safely(act)
    if not stepOk:
        print "FAILED STEP"
    checkResult = t.check()
    if not checkResult:
        print "FAILED PROPERTY"
    i += 1

print "TEST REPLAY SUCCESSFUL"
