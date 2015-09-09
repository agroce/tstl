import sut as SUT
import sys

file = sys.argv[0]

t = SUT.sut()
t.restart()
i = 0
for l in open(file):
    name = l[:-1]
    if name == "<<RESTART>>":
        print "RESTART"
        t.restart()
    else:
        print "STEP",i,name
        action = t.playable(name)
        stepOk = t.safely(action)
        if not stepOk:
            print "FAILED STEP"
        checkResult = t.check()
        if not checkResult:
            print "FAILED PROPERTY"
    i += 1

print "TEST REPLAY SUCCESSFUL"
