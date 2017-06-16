"""
BOILERPLATE METHODS OF SUT
==========================
These are the set of methods available on each SUT by default

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

def getOkExceptions(self,name):
    return self.__okExcepts[name]

def getPreCode(self,name):
    try:
        return self.__preCode[name]
    except:
        return None

def getRefCode(self,name):
    try:
        return self.__refCode[name]
    except:
        return None

def getPropCode(self,name):
    try:
        return self.__propCode[name]
    except:
        return None        

def actionClass(self,action):
    return self.__actionClass[action[0]]

def dependencies(self,actClass):
    return self.__dependencies[actClass]

def abstraction(self, pool):
    if pool not in self.__abstraction:
        return None
    return self.__abstraction[pool]

def prettyName(self, name):
    newName = name
    for p in self.__pools:
        pfind = newName.find(p+"[")
        while pfind != -1:
            closePos = newName.find("]",pfind)
            index = newName[newName.find("[",pfind)+1:closePos]
            access = newName[pfind:newName.find("]",pfind)+1]
            needUnderscore = ""
            if p[-1] in ['0','1','2','3','4','5','6','7','8','9']:
                needUnderscore = "_"
            newAccess = p.replace(self.__poolPrefix,"") + needUnderscore + index                
            newName = newName.replace(access, newAccess)
            pfind = newName.find(p+"[")
    return newName

def actOrder(self, action):
    return self.__orderings[action[0]]

def pools(self):
    return self.__pools

def prettyPrintTest(self, test, columns=80):
    i = 0
    for (s,_,_) in test:
        steps = "# STEP " + str(i)
        print self.prettyName(s).ljust(columns - len(steps),' '),steps
        i += 1

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

def highLowSwarm(self, rgen, P = 0.5, file = None, highProb = 0.9):
    high = []

    if file != None:
        classProb = {}
        for l in open(file):
            ls = l.split("%%%%")
            c = ls[0][:-1]
            prob = float(ls[1])
            classProb[c] = prob
            
    for c in self.__actionClasses:
        if file == None:
            if rgen.random() < P:
                high.append(c)
        else:
            if rgen.random() < classProb[c]:
                high.append(c)
    if high == []:
        high.append(rgen.choice(self.__actionClasses))
    changed = True
    while changed:
        changed = False
        
        forcedAdd = []
        for c in high:
            for d in self.dependencies(c):
                df = filter(lambda x:x in d, high) + filter(lambda x:x in d, forcedAdd)
                if df == []:
                    forcedAdd.append(rgen.choice(d))
                    changed = True
        high.extend(forcedAdd)

        forcedAdd = []
        for c in high:
            if self.dependencies(c) == []:
                anyDepend = False
                for c2 in (high + forcedAdd):
                    for d in self.dependencies(c2):
                        if c in d:
                                anyDepend = True
                                break
                    if anyDepend:
                        break
                if not anyDepend:
                    needsThis = []
                    for c2 in self.__actionClasses:
                        for d in self.dependencies(c2):
                            if c in d:
                                needsThis.append(c2)
                                break
                    if needsThis != []:
                        forcedAdd.append(rgen.choice(needsThis))
                        changed = True
        high.extend(forcedAdd)
    low = filter(lambda x:x not in high, self.__actionClasses)
    probs = []
    if low == []:
        return map(lambda x:(1.0/len(high),x), high)
    if high == []:
        return map(lambda x:(1.0/len(low),x), low)    
    highP = highProb / len(high)
    lowP = (1.0-highProb) / len(low)    
    for c in high:
        probs.append((highP,c))
    for c in low:
        probs.append((lowP,c))
    return probs

def highLowClassProbs(self,rgen, P = 0.5, file = None, highProb = 0.9):
    high = []
    low = []
    if file != None:
        classProb = {}
        for l in open(file):
            ls = l.split("%%%%")
            c = ls[0][:-1]
            prob = float(ls[1])
            classProb[c] = prob
             
    for c in self.__actionClasses:
        if file == None:
            if rgen.random() < P:
                high.append(c)
            else:
                low.append(c)
        else:
            if rgen.random() < classProb[c]:
                high.append(c)
            else:
                low.append(c)
    probs = []
    if low == []:
        return map(lambda x:(1.0/len(high),x), high)
    if high == []:
        return map(lambda x:(1.0/len(low),x), low)    
    highP = highProb / len(high)
    lowP = (1.0-highProb) / len(low)    
    for c in high:
        probs.append((highP,c))
    for c in low:
        probs.append((lowP,c))
    return probs

def randomEnabledClassProbs(self,rgen,probs):
    if self.__enumerateEnabled:
        enableds = self.enabled()
    else:
        enableds = None            
    a = None
    while a == None:
        r = rgen.random()
        p = 0.0
        ac = None
        for (pac,tac) in probs:
            p += pac
            if p > r:
                ac = tac
                break
        a = self.randomEnabled(rgen,actFilter = lambda act:self.actionClass(act) == ac, enabledActs=enableds)
        if a == None:
            if len(probs) == 1:
                return None
            padd = pac / (len(probs)-1)
            newprobs = []
            for (pac,tac2) in probs:
                #print pac,tac2
                if tac2 == tac:
                    continue
                newprobs.append((pac+padd,tac2))
            probs = newprobs
            if probs == []:
                break
    return a

def setEnumerateEnabled(self,bval):
    self.__enumerateEnabled = bval

def randomEnabled(self,rgen,actFilter=None,enabledActs=None):
    """
    Return a random enabled action, or None if no such action can be produced, based on a provided random generator
    """
    if enabledActs != None:
        acts = list(enabledActs)
    else:
        acts = self.__actions
    if filter != None:
        acts = filter(actFilter,acts)
    if self.__enumerateEnabled:
        try:
            return rgen.choice(filter(lambda (s, g, a): g(), acts))
        except IndexError:
            return None
    a = None
    while a == None:
        if len(acts) == 1:
            p = 0
        elif len(acts) == 0:
            break
        else:
            p = rgen.randint(0,len(acts)-1)
        a = acts[p]
        if a[1]():
            break
        else:
            a = None
        acts = acts[:p] + acts[p+1:]
    return a

def randomEnableds(self,rgen,n):
    """
    Return list of random enabled actions, up to n actions if possible
    """

    retActs = []
    acts = self.__actions
    if self.__enumerateEnabled:
        acts = self.enabled()    
    while len(retActs) < n:
        if len(acts) == 1:
            p = 0
        elif len(acts) == 0:
            break
        else:
            p = rgen.randint(0,len(acts)-1)
        a = acts[p]
        if a[1]():
            retActs.append(a)
        acts = acts[:p] + acts[p+1:]
    return retActs

def randomEnabledPred(self,rgen,n,pred):
    """
    Return first enabled action satisfying pred, with up to n attempts.
    If none found, returns last enabled action checked.
    """

    tries = 0
    acts = self.__actions
    if self.__enumerateEnabled:
        acts = self.enabled()
    a = None
    lastSafe = None
    while tries < n:
        if len(acts) == 1:
            p = 0
        elif len(acts) == 0:
            break
        else:
            p = rgen.randint(0,len(acts)-1)
        a = acts[p]
        if a[1]():
            lastSafe = a
            if pred(a):
                return a
            tries += 1
        acts = acts[:p] + acts[p+1:]
    return lastSafe

def mutate(self,test,rgen,Pinsert=0.2):
    '''
    Simple tool for mutating tests randomly.  Does not ensure validity of the new test, which may be functionally equivalent.
    There are two types of mutation, replacement and insertion.  Pinsert gives probability of insert (default 0.2).
    '''
    newTest = list(test)
    loc = rgen.randrange(0,len(test))
    act = rgen.choice(self.__actions)
    if rgen.random() < Pinsert:
        newTest.insert(loc,act)
    else:
        newTest[loc] = act
    return newTest

def crossover(self,test1,test2,rgen,twoPoint=False):
    '''
    Simple code for performing crossover of two tests.  Just picks an order, then picks a point at which to stop first 
    test then start second.  twoPoint results in two point crossover.
    '''
    if rgen.randrange(2) == 0:
        t1 = test1
        t2 = test2
    else:
        t2 = test1
        t1 = test2
    p1 = rgen.randrange(1,len(t1))
    p2 = rgen.randrange(0,len(t2))
    newTest = t1[:p1]
    if twoPoint:
        p3 = rgen.randrange(p1,len(t1))
        p4 = rgen.randrange(p2,len(t2))
        newTest.extend(t2[p2:p4])
        newTest.extend(t1[p3:])
    else:
        newTest.extend(t2[p2:])
    return newTest
        
def makeTest(self,size,rgen=None,generator=None,sgenerator=None,stopFail=True,checkProp=True,initial=None,timeout=None):
    '''
    Allows generation of fixed length tests using either a default generator (pure random testing), or using a simple
    generator that only takes the current test step as input (generator) or a complex stateful generator (sgenerator).
    An sgenerator must take as input both a state and an interface to the SUT (to query for coverage, etc.) and return
    an (action, new state) tuple.  User can also control whether to stop on failure, whether to check properties, and
    supply a timeout in seconds.
    
    '''
    
    if timeout != None:
        stime = time.time()

    noFailure = True
        
    if generator != None:
        genF = generator
    else:
        genF = lambda x: self.randomEnabled(rgen)
    if sgenerator != None:
        state = initial
    self.restart()
    for i in xrange(0,size):
        if sgenerator == None:
            ok = self.safely(genF(i))
        else:
            (action, state) = sgenerator(state,self)
            ok = self.safely(action)
        if not ok:
            noFailure = False
            if stopFail:
                return (self.test(), False)
        if checkProp:
            if not self.check():
                noFailure = False
                if stopFail:
                    return (self.test(), False)
        if timeout != None:
            if (time.time() - stime) > timeout:
                return (self.test(), noFailure)
    return (list(self.test()), noFailure)

def features(self):
    return self.__features

def actions(self):
    """
    Returns all the action objects whether enabled or disabled.
    """
    return self.__actions

def actionClasses(self):
    return self.__actionClasses

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
    self.__swarmConfig = None
    self.__actions = self.__actions_backup

def objCodeLOCs(self,obj,context):
    LOCs = []
    for o in inspect.getmembers(obj):
        if inspect.isfunction(o[1]) or inspect.ismethod(o[1]):
            if o[0] == "__init__":
                LOCs.append((context[-1],len(inspect.getsourcelines(o[1])[0]), context))
            LOCs.append((o[0],len(inspect.getsourcelines(o[1])[0]), context))
        if inspect.isclass(o[1]):
            if o[1] == object:
                continue
            if o[1] == type:
                continue
            LOCs.extend(self.objCodeLOCs(o[1],context + [o[0]]))
    return LOCs
    
def codeLOCs(self):
    LOCs = []
    for m in self.__importModules:
        LOCs.extend(self.objCodeLOCs(m,[m.__name__]))
    return LOCs

def codeLOCProbs(self, baseline=0.2, codeLOCs=None):
    if codeLOCs == None:
        # use static estimation if no dynamic estimates provided
        cl = self.codeLOCs()
    else:
        cl = codeLOCs

    totalLOCs = 0.0
    aProbs = []
    num0LOC = 0
    
    for a in self.__actionClasses:
        thisLOC = 0
        for (f,LOC,c) in cl:
            if (("." + f + "(") in a):
                thisLOC += LOC
        totalLOCs += thisLOC
        if thisLOC == 0:
            num0LOC += 1
        aProbs.append((a,thisLOC))
    P = []
    leftOver = 1.0 - baseline
    for (a,LOC) in aProbs:
        if LOC == 0:
            P.append((baseline/num0LOC,a))
        else:
            P.append(((LOC/totalLOCs)*leftOver,a))
    return P
    
    
def readProbFile(self, file, returnList=False):
    classProb = {}
    with open(file) as f:
        for l in f:
            ls = l.split("%%%%")
            c = ls[0][:-1]
            prob = float(ls[1])
            classProb[c] = prob
    if not returnList:
        return classProb
    l = []
    for k in classProb:
        l.append((classProb[k],k))
    return l
    
def standardSwarm(self, rgen, P = 0.5, file = None, classProb = None, noDependencies = False):
    """
    Enables all actions, then sets a swarm configuration based on rgen, P = probability of enabling an action class,
    file is a file (format action %%%% probability) giving probabilities for inclusion)
    """
    self.enableAll()
    newEnabled = []

    if file != None:
        classProb = self.readProbFile(file)
            
    for c in self.__actionClasses:
        if classProb == None:
            if rgen.random() < P:
                newEnabled.append(c)
        else:
            if rgen.random() < classProb[c]:
                newEnabled.append(c)
    if newEnabled == []:
        newEnabled.append(rgen.choice(self.__actionClasses))

    changed = True
    if noDependencies:
        changed = False
    
    while changed:
        changed = False
        
        forcedAdd = []
        for c in newEnabled:
            for d in self.dependencies(c):
                df = filter(lambda x:x in d, newEnabled) + filter(lambda x:x in d, forcedAdd)
                if df == []:
                    forcedAdd.append(rgen.choice(d))
                    changed = True
        newEnabled.extend(forcedAdd)

        forcedAdd = []
        for c in newEnabled:
            if self.dependencies(c) == []:
                anyDepend = False
                for c2 in (newEnabled + forcedAdd):
                    for d in self.dependencies(c2):
                        if c in d:
                                anyDepend = True
                                break
                    if anyDepend:
                        break
                if not anyDepend:
                    needsThis = []
                    for c2 in self.__actionClasses:
                        for d in self.dependencies(c2):
                            if c in d:
                                needsThis.append(c2)
                                break
                    if needsThis != []:
                        forcedAdd.append(rgen.choice(needsThis))
                        changed = True
        newEnabled.extend(forcedAdd)
                            
    #print "SWARMING WITH CONFIGURATION:",newEnabled
    self.__swarmConfig = newEnabled
    enabledActions = []
    for a in self.__actions:
        if self.actionClass(a) in newEnabled:
            enabledActions.append(a)
    self.__actions = enabledActions

def swarmConfig(self):
    return self.__swarmConfig
    
def serializable(self, step):
    return step[0]

def saveTest(self, test, filename):
    outf = open(filename,'w')
    for s in test:
        outf.write(self.serializable(s) + "\n")
    outf.close()

def loadTest(self, filename):
    test = []
    with open(filename) as f:
        for l in f:
            test.append(self.playable(l[:-1]))
    return test

def playable(self, name):
    return self.__names[name]

def setDebugSafelyMode(self, mode):
    self.__safeSafelyMode = mode

def safely(self, act):
    if self.__safeSafelyMode:
        if not act[1]():
            print "WARNING:  ATTEMPED TO EXECUTE NON-ENABLED ACTION"
            return False
    try:
        act[2]()
    except KeyboardInterrupt as e:
        raise e
    except:
        self.__failure = sys.exc_info()
        return False
    return True

def failure(self):
    return self.__failure

def warning(self):
    return self.__warning

def allEnabled(self, test):
    for (name, guard, act) in test:
        if not guard():
            return False
        self.safely((name,guard,act))
    return True

def replay(self, test, catchUncaught = False, extend=False, checkProp=False, verbose=False, stopFail = True, returnCov = False):
    '''
    Replays a test, either resetting first or extending current test (default is to restart).  Can either stop or keep going
    on failure, ignore uncaught exceptions, throw them, and check or not check properties.  The returnCov setting adds a sequential
    record of coverage by step as another element of a return tuple.
    '''
    if not extend:
        self.restart()
    if returnCov:
        allS = set([])
        allB = set([])
        cov = []
    for (name, guard, act) in test:
        if verbose:
            print name
        if guard():
            if verbose:
                print "EXECUTING"
            if catchUncaught:
                try:
                    act()
                except KeyboardInterrupt as e:
                    raise e                    
                except:
                    self.__failure = sys.exc_info()
                    if stopFail:
                        return False
                    pass
            else:
                act()
        if checkProp:
            if (not self.check()) and stopFail:
                return False
        if returnCov:
            s = set(self.currStatements())
            b = set(self.currBranches())
            newS = s - allS
            newB = b - allB
            if (len(newS) > 0) or (len(newB) > 0):
                cov.append((newS,newB))
            allS.update(s)
            allB.update(b)            
    if returnCov:
        return (self.__failure == None, cov)
    return (self.__failure == None)

def replayUntil(self, test, pred, catchUncaught = False, checkProp=False, stopFail = True):
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
                except KeyboardInterrupt as e:
                    raise e                    
                except:
                    self.__failure = sys.exc_info()
                    if stopFail:
                        return False
                    pass
            else:
                act()
        if pred():
            return newt
        if checkProp:
            if not self.check():
                return False
    return None

def failsCheck(self, test, verbose=False, failure=None):
    try:
        r = self.replay(test, catchUncaught=True, checkProp=True, verbose=verbose)
    except KeyboardInterrupt as e:
        raise e        
    except:
        if (failure == None) or ((self.__failure[0] == failure[0]) and (repr(self.__failure[1]) == repr(failure[1]))):
            return True
        else:
            return False
    if r == True:
        return False
    if (failure == None) or ((self.__failure[0] == failure[0]) and (repr(self.__failure[1]) == repr(failure[1]))):
        return True
    else:
        return False

def fails(self, test, verbose=False, failure=None):
    try:
        r = self.replay(test, verbose=verbose, catchUncaught=True)
    except KeyboardInterrupt as e:
        raise e    
    except:
        if (failure == None) or ((self.__failure[0] == failure[0]) and (repr(self.__failure[1]) == repr(failure[1]))):
            return True
        else:
            return False
    if r == True:
        return False
    if (failure == None) or ((self.__failure[0] == failure[0]) and (repr(self.__failure[1]) == repr(failure[1]))):
        return True
    else:
        return False
    
def failsAny(self, test, verbose=False, failure=None):
    try:
        r = self.replay(test, checkProp=True, verbose=verbose,catchUncaught=True)
    except KeyboardInterrupt as e:
        raise e        
    except:
        self.__failure = sys.exc_info()
        if (failure == None) or ((self.__failure[0] == failure[0]) and (repr(self.__failure[1]) == repr(failure[1]))):
            return True                
        return False
    if r == False:
        #self.__failure = sys.exc_info()
        if (failure == None) or ((self.__failure[0] == failure[0]) and (repr(self.__failure[1]) == repr(failure[1]))):
            return True                
        return False        
    return False    

def verbose(self, bool):
    self.__verboseActions = bool

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

def testCandidates(self, t, n):
    # Fix so that if n means removal is single items, you just return all the relevant removals
    candidates = []
    s = len(t) / n
    if (s == 1):
        n = len(t)
    for i in xrange(0,n):
        tc = t[0:i*s]
        tc.extend(t[(i+1)*s:])
        candidates.append(tc)
    return candidates

def reduce(self, test, pred, pruneGuards = False, keepLast = False, verbose = True, rgen = None, amplify = False, stopFound = False, tryFast=False):
    """
    This function takes a test that has failed, and attempts to reduce it using a simplified version of Zeller's Delta-Debugging algorithm.
    pruneGuards determines if disabled guards are automatically removed from reduced tests, keepLast determines if the last action must remain unchanged
    (this is useful for keeping the fault detected from changing).

    amplify changes behavior from "preserve (or find) pred(test) = True" to "increase the value of pred(test)"

    tryFast means that instead of the binary search, reduce assumes the test is already close to 1-minimal (e.g., from normalization)
    and skips right to the smallest granularity, searching for a close-by 1-minimal test.
    """
    try:
        test_before_reduce(self)
    except:
        pass

    if len(test) < 2:
        return test

    if amplify:
        currBest = pred(test)
    
    if keepLast:
        tb = test[:-1]
        addLast = [test[-1]]
    else:
        tb = test
        addLast = []
    if not tryFast:
        n = 2
    else:
        n = len(tb)
    count = 0
    stests = {}
    while True:
        stest = self.captureReplay(tb)
        assert ((stest,n) not in stests)
        stests[(stest,n)] = True
        count += 1
        c = self.testCandidates(tb, n)
        if rgen:
            rgen.shuffle(c)
        reduced = False
        for tc in c:
            if verbose == "VERY":
                print "Trying candidate of length",len(tc+addLast)
            v = pred(tc + addLast)
            if amplify:
                if v > currBest:
                    currBest = v
                    v = True
                else:
                    v = False
            if v:
                if stopFound:
                    return (tc + addLast)
                tb = tc
                if not tryFast:
                    n = 2
                else:
                    n = len(tb)
                if pruneGuards:
                    self.restart()
                    newtb = []
                    for a in tb:
                        if a[1]():
                            newtb.append(a)
                            try:
                                a[2]()
                            except KeyboardInterrupt as e:
                                raise e                                
                            except:
                                pass
                    tb = newtb
                reduced = True
                if verbose:
                    print "Reduced test length to",len(tb+addLast)
                break
        if not reduced:
            if n == len(tb):
                try:
                    test_after_reduce(self)
                except:
                    pass
                return tb + addLast
            n = min(n*2, len(tb))
            if verbose:
                print "Failed to reduce, increasing granularity to",n
        elif len(tb) == 1:
            try:
                test_after_reduce(self)
            except:
                pass
            v = pred([] + addLast)
            if amplify:
                if v > currBest:
                    v = True
                else:
                    v = False
            if v:
                return ([] + addLast)
            else:
                return (tb + addLast)

def tryCompose(tests, pred, pruneGuards = False, keepLast = False, verbose = True, rgen = None, amplify = False, combs = 1):
    newt = []
    for t in tests:
        newt.extend(t)
    newt = newt * combs
    return reduce(newt, pred, pruneGuards, keepLast, verbose, rgen, amplify)
            
def reductions(self, test, pred, pruneGuards = False, keepLast = False, verbose=True, recursive=1, useClasses=True, limit = None):
    # use recursive = -1 for infinite recursion (all tests)
    r = self.reduce(test, pred, pruneGuards = pruneGuards, keepLast = keepLast, verbose=verbose)
    reductions = [r]
    anyNew = True
    filterActs = set()
    impossibleSets = []
    analyzedCount = 0
    analyzed = []
    while anyNew:
        recursive = recursive - 1
        filterActs = set([])
        for r in reductions:
            for s in r:
                if not set([s]) in impossibleSets:
                    filterActs.add(s)
                
        anyNew = False
        sys.stdout.flush()
        for i in xrange(1,len(filterActs)):
            ncombos = 0
            #print "SIZE",i
            if verbose:
                print "ANALYZING SIZE",i,"COMBINATIONS"
            combs = combinations(filterActs,i)
            for c in combs:
                analyzedCount += 1
                #if (analyzedCount % 10) == 0:
                #    print "ANALYZED:",analyzedCount
                if (limit != None) and (analyzedCount > limit):
                    print "REDUCTION LIMIT EXCEEDED"
                    return reductions                
                cs = set(c)
                if cs in analyzed:
                    continue
                analyzed.append(cs)
                #print "COMBO:",map(lambda x:self.prettyName(x[0]), cs)
                skipCombo = False
                for iset in impossibleSets:
                    if filter(lambda x:x not in cs, iset) == []:
                        #print "SKIPPING, IMPOSSIBLE"
                        skipCombo = True
                        break
                if skipCombo:
                    continue
                skipCombo = False
                for r in reductions:
                    if filter(lambda x:x in cs, r) == []:
                        skipCombo = True
                        break
                if skipCombo:
                    continue
                ncombos += 1
                ac = map(self.actionClass,cs)
                if useClasses:
                    tfilter1 = filter(lambda x:self.actionClass(x) not in ac, test)
                    pfilter1 = pred(tfilter1)
                else:
                    pfilter1 = False
                tfilter2 = filter(lambda x:x not in cs, test)
                pfilter2 = pred(tfilter2)
                if pfilter1:
                    rfilter1 = self.reduce(tfilter1, pred, pruneGuards = pruneGuards, keepLast = keepLast, verbose=verbose)
                    if rfilter1 not in reductions:
                        if recursive != 0:
                            anyNew = True
                        if verbose:
                            print "ADDING NEW TEST OF LENGTH",len(rfilter1)
                        #print "ADDING NEW TEST OF LENGTH",len(rfilter1)                            
                        reductions.append(rfilter1)
                if pfilter2:
                    rfilter2 = self.reduce(tfilter2, pred, pruneGuards = pruneGuards, keepLast = keepLast, verbose=verbose)
                    if rfilter2 not in reductions:
                        if recursive != 0:
                            anyNew = True
                        if verbose:
                            print "ADDING NEW TEST OF LENGTH",len(rfilter2)
                        #print "ADDING NEW TEST OF LENGTH",len(rfilter2)                            
                        reductions.append(rfilter2)
                if (not pfilter1) and (not pfilter2):
                    if cs not in impossibleSets:
                        if verbose:
                            print "FOUND IMPOSSIBLE RESTRICTION:",map(lambda x:self.prettyName(x[0]),cs)
                        impossibleSets.append(cs)
            if verbose:
                print "ANALYZED",ncombos,"COMBINATIONS"
            #print "ANALYZED",ncombos,"COMBINATIONS"                
                    
    return reductions

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

def powerset(self,iterable):
    xs = list(iterable)
    return chain.from_iterable(combinations(xs,n) for n in range(len(xs)+1) )

def reduceEssentials(self, test, original, pred, pruneGuards = False, keepLast = False):
    possibleRemove = test
    if keepLast:
        possibleRemove = test[:-1]
    removals = list(self.powerset(possibleRemove))
    removals = sorted(removals, key=lambda x: len(x), reverse=True)
    workingRemovals = []
    failedRemovals = []
    for rset in removals:
        if rset == []:
            continue
        foundSuperset = False
        for (w, _) in workingRemovals:
            allPresent = True
            for r in rset:
                if r not in w:
                    allPresent = False
                    break
            if allPresent:
                foundSuperset = True
                break
        if foundSuperset:
            continue
        newOrig = filter(lambda x: x not in rset, original)
        if pred(newOrig):
            reduced = self.reduce(newOrig, pred, pruneGuards, keepLast)
            workingRemovals.append((rset,reduced))
        else:
            failedRemovals.append(rset)
    return (workingRemovals, failedRemovals)

def actionReplace(self,action,old,new):
    if action[0] == old:
        return self.__names[new]
    else:
        return action

def actionModify(self,action,old,new):
    name = action[0]
    newName = name.replace(old,new)
    return self.__names[newName]

def levDist(self,s1,s2):
    if len(s1) > len(s2):
        s1,s2 = s2,s1
    distances = range(len(s1) + 1)
    for index2,char2 in enumerate(s2):
        newDistances = [index2+1]
        for index1,char1 in enumerate(s1):
            if char1 == char2:
                newDistances.append(distances[index1])
            else:
                newDistances.append(1 + min((distances[index1],
                                             distances[index1+1],
                                             newDistances[-1])))
        distances = newDistances
    return distances[-1]

def getEnabled(self, test, checkEnabled):
    self.restart()
    enableChange = {}
    for i in xrange(0,len(test)):
        if checkEnabled:
            enableChange[i] = map(lambda x:x[0], self.enabled())
            self.safely(test[i])
        else:
            enableChange[i] = map(lambda x:x[0], self.actions())
    for i in xrange(0,len(test)):
        enableChange[i] = sorted(enableChange[i],key=lambda x:self.__orderings[x])
    return enableChange

def numReassigns(self, test):

    if not self.__noReassigns:
        return 0
    
    lhsPools = []
    reuses = []

    i = 0
    for s in test:
        if " = " in s[0]:
            lhs = s[0].split(" = ")[0]
            lhsp = self.poolUses(lhs)
            if len(lhsp) == 1:
                for p in self.poolUses(lhs):
                    if p in lhsPools:
                        reuses.append((i,p))
                    else:
                        lhsPools.append(p)
        i += 1
    return len(reuses)

def reduceLengthStep(self, test, pred, pruneGuards = False, keepLast = False, verbose = False, checkEnabled = False, distLimit = None):
    if verbose == "VERY":
        print "STARTING REDUCE LENGTH STEP"
    # Replace any action with another action, if that allows test to be further reduced
    enableChange = self.getEnabled(test,checkEnabled)

    reassignCount = self.numReassigns(test)
    
    for i in xrange(0,len(test)):
        name1 = test[i][0]
        if i not in enableChange:
            continue        
        for name2 in enableChange[i]:
            if name1 != name2:
                if (distLimit != None) and (self.levDist(name1, name2) > distLimit):
                    continue
                testC = test[0:i] + [self.__names[name2]] + test[i+1:]
                if (self.numReassigns(testC) <= reassignCount) and pred(testC):
                    rtestC = self.reduce(testC, pred, pruneGuards, keepLast, verbose=verbose,tryFast=True)
                    if len(rtestC) < len(test):
                        if verbose:
                            print "NORMALIZER: RULE ReduceAction: STEP",i,name1,"-->",name2,"REDUCING LENGTH FROM",len(test),"TO",len(rtestC)
                        return (True, rtestC)
    return (False, test)

def replaceAllStep(self, test, pred, pruneGuards = False, keepLast = False, verbose = False, checkEnabled = False, distLimit = None):
    if verbose == "VERY":
        print "STARTING REPLACE ALL STEP"    
    # Replace all occurrences of an action with a simpler action
    enableChange = self.getEnabled(test,checkEnabled)    

    reassignCount = self.numReassigns(test)
    
    donePairs = []
    for i in xrange(0,len(test)):
        name1 = test[i][0]
        if i not in enableChange:
            continue        
        for name2 in enableChange[i]:
            if (self.__orderings[name1] > self.__orderings[name2]) and ((name1,name2) not in donePairs):
                if (distLimit != None) and (self.levDist(name1, name2) > distLimit):
                    continue
                donePairs.append((name1,name2))
                testC = map(lambda x: self.actionReplace(x,name1,name2), test)
                if (self.numReassigns(testC) <= reassignCount) and pred(testC):
                    if verbose:
                        print "NORMALIZER: RULE SimplifyAll:",name1,"-->",name2
                    return (True, testC)
    return (False, test)

def replacePoolStep(self, test, pred, pruneGuards = False, keepLast = False, verbose = False, checkEnabled = False, distLimit = None):
    if verbose == "VERY":
        print "STARTING REPLACE POOL STEP"        
    # Replace pools with lower-numbered pools

    pools = []
    for s in test:
        for p in self.poolUses(s[0]):
            if p not in pools:
                pools.append(p)

    reassignCount = self.numReassigns(test)                

    # First try the simple version:

    if self.__noReassigns:
    
        for (p,i) in pools:
            for n in xrange(0,int(i)):
                new = p.replace("["+i+"]","[" + str(n) + "]")    
                testC = map(lambda x: self.actionModify(x,p,new), test)
                if (testC != test) and (self.numReassigns(testC) <= reassignCount) and pred(testC):
                    if verbose:
                        print "NORMALIZER: RULE ReplacePool:",p,"WITH",new
                    return (True, testC)    

        # Remained of this code is now not needed, probably, due to noReassignRule
        return (False, test)
    
    # Reduce number of pools but may need to move assignment to a later position, or only change after the position
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
                newPrefix = map(lambda x: self.actionModify(x,p,new), prefix)
                newSuffix = map(lambda x: self.actionModify(x,p,new), suffix)                
                testC = newPrefix + newSuffix
                if (testC != test) and (self.numReassigns(testC) <= reassignCount) and pred(testC):
                    if verbose:
                        if pos == 0:
                            print "NORMALIZER: RULE ReplacePool:",p,"WITH",new
                        else:
                            print "NORMALIZER: RULE ReplaceMovePool:",p,"WITH",new," -- MOVED TO",pos
                    return (True, testC)
                # Not possible, try with only replacing between pos and pos2
                for pos2 in xrange(len(test),pos,-1):
                    prefix = test[:pos]
                    suffix = map(lambda x: self.actionModify(x,p,new), test[pos:pos2])
                    testC = prefix + suffix + test[pos2:]
                    if (testC != test) and (self.numReassigns(testC) <= reassignCount) and pred(testC):
                        if verbose:
                            print "NORMALIZER: RULE ReplacePool:",p,"WITH",new,"FROM",pos,"TO",pos2
                        return (True, testC)
    return (False, test)


def replaceSingleStep(self, test, pred, pruneGuards = False, keepLast = False, verbose = False, checkEnabled = False, distLimit = None):
    if verbose == "VERY":
        print "STARTING REPLACE SINGLE STEP"        
    # Replace any single action with a lower-numbered action
    enableChange = self.getEnabled(test,checkEnabled)    

    reassignCount = self.numReassigns(test)
    
    for i in xrange(0,len(test)):
        name1 = test[i][0]
        if i not in enableChange:
            continue        
        for name2 in enableChange[i]:
            if self.__orderings[name1] > self.__orderings[name2]:
                if (distLimit != None) and (self.levDist(name1, name2) > distLimit):
                    continue
                testC = test[0:i] + [self.__names[name2]] + test[i+1:]
                if (self.numReassigns(testC) <= reassignCount) and pred(testC):
                    if verbose:
                        print "NORMALIZER: RULE SimplifySingle: STEP",i,name1,"-->",name2
                    return (True, testC)
    return (False, test)

def swapPoolStep(self, test, pred, pruneGuards = False, keepLast = False, verbose = False, checkEnabled = False, distLimit = None):
    if verbose == "VERY":
        print "STARTING SWAP POOL STEP"        
    # Swap two pool uses in between two positions, if this lowers the minimal action ordering between them
    pools = []
    for s in test:
        for p in self.poolUses(s[0]):
            if p not in pools:
                pools.append(p)

    reassignCount = self.numReassigns(test)
                
    swaps = []
    for (p1,i1) in pools:
        for (p2,i2) in pools:
            for pos1 in xrange(0,len(test)):
                for pos2 in xrange(len(test),pos1,-1):
                    if (p1 != p2) and (p1.split("[")[0] == p2.split("[")[0]):
                        p1new = p1.replace("[" + i1 + "]", "[" + i2 + "]")
                        p2new = p2.replace("[" + i2 + "]", "[" + i1 + "]")
                        p2newTemp = p2.replace("[" + i2 + "]", "[**]")
                        tempTest = map(lambda x:(x[0].replace(p2,p2newTemp),x[1],x[2]), test[pos1:pos2])
                        tempTest2 = map(lambda x:(x[0].replace(p1,p1new),x[1],x[2]), tempTest)
                        testC = test[:pos1] + map(lambda x: self.actionModify(x,p2newTemp,p2new), tempTest2) + test[pos2:]
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
                            if (self.numReassigns(testC) <= reassignCount) and pred(testC):
                                if verbose:
                                    print "NORMALIZER: RULE SwapPool:",p1,"AND",p2,"BETWEEN STEP",pos1,"AND",pos2
                                return (True, testC)
    return (False, test)

def opaque(self):
    return self.__opaque

def uniqueVals(self):
    ss = self.shallowState()
    uvals = []
    for (pool, vals) in ss:
        if pool not in self.__opaque:
            for v in vals.values():
                if v != None:
                    if (pool, str(v)) not in uvals:
                        uvals.append((pool,str(v)))
    return uvals

def coversUnique(self, val, catchUncaught=False):
    def coverPred(test):
        try:
            self.replay(test, catchUncaught)
        except KeyboardInterrupt as e:
            raise e            
        except:
            pass
        uv = self.uniqueVals()
        return val in uv
    return coverPred

def noReassignStep(self, test, pred, pruneGuards = False, keepLast = False, verbose = False, checkEnabled = False, distLimit = None):
    if not self.__noReassigns:
        return (False, test)
    
    if verbose == "VERY":
        print "STARTING NOREASSIGNS STEP"
    # Replace reassignments with fresh variables
    pools = []
    lhsPools = []
    reuses = []

    i = 0
    for s in test:
        if " = " in s[0]:
            lhs = s[0].split(" = ")[0]
            lhsp = self.poolUses(lhs)
            if len(lhsp) == 1:
                for p in self.poolUses(lhs):
                    if p in lhsPools:
                        reuses.append((i,p))
                    else:
                        lhsPools.append(p)
        for p in self.poolUses(s[0]):
            if p not in pools:
                pools.append(p[0])
        i += 1

    for (i,pu) in reuses:
        prefix = test[0:i]
        (p,pnum) = pu
        newp = None
        for ni in xrange(0,self.__psize[p.split("[")[0].replace(self.__poolPrefix,"")]):
            if int(ni) == int(pnum):
                continue
            tnewp = p.replace("[" + str(pnum) + "]","[" + str(ni) + "]")
            print "REPLACING",tnewp,ni,p,pnum
            if tnewp not in pools:
                newp = tnewp
                break
        if newp == None:
            continue
        if verbose:
            print "NORMALIZER: RULE NoReassigns:",i,test[i][0],p,"TO",newp
        suffix = []
        for s in test[i:]:
            suffix.append(self.actionModify(s,p,newp))
        return (True, prefix+suffix)
            
    return (False, test)

def swapActionOrderStep(self, test, pred, pruneGuards = False, keepLast = False, verbose = False, checkEnabled = False, distLimit = None):
    if verbose == "VERY":
        print "STARTING SWAP ACTION ORDER STEP"        
    # Try to swap any out-of-order actions
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
                        if verbose:
                            print "NORMALIZER: RULE SwapAction:",i,test[i][0],"WITH STEP",j,test[j][0]
                        return (True, testC)
    return (False, test)

def clearNormalizationCache(self):
    self.__simplifyCache = {}

def swapPools(self,test,p1,p2,after=0):
    poolsByLength = sorted(self.__pools, key = len, reverse=True)
    tPrefix = test[:after]
    test = test[after:]
    p1new = self.__poolPrefix + p1
    p2new = self.__poolPrefix + p2
    for p in poolsByLength:
        if p in p1new:
            p1new = p + "[" + p1new.split(p)[1] + "]"
    for p in poolsByLength:
        if p in p2new:
            p2new = p + "[" + p2new.split(p)[1] + "]"
    newTest = map(lambda x: x[0].replace(p1new,"!!P1NEW!!"), test)
    newTest = map(lambda x: x.replace(p2new,p1new), newTest)
    newTest = map(lambda x: x.replace("!!P1NEW!!",p2new), newTest)
    newTest = map(lambda x: self.__names[x], newTest)
    return tPrefix+newTest

def alphaConvert(self, test):
    """
    This ONLY performs renaming of pools to lowest values possible; it CAN in theory cause worse normalization.
    """
    count = {}
    changed = True
    while changed:
        changed = False
        for p in self.__pools:
            count[p] = 0
        for s in test:
            lhs = s[0].split(" = ")[0]
            lhsp = self.poolUses(lhs)
            for (p,n) in lhsp:
                basep = p.split("[")[0]
                if count[basep] < int(n):
                    p1new = p
                    p2new = p.replace(n,str(count[basep]))
                    #print "REPLACING",p1new,"WITH",p2new
                    newTest = map(lambda x: x[0].replace(p1new,"!!P1NEW!!"), test)
                    newTest = map(lambda x: x.replace(p2new,p1new), newTest)
                    newTest = map(lambda x: x.replace("!!P1NEW!!",p2new), newTest)
                    newTest = map(lambda x: self.__names[x], newTest)
                    test = newTest
                    #self.prettyPrintTest(test)
                    count[basep] += 1
                    changed = True
                    break
                else:
                    count[basep] += 1
            if changed:
                break
    return test
    
def normalize(self, test, pred, pruneGuards = False, keepLast = False, verbose = False, speed = "FAST", checkEnabled = False, distLimit = None, reorder=True,
              noReassigns = False, useCache = True):
    """
    Attempts to produce a normalized test case
    """
    try:
        test_before_normalize(self)
    except:
        pass

    if noReassigns:
        self.__noReassigns = True
    else:
        self.__noReassigns = False
    
    # Check the cache
    stest = self.captureReplay(test)
    if useCache and (stest in self.__simplifyCache):
        if verbose:
            print "NORMALIZER: FOUND TEST IN CACHED RESULTS"
        return self.__simplifyCache[stest]
    history = [stest]
        
    # Turns off requirement that you can't initialize an unused variable, allowing reducer to take care of redundant assignments
    #self.relax()
             
    # Default speed is fast, if speed not recognized
    simplifiers = [self.noReassignStep, self.replaceAllStep, self.replacePoolStep, self.replaceSingleStep, self.swapPoolStep, self.swapActionOrderStep, self.reduceLengthStep]
    #simplifiers = [self.noReassignStep, self.replaceAllStep, self.replaceSingleStep, self.swapActionOrderStep, self.reduceLengthStep]
    # Default approach tries a reduce after any change
    reduceOnChange = True
    if speed == "SLOW":
        simplifiers = [self.reduceLengthStep, self.replaceAllStep, self.replacePoolStep, self.replaceSingleStep, self.swapPoolStep, self.swapActionOrderStep]
    elif speed == "ONEREDUCE":
        # Runs one attempt at length reduction before normal simplification, without reduction step
        (changed, test) = self.reduceLengthStep(test, pred, pruneGuards, keepLast, verbose, checkEnabled, distLimit)
        if changed:
            stest = self.captureReplay(test)
            history.append(stest)
        simplifiers = [self.replaceAllStep, self.replacePoolStep, self.replaceSingleStep, self.swapPoolStep, self.swapActionOrderStep]
    elif speed == "MEDIUM":
        # Runs one attempt at length reduction before normal simplification
        (changed, test) = self.reduceLengthStep(test, pred, pruneGuards, keepLast, verbose)
        if changed:
            stest = self.captureReplay(test)
            history.append(stest)
    elif speed == "VERYFAST":
        reduceOnChange = False
        if distLimit == None:
            distLimit = 3 # maximum of 3 char change when replacing actions!  allows numeric switches, simple pool modifications, but very few method changes
    elif speed == "VERYFASTREDUCE":
        reduceOnChange = True
        if distLimit == None:
            distLimit = 3 # maximum of 3 char change when replacing actions!  allows numeric switches, simple pool modifications, but very few method changes            

    numChanges = 0
    changed = True
    stests = {}
    while changed:
        stest = self.captureReplay(test)
        assert (stest not in stests)
        stests[stest] = True
        changed = False
        if reorder:
            newSimplifiers = list(simplifiers)
        for s in simplifiers:
            oldTest = test
            (changed, test) = s(test, pred, pruneGuards, keepLast, verbose, checkEnabled, distLimit)
            if changed:
                if reduceOnChange:
                    test = self.reduce(test, pred, pruneGuards, keepLast, verbose=verbose, tryFast=True)
                if verbose:
                    self.prettyPrintTest(test)
                stest = self.captureReplay(test)
                if useCache and (stest in self.__simplifyCache):
                    if verbose:
                        print "NORMALIZER: FOUND TEST IN CACHED RESULTS"
                    result = self.__simplifyCache[stest]
                    for t in history:
                        self.__simplifyCache[t] = result
                    #self.stopRelax()
                    return result                
                history.append(stest)
                if reorder:
                    simplifiers = newSimplifiers
                break
            elif reorder:
                newSimplifiers.remove(s)
                newSimplifiers.append(s)

    # No changes, this is 1-simple (fix-point)
    try:
        test_after_normalize(self)
    except:
        pass

    #self.stopRelax()
    # restore normal TSTL semantics!

    # Update the simplification cache and return
    if useCache:
        for t in history:
            self.__simplifyCache[t] = test    
    return test

def freshSimpleVariants(self, name, previous, replacements):
#    print "FINDING FRESH SIMPLES FOR",name
    prevNames = map(lambda x:x[0], previous)
    prevNames.reverse()
    lastAppear = []
    eqFind = name.find("=")
    if eqFind != -1:
        poolAssign = name[0:eqFind-1]
    else:
        poolAssign = None
    pools = self.poolUses(name)
    lastAppearMap = {}
    for (p,i) in pools:
        for n in prevNames:
            if p[0:p.find("[")] in self.__consts:
                if n.find(p + " = ") == -1:
                    continue
            lastAppearMap[p] = [n]
            break
        skeys = replacements.keys()
        skeys = filter(lambda x: x < len(previous), skeys)
        skeys = sorted(skeys, reverse = True)
        for i in skeys:
#            print "i = ",i
            foundAny = False
            for r in replacements[i]:
                if p[0:p.find("[")] in self.__consts:
                    if r.find(p + " = ") == -1:
                        continue
                foundAny = True
                if p in lastAppearMap:
                    lastAppearMap[p].append(r)
                else:
                    lastAppearMap[p] = [r]
            if foundAny:
                break
    for n in lastAppearMap:
        lastAppear.extend(lastAppearMap[n])
#    print "LAST APPEAR = ",lastAppear
    freshSimples = []
    for (p,i) in pools:
        if p == poolAssign:
            continue
        for n in self.__names:
            if n in lastAppear:
                continue
            if (p + " = ") in n:
                uses = self.poolUses(n[n.find("=")+1:])
                if uses == []:
                    freshSimples.append([self.__names[n],self.__names[name]])
    freshSimples = sorted(freshSimples,key = lambda x:self.__orderings[x[0][0]])
    return freshSimples

def generalize(self, test, pred, pruneGuards = False, keepLast = False, verbose = False, checkEnabled = False, distLimit = None,
               returnCollect = False, collected = None, depth = 0, silent=False, targets = None, fresh=True):

    #print self.__consts
    
    if collected is None:
        collected = {}

    newCollected = {}
        
    # Change so double assignments are allowed
    #self.relax()

    enableChange = self.getEnabled(test,checkEnabled)
    
    canReplace = {}
    canSwap = {}
    canMakeSimple = {}
    for i in xrange(0,len(test)):
        canSwap[i] = []
    for i in xrange(0,len(test)):
        canReplace[i] = []
        canMakeSimple[i] = []
        if i not in enableChange:
            continue
        for a in enableChange[i]:
            if (distLimit != None) and (self.levDist(a, test[i][0]) > distLimit):
                continue
            if a != test[i][0]:
                testC = test[:i] + [self.__names[a]] + test[i+1:]
                if pred(testC): # and self.allEnabled(testC):
                    if returnCollect:
                        stestC = self.captureReplay(testC)
                        if stestC not in collected:
                            collected[stestC] = True
                            newCollected[stestC] = True                            
                        if stestC in targets:
                            #self.stopRelax()
                            return (True, stestC, dict(collected))                                                    
                    canReplace[i].append(a)
        for j in xrange(i+1,len(test)):
            if i == j or test[i][0] == test[j][0]:
                continue
            testC = test[:i]+[test[j]]+test[i+1:j]+[test[i]]+test[j+1:]
            if pred(testC): # and self.allEnabled(testC):
                if returnCollect:
                    stestC = self.captureReplay(testC)
                    if stestC not in collected:
                        collected[stestC] = True
                        newCollected[stestC] = True                        
                        if stestC in targets:
                            #self.stopRelax()
                            return (True, stestC, dict(collected))                        
                canSwap[i].append(j)
                canSwap[j].append(i)
        if fresh:
            for v in self.freshSimpleVariants(test[i][0],test[:i],canReplace):
                #print "="*50
                #print "FRESH SIMPLE, i = ",i
                testC = test[:i] + v + test[i+1:]
                #self.prettyPrintTest(testC)                
                if pred(testC) and self.allEnabled(testC):
                    #print "SUCCESS!"
                    canMakeSimple[i].append(v)
    if not silent:
        noOrder = []
        endSwappable = -1
        for i in xrange(0,len(test)):
            if endSwappable >= i:
                continue
            foundSwap = False
            for j in xrange(len(test)-1,i,-1):
                allSwappable = True
                for k1 in xrange(i,j+1):
                    for k2 in xrange(k1+1,j+1):
                            if k2 not in canSwap[k1]:
                                    allSwappable = False
                                    break
                    if not allSwappable:
                        break
                if allSwappable:
                    noOrder.append((i,j))
                    for k1 in xrange(i,j+1):
                        for k2 in xrange(i,j+1):
                            if k2 in canSwap[k1]:
                                canSwap[k1].remove(k2)
                    endSwappable = j
                    break
        for i in xrange(0,len(test)):
            for (begin,end) in noOrder:
                if i == begin:
                    print "#["
            pn = self.prettyName(test[i][0])
            spaces = " " * (90-len(pn)-len(" # STEP"))
            print self.prettyName(test[i][0]),spaces,"# STEP",i
            if canReplace[i] != []:
                firstRep = None
                lastRep = None
                for rep in canReplace[i]:
                    if firstRep == None:
                        firstRep = rep
                        lastRep = rep
                    elif self.__orderings[rep] != (self.__orderings[lastRep] + 1):
                        if firstRep == lastRep:
                            print "#  or",self.prettyName(firstRep)
                        else:
                            print "#  or",self.prettyName(firstRep)
                            print "#   -",self.prettyName(lastRep)
                        firstRep = rep
                        lastRep = rep
                    else:
                        lastRep = rep
                if firstRep == lastRep:
                    print "#  or",self.prettyName(firstRep)
                else:
                    print "#  or",self.prettyName(firstRep)
                    print "#   -",self.prettyName(lastRep)
            if canMakeSimple[i] != []:
                for v in canMakeSimple[i]:
                    print "#  or ("
                    for s in v[:-1]:
                        print "#     ",self.prettyName(s[0]),";"
                    print "#     ",self.prettyName(v[-1][0])
                    print "#     )"
            if canSwap[i] != []:
                if len(canSwap[i]) == 1:
                    print "#  swaps with step",
                else:
                    print "#  swaps with steps",
                for j in canSwap[i]:
                    print j,
                print
            for (begin,end) in noOrder:
                if i == end:
                    print "#] (steps in [] can be in any order)"
    # Restore semantics
    #self.stopRelax()
    if returnCollect:
        if depth == 0:
            return (False, None, dict(collected))
        else:
            allCollected = dict(collected)
            for c in newCollected:
                (found, stest, cGen) = self.generalize(self.replayable(c), pred, pruneGuards, keepLast, verbose, checkEnabled,
                                                distLimit, returnCollect=True, collected = allCollected,
                                                depth = depth-1, silent=True, targets = targets)
                for c2 in cGen:
                    if c2 not in allCollected:
                        allCollected[c2] = True
                if found == True:
                    return (True, stest, dict(allCollected))
            return (False, None, dict(allCollected))

def relax(self):
    self.__relaxUsedRestriction = True

def stopRelax(self):
    self.__relaxUsedRestriction = False

def moduleFiles(self):
    # This code is not very robust, tried to find locations for code coverage and avoid system library code
    files = []
    for m in self.__importModules:
        try:
            files.extend(m.__path__)
        except AttributeError:
            f = m.__file__
            if f.find("python2.7") != -1:
                # if it is a library file, grab the entire directory
                f = os.path.dirname(m.__file__)
                if f.split("/")[-1] in ["python2.7", "lib-dynload"]:
                    # In general don't report coverage on Python core modules
                    continue
            files.append(f.replace(".pyc",".py"))
    print "FILES:",files
    return files
        
