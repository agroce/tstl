import sut as SUT
import sys

rout = open("replay.out",'w')

file = sys.argv[1]

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
        #print "STEP",i,name
        rout.write("STEP " + str(i) + name + "\n")
        action = t.playable(name)
        if action[1](): # check the guard
            stepOk = t.safely(action)
            if not stepOk:
                pass
                #print "FAILED STEP"
        checkResult = t.check()
        if not checkResult:
            pass
            #print "FAILED PROPERTY"
    i += 1

rout.write("TEST REPLAYED SUCCESSFULLY\n")
rout.close()
