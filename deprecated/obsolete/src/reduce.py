def candidates(t, n):
    candidates = []
    s = len(t) / n
    for i in xrange(0,n):
        tc = t[0:i*s]
        tc.extend(t[(i+1)*s:])
        candidates.append(tc)
    return candidates
    

def reduce(SUT, test, f, pred, checkGuards = False):
    print len(test)
    tb = test
    n = 2
    oldc = []
    while oldc != tb:
        c = candidates(tb, n)
        reduced = False
        for tc in c:
            if pred(f(tc)):
                oldc = tb
                tb = tc
                n = 2
                print "reduced, n back to 2, len", len(tb)
                if checkGuards:
                    SUT.restart()
                    tb = filter(lambda a:a[1](), tb)
                    print "Threw away failing guards",len(tb)
                reduced = True
                break
        if not reduced:
            if n == len(tb):
                return tb
            n = min(n*2, len(tb))
            print "increasing n to ",n
    return tb
