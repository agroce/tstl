# $Id: SUTDD.py, based on GCCDD.py v 1.1 2001/11/05 19:53:33 zeller Exp $
# Using delta debugging on an SUT

import DD
import commands
import string

class MyDD(DD.DD):
    def __init__(self):
        DD.DD.__init__(self)
        
    def _test(self, deltas):
        # Build input
        test = []
        for (index, step) in deltas:
            test.append(step)

#        print self.coerce(deltas)

        status = myPred(test + addLast)

        # Determine outcome
        if status == False:
            return self.PASS
        elif status == True:
            return self.FAIL
        return self.UNRESOLVED

    def coerce(self, deltas):
        # Pretty-print the configuration
        input = ""
        for (index, character) in deltas:
            input = input + str(character[0]) + "\n"
        if addLast != []:
            input = input + str(addLast[0][0])
        return input


def DDreduce(SUT, test, pred, keepLast = True):
    global mySUT
    global myPred
    global addLast
    mySUT = SUT
    myPred = pred
    if keepLast:
        addLast = [test[-1]]
        test = test[:-1]
    else:
        addLast = []
    deltas = []
    index = 1
    for t in test:
        deltas.append((index, t))
        index = index + 1

    mydd = MyDD()
    
#    print "Simplifying failure-inducing input..."
    c = mydd.ddmin(deltas)              # Invoke DDMIN
#    print "The 1-minimal failure-inducing input is", mydd.coerce(c)
#    print "Removing any element will make the failure go away."

    return map(lambda x:x[1], c) + addLast


# Local Variables:
# mode: python
# End:
