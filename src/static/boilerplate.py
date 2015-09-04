"""
BOILERPLATE METHODS OF SUT
==========================
These are the set of methods available on each SUT by default (depending on whether they are required or not).

Examples
--------

t.enabled()
t.actions()
"""

def setReplayBacktrack(self, val):
    self.__replayBacktrack = val

def test(self):
    """
    Returns the current test as a sequence of (name, guard, actions)
    """
    return self.__test

def captureReplay(self, test):
    captured = ""
    for step in test:
        captured += self.serializable(step)
        captured += "#!#!"
    return captured[:-4]

def replayable(self,stest):
    steps = stest.split("#!#!")
    if steps == ['']:
        return []
    return map(self.playable, steps)

def enabled(self):
    """
    Returns all enabled action objects.
    """
    return filter(lambda (s, g, a): g(), self.__actions)

def features(self):
    return self.__features

def actions(self):
    """
    Returns all the action objects whether enabled or disabled.
    """
    return self.__actions

def disable(self,f):
    """
    Disable an action by name.
    """
    newActions = []
    for (name, act, guard) in self.__actions:
        if not re.match(f, name):
            newActions.append((name, act, guard))
    self.__actions = newActions

def enableAll(self):
    """
    Enable all actions.
    """
    self.__actions = self.__actions_backup

def serializable(self, step):
    return step[0]

def playable(self, name):
    return self.__names[name]

def safely(self, act):
    try:
        act[2]()
    except:
        self.__failure = sys.exc_info()
        return False
    return True

def failure(self):
    return self.__failure

def replay(self, test, catchUncaught = False):
    self.restart()
    for (name, guard, act) in test:
        if guard():
            if catchUncaught:
                try:
                    act()
                except:
                    pass
            else:
                act()
        if not self.check():
            return False
    return True

def replayUntil(self, test, pred, catchUncaught = False):
    self.restart()
    newt = []
    if pred():
        return newt

    for (name, guard, act) in test:

        newt.append((name, guard, act))
        if guard():
            if catchUncaught:
                try:
                    act()
                except:
                    pass
            else:
                act()
        if pred():
            return newt
        if not self.check():
            return False
    return None

def failsCheck(self, test):
    try:
        return not self.replay(test, catchUncaught = True)
    except:
        return True
    return False

def fails(self, test):
    try:
        return not self.replay(test)
    except:
        return True
    return False

def logOff(self):
    self.__log = None

def logAll(self):
    self.__log = 'All'

def setLog(self, level):
    self.__log = level

def setLogAction(self, f):
    self.__logAction = f

def logPrint(self, name, code, text, after):
    print "[",
    if after:
        print "POST",
    print "LOG " + name + "  :  " + str(code) + "] " + str(text)

def __candidates(self, t, n):
    candidates = []
    s = len(t) / n
    for i in xrange(0,n):
        tc = t[0:i*s]
        tc.extend(t[(i+1)*s:])
        candidates.append(tc)
    return candidates

def reduce(self, test, pred, pruneGuards = False, keepLast = True):
    """
    This function takes a test that has failed, and attempts to reduce it using a simplified version of Zeller's Delta-Debugging algorithm.
    pruneGuards determines if disabled guards are automatically removed from reduced tests, keepLast determines if the last action must remain unchanged
    (this is useful for keeping the fault detected from changing).
    """
    try:
        test_before_reduce(self)
    except:
        pass
    if keepLast:
        tb = test[:-1]
        addLast = [test[-1]]
    else:
        tb = test
        addLast = []
    n = 2
    count = 0
    while True:
        count += 1
        c = self.__candidates(tb, n)
        reduced = False
        for tc in c:
            if pred(tc + addLast):
                tb = tc
                n = 2
                if pruneGuards:
                    self.restart()
                    newtb = []
                    for a in tb:
                        if a[1]():
                            newtb.append(a)
                            try:
                                a[2]()
                            except:
                                pass
                    tb = newtb
                reduced = True
                break
        if not reduced:
            if n == len(tb):
                try:
                    test_after_reduce(self)
                except:
                    pass
                return tb + addLast
            n = min(n*2, len(tb))
        elif len(tb) == 1:
            try:
                test_after_reduce(self)
            except:
                pass
            if pred([] + addLast):
                return ([] + addLast)
            else:
                return (tb + addLast)

def poolUses(self,str):
    uses = []
    for p in self.__pools:
        pos = str.find(p,0)
        while pos != -1:
            access  = str[pos:str.find("]",pos)+1]
            if access not in uses:
                uses.append((access,access[access.find("[")+1:access.find("]")]))
            pos = str.find(p,pos+1)
    return uses
            
def actionModify(self,action,old,new):
    name = action[0]
    newName = name.replace(old,new)
    return self.__names[newName]
            
