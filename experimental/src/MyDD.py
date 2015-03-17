# $Id: MyDD.py,v 1.1 2001/11/05 19:53:33 zeller Exp $
# Template for adapting delta debugging.  Areas to customize are
# tagged with `FIXME'.

import DD

class MyDD(DD.DD):
    def __init__(self):
        DD.DD.__init__(self)
        
    def _test(self, deltas):
	# FIXME: Set up a test function that takes a set of deltas and
        # returns either self.PASS, self.FAIL, or self.UNRESOLVED.
        if c == []:
            return self.PASS
        return self.UNRESOLVED

if __name__ == '__main__':
    deltas = [ 1 ]
    # FIXME: Insert your deltas here

    mydd = MyDD()
    
    # print "Simplifying failure-inducing input..."
    # c = mydd.ddmin(deltas)              # Invoke DDMIN
    # print "The 1-minimal failure-inducing input is", c
    # print "Removing any element will make the failure go away."
    # print
    
    print "Isolating the failure-inducing difference..."
    (c, c1, c2) = mydd.dd(deltas)	# Invoke DD
    print "The 1-minimal failure-inducing difference is", c
    print c1, "passes,", c2, "fails"




# Local Variables:
# mode: python
# End:
