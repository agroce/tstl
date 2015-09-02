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
            
def canonize(self, test, pred, pruneGuards = False, keepLast = True):
    """
    Attempts to change the pools used with lower-numbered pools (and use as few pools as possible), and to re-order actions into a
    fixed order.  Uses the reducer as a subprocedure to eliminate redundancies discovered during canonization.
    """
    try:
        test_before_canonize(self)
    except:
        pass
    pools = []
    for s in test:
        for p in self.poolUses(s[0]):
            if p not in pools:
                pools.append(p)
    replacements = []
    for (p,i) in pools:
        for n in xrange(0,int(i)):
            replacements.append((p,p.replace("["+i+"]","[" + str(n) + "]")))
    anyReplaced = True
    while anyReplaced:
        anyReplaced = False
        for (old,new) in replacements:
            test2 = map(lambda x: self.actionModify(x,old,new), test)
            if pred(test2):
                #print "REPLACING",old,"WITH",new
                anyReplaced = True
                removals = [old]
                test = test2
                break
        if anyReplaced:
            replacements = filter(lambda x: x[0] not in removals, replacements)

    # Now try reorderings

    #print "TEST:",len(test)

    lastMover = len(test)
    if keepLast:
        lastMover = lastMover - 1
    
    anyMoved = True
    while anyMoved:
        anyMoved = False
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
                    test2 = frag1 + frag2 + frag3 + frag4 + frag5
                    if pred(test2):
                        #print "SWAPPING",i,test[i][0],j,test[j][0]
                        anyMoved = True
                        test = test2
                        break
    
    return self.reduce(test, pred, pruneGuards, keepLast)

def simplify2(self, test, pred, pruneGuards = False, keepLast = True):
    """
    Attempts to replace each action with all lower-ordered actions, which has effect of reducing numeric/complex values.
    """
    try:
        test_before_simplify(self)
    except:
        pass

    anyReplaced = True
    while anyReplaced:
        anyReplaced = False
        for i in xrange(0,len(test)):
            name = test[i][0]
            for (name2,_,_) in self.__actions:
                if self.__orderings[name] > self.__orderings[name2]:
                    test2 = test[0:i] + [self.__names[name2]] + test[i+1:]
                    if pred(test2):
                        print "REPLACING",name,"WITH",name2
                        anyReplaced = True
                        test = test2
                        test = self.reduce(test, pred, pruneGuards, keepLast)
                        break
            if anyReplaced:
                break

    return test

def simplify(self, test, pred, pruneGuards = False, keepLast = True):
    """
    Attempts to produce a 1-simplified test case
    """
    try:
        test_before_simplify(self)
    except:
        pass

    # First attempt to replace pools with lower-numbered pools
    pools = []
    for s in test:
        for p in self.poolUses(s[0]):
            if p not in pools:
                pools.append(p)

    for (p,i) in pools:
        for n in xrange(0,int(i)):
            new = p.replace("["+i+"]","[" + str(n) + "]")
            testC = map(lambda x: self.actionModify(x,p,new), test)
            if pred(testC):
                return self.simplify(self.reduce(testC, pred, pruneGuards, keepLast), pred, pruneGuards, keepLast)

    # Next try to replace any action with a lower-numbered action

    for i in xrange(0,len(test)):
        name1 = test[i][0]
        for (name2,_,_) in self.__actions:
            if self.__orderings[name1] > self.__orderings[name2]:
                testC = test[0:i] + [self.__names[name2]] + test[i+1:]
                if pred(testC):
                    return self.simplify(self.reduce(testC, pred, pruneGuards, keepLast), pred, pruneGuards, keepLast)

    # Swap two pool uses, if this lowers the minimal action ordering between them

    swaps = []
    for (p1,i1) in pools:
        for (p2,i2) in pools:
            if (p1 != p2) and (p1.split("[")[0] == p2.split("[")[0]):
                p1new = p1.replace("[" + i1 + "]", "[" + i2 + "]")
                p2new = p2.replace("[" + i2 + "]", "[" + i1 + "]")
                p2newTemp = p2.replace("[" + i2 + "]", "[**]")
                tempTest = map(lambda x:(x[0].replace(p2,p2newTemp),x[1],x[2]), test)
                tempTest2 = map(lambda x:(x[0].replace(p1,p1new),x[1],x[2]), tempTest)
                testC = map(lambda x: self.actionModify(x,p2newTemp,p2new), tempTest2)
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
                        return self.simplify(self.reduce(testC, pred, pruneGuards, keepLast), pred, pruneGuards, keepLast)
                                        
    # No changes, this is 1-simple (fix-point)
    
    return test

    