def simplify(self, test, pred, pruneGuards = False, keepLast = True):
    """
    Attempts to produce a 1-simplified test case
    """
    try:
        test_before_simplify(self)
    except:
        pass

    # Turns off requirement that you can't initialize an unused variable, allowing reducer to take care of redundant assignments
    self.__relaxUsedRestriction = True

    # If any action can be changed, resulting in a shorter test, that is first:

    for i in xrange(0,len(test)):
        name1 = test[i][0]
        for name2 in self.__names:
            if name1 != name2:
                testC = test[0:i] + [self.__names[name2]] + test[i+1:]
                if pred(testC):
                    rtestC = self.reduce(testC, pred, pruneGuards, keepLast)
                    if len(rtestC) < len(test):
                        print "SIMPLIFIER: REPLACED STEP",i,name1,"WITH",name2,"REDUCING LENGTH FROM",len(test),"TO",len(rtestC)
                        return self.simplify(rtestC, pred, pruneGuards, keepLast)
        
    # Attempt to replace pools with lower-numbered pools
    pools = []
    for s in test:
        for p in self.poolUses(s[0]):
            if p not in pools:
                pools.append(p)

    # Reduce number of pools but may need to move assignment to a later position

    for pos in xrange(0,len(test)):
        for (p,i) in pools:
            for n in xrange(0,int(i)):
                new = p.replace("["+i+"]","[" + str(n) + "]")    
                prefix = []
                moved = []
                for j in xrange(0,pos):
                    if new in test[j][0]:
                        moved.append(test[j])
                    else:
                        prefix.append(test[j])
                suffix = map(lambda x: self.actionModify(x,p,new), moved + test[pos:])
                testC = prefix + map(lambda x: self.actionModify(x,p,new), suffix)
                if (testC != test) and pred(testC):
                    print "SIMPLIFIER: REPLACED",p,"WITH",new," -- MOVED TO",pos
                    return self.simplify(self.reduce(testC, pred, pruneGuards, keepLast), pred, pruneGuards, keepLast)
        
    # Replace ALL occurrences of an action with a lower-numbered action

    for i in xrange(0,len(test)):
        name1 = test[i][0]
        for (name2,_,_) in self.__actions:
            if self.__orderings[name1] > self.__orderings[name2]:
                testC = map(lambda x: self.actionModify(x,name1,name2), test)
                if pred(testC):
                    print "SIMPLIFIER: REPLACED ALL",name1,"WITH",name2
                    return self.simplify(self.reduce(testC, pred, pruneGuards, keepLast), pred, pruneGuards, keepLast)
        
    # Next try to replace any single action with a lower-numbered action

    for i in xrange(0,len(test)):
        name1 = test[i][0]
        for (name2,_,_) in self.__actions:
            if self.__orderings[name1] > self.__orderings[name2]:
                testC = test[0:i] + [self.__names[name2]] + test[i+1:]
                if pred(testC):
                    print "SIMPLIFIER: REPLACED STEP",i,name1,"WITH",name2
                    return self.simplify(self.reduce(testC, pred, pruneGuards, keepLast), pred, pruneGuards, keepLast)

    # Swap two pool uses after position, if this lowers the minimal action ordering between them

    swaps = []
    for (p1,i1) in pools:
        for (p2,i2) in pools:
            for pos in xrange(0,len(test)):
                if (p1 != p2) and (p1.split("[")[0] == p2.split("[")[0]):
                    p1new = p1.replace("[" + i1 + "]", "[" + i2 + "]")
                    p2new = p2.replace("[" + i2 + "]", "[" + i1 + "]")
                    p2newTemp = p2.replace("[" + i2 + "]", "[**]")
                    tempTest = map(lambda x:(x[0].replace(p2,p2newTemp),x[1],x[2]), test[pos:])
                    tempTest2 = map(lambda x:(x[0].replace(p1,p1new),x[1],x[2]), tempTest)
                    testC = test[:pos] + map(lambda x: self.actionModify(x,p2newTemp,p2new), tempTest2)
                    assert (len(testC) == len(test))
                    leastTestC = -1
                    leastTest = -1
                    for s in xrange(0,len(test)):
                        if test[s] != testC[s]:
                            ordTest = self.__orderings[test[s][0]]
                            if (leastTest == -1) or (ordTest < leastTest):
                                leastTest = ordTest
                            ordTestC = self.__orderings[testC[s][0]]
                            if (leastTestC == -1) or (ordTestC < leastTestC):
                                leastTestC = ordTestC
                    if leastTestC < leastTest:
                        if pred(testC):
                            print "SIMPLIFIER: SWAPPED",p1,"AND",p2,"AFTER STEP",pos
                            return self.simplify(self.reduce(testC, pred, pruneGuards, keepLast), pred, pruneGuards, keepLast)

    # Finally try to swap any out-of-order actions
        
    lastMover = len(test)
    if keepLast:
        lastMover -= 1
        
    for i in xrange(0,lastMover):
        for j in xrange(i+1,lastMover):
            step1 = test[i][0]
            step2 = test[j][0]
            if self.__orderings[step2] < self.__orderings[step1]:
                    frag1 = test[:i]
                    frag2 = [test[j]]
                    frag3 = test[i+1:j]
                    frag4 = [test[i]]
                    frag5 = test[j+1:]
                    testC = frag1 + frag2 + frag3 + frag4 + frag5
                    if pred(testC):
                        print "SIMPLIFIER: SWAPPED STEP",i,test[i][0],"WITH STEP",j,test[j][0]
                        return self.simplify(self.reduce(testC, pred, pruneGuards, keepLast), pred, pruneGuards, keepLast)
                                        
    # No changes, this is 1-simple (fix-point)

    try:
        test_after_simplify(self)
    except:
        pass

    self.__relaxUsedRestriction = True
    # restore normal TSTL semantics!
    
    return test

    
