import sut as SUT
import sys
import traceback

rout = open("replay.out",'w')

file = sys.argv[1]
nocheck = "--nocheck" in sys.argv

t = SUT.sut()
t.restart()
i = 0
for l in open(file):
    name = l[:-1]
    if name == "<<RESTART>>":
        #print "RESTART"
        rout.write("RESTART\n")
        t.restart()
    else:
        #print "STEP",i,t.prettyName(name)
        rout.write("STEP " + str(i) + name + "\n")
        action = t.playable(name)
        if action[1](): # check the guard
            stepOk = t.safely(action)
            if not stepOk:
                print "FAILED STEP"
                print t.failure()
                traceback.print_tb(t.failure()[2])
        if not nocheck:
            checkResult = t.check()
            if not checkResult:
                print "FAILED PROPERTY"
                print t.failure()
                traceback.print_tb(t.failure()[2])
    i += 1

rout.write("TEST REPLAYED SUCCESSFULLY\n")
rout.close()
