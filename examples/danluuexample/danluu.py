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
