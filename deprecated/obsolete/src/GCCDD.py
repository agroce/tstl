# $Id: GCCDD.py,v 1.1 2001/11/05 19:53:33 zeller Exp $
# Using delta debugging on GCC input

import DD
import commands
import string

class MyDD(DD.DD):
    def __init__(self):
        DD.DD.__init__(self)
        
    def _test(self, deltas):
        # Build input
        input = ""
        for (index, character) in deltas:
            input = input + character

        # Write input to `input.c'
        out = open('input.c', 'w')
        out.write(input)
        out.close()

        print self.coerce(deltas)

        # Invoke GCC
        (status, output) = commands.getstatusoutput(
            "(ulimit -H -s 256; gcc -c -O input.c) 2>&1")

        print output
        print "Exit code", status

        # Determine outcome
        if status == 0:
            return self.PASS
        elif string.find(output, "fatal signal 11") >= 0:
            return self.FAIL
        return self.UNRESOLVED

    def coerce(self, deltas):
        # Pretty-print the configuration
        input = ""
        for (index, character) in deltas:
            input = input + character
        return input


def DDreduce(SUT, test, pred, keepLast = True):
    deltas = []
    index = 1
    for t in test:
        deltas.append((index, t))
        index = index + 1

    mydd = MyDD()
    
    print "Simplifying failure-inducing input..."
    c = mydd.ddmin(deltas)              # Invoke DDMIN
    print "The 1-minimal failure-inducing input is", mydd.coerce(c)
    print "Removing any element will make the failure go away."

    return mydd.coerce(c)


# Local Variables:
# mode: python
# End:
