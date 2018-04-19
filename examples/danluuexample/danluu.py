# Example taken from https://danluu.com/testing/

# TSTL, even with coverage-driven mode, has trouble with this.
# tstl_afl_fuzz, however, given the start (once TSTL finds -1 in the first
# position, finishes it in less than five minutes; it does have some difficulty
# getting to the first -1 with just an input producing a four item list, though.

def dlfilter(x):
    for i in range(0,16):
        if not((x & 1) == 1):
            return False
        x >>= 1
    return True

def dut(l):
    if len(l) != 4:
        return 1
    if dlfilter(l[0]):
        if dlfilter(l[1]):
            if dlfilter(l[2]):
                if dlfilter(l[3]):
                    return 0
                return 2
            return 3
        return 4
    return 5
