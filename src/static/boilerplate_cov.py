def __updateCov(self,extendCov=False):
    if not extendCov:
        self.__newBranches = set()
        self.__newStatements = set()
    newCov = self.__cov.get_data()
    if self.__oldCovData == None:
        self.__oldCovData = coverage.CoverageData()
    self.__oldCovData.update(newCov)
    if newCov.measured_files() == None:
        return
    for src_file in newCov.measured_files():
        thisArcs = newCov.arcs(src_file)
        if thisArcs == None:
            continue # assume if we have arcs we have lines
        for arc in thisArcs:
            branch = (src_file, arc)
            if branch not in self.__allBranches:
                self.__allBranches.add(branch)
                self.__newBranches.add(branch)
                self.__newCurrBranches.add(branch)
            if branch not in self.__currBranches:
                self.__currBranches.add(branch)
        for line in newCov.lines(src_file):
            statement = (src_file, line)
            if statement not in self.__allStatements:
                self.__allStatements.add(statement)
                self.__newStatements.add(statement)
                self.__newCurrStatements.add(statement)
            if statement not in self.__currStatements:
                self.__currStatements.add(statement)

def silenceCoverage(self):
    self.__cov._warn_no_data = False
                                
def internalReport(self):
    print "TSTL INTERNAL COVERAGE REPORT:"
    if self.__oldCovData == None:
        return
    for src_file in self.__oldCovData.measured_files():
        adata = self.__oldCovData.arcs(src_file)
        print src_file,"ARCS:",len(adata),sorted(adata)
        for (f,a) in self.__allBranches:
            if f == src_file:
                if a not in adata:
                    print "WARNING:",a,"VISITED BUT MISSING FROM COVERAGEDATA"
        for a in adata:
            if (src_file,a) not in self.__allBranches:
                print "WARNING:",a,"IN COVERAGEDATA BUT NOT IN TSTL COVERAGE"
        ldata = list(set(self.__oldCovData.lines(src_file)))
        print src_file,"LINES:",len(ldata),sorted(ldata)
        for (f,l) in self.__allStatements:
            if f == src_file:
                if l not in ldata:
                    print "WARNING:",l,"VISITED BUT MISSING FROM COVERAGEDATA"
        for l in ldata:
            if (src_file,l) not in self.__allStatements:
                print "WARNING",l,"IN COVERAGEDATA BUT NOT IN TSTL COVERAGE"
    for (f,l) in self.__allStatements:
        if f not in self.__oldCovData.measured_files():
            print "WARNING:",(f,l),"IS NOT IN COVERAGEDATA"
    print "TSTL BRANCH COUNT:",len(self.__allBranches)                
    print "TSTL STATEMENT COUNT:",len(self.__allStatements)
                
def cleanCov(self):
    self.__newBranches = set()
    self.__newStatements = set()
    self.__currBranches = set()
    self.__currStatements = set()
    self.__newCurrBranches = set()
    self.__newCurrStatements = set()    
    if self.__oldCovData == None:
        self.__oldCovData = coverage.CoverageData()
    if self.__cov.get_data() == None:
        return
    self.__oldCovData.update(self.__cov.get_data())
    self.__cov.erase()
                    
def resetCov(self):
    self.__cov.erase()
    self.__oldCovData = None
    self.__allBranches = set()
    self.__allStatements = set()
    self.__newBranches = set()
    self.__newStatements = set()
    self.__currBranches = set()
    self.__currStatements = set()
    self.__newCurrBranches = set()
    self.__newCurrStatements = set()    

def report(self, filename):
    if self.__oldCovData != None:
        self.__oldCovData.write_file(filename)
        self.__cov.combine([filename])
    outf = open(filename,'w')
    r = -1
    try:
        r = self.__cov.report(morfs=self.__modules, file=outf)
    finally:
        outf.close()
        return r

def htmlReport(self, dir):
    if self.__oldCovData != None:
        self.__oldCovData.write_file(dir + "/.tmpcov")
        self.__cov.combine([dir + "/.tmpcov"])    
    r = -1
    try:
        r = self.__cov.html_report(morfs=self.__modules, directory=dir,
                                      title="TSTL Coverage Report")
    finally:
        return r

def allBranches(self):
    return self.__allBranches

def allStatements(self):
    return self.__allStatements

def currBranches(self):
    return self.__currBranches

def currStatements(self):
    return self.__currStatements

def newBranches(self):
    return self.__newBranches

def newStatements(self):
    return self.__newStatements

def newCurrBranches(self):
    return self.__newCurrBranches

def newCurrStatements(self):
    return self.__newCurrStatements

def startCoverage(self):
    self.__collectCov = True

def stopCoverage(self):
    self.__collectCov = False    

def coversBranches(self, branches, catchUncaught=False):
    def coverPred(test):
        try:
            self.replay(test, catchUncaught)
        except:
            pass
        cb = self.currBranches()
        for b in branches:
            if b not in cb:
                return False
        return True
    return coverPred

def coversStatements(self, statements, catchUncaught=False):
    def coverPred(test):
        try:
            self.replay(test, catchUncaught)
        except:
            pass
        cs = self.currStatements()
        for s in statements:
            if s not in cs:
                return False
        return True
    return coverPred

def coversAll(self, statements, branches, catchUncaught=False, checkProp=False):
    def coverPred(test):
        try:
            self.replay(test, catchUncaught=catchUncaught, checkProp=checkProp)
        except:
            pass
        cs = self.currStatements()
        for s in statements:
            if s not in cs:
                return False
        cb = self.currBranches()
        for b in branches:
            if b not in cb:
                return False
        return True
    return coverPred

def coversMore(self, statements, branches, catchUncaught=False, checkProp=False):
    def coverPred(test):
        try:
            self.replay(test, catchUncaught=catchUncaught, checkProp=checkProp)
        except:
            pass
        cs = self.currStatements()
        for s in statements:
            if s not in cs:
                return False
        cb = self.currBranches()
        for b in branches:
            if b not in cb:
                return False
        for b in cb:
            if b not in branches:
                return True
        for s in cs:
            if s not in statements:
                return True            
        return False
    return coverPred

def coversSame(self, test, catchUncaught=False, checkProp=False):
    self.replay(test,catchUncaught=catchUncaught,checkProp=checkProp)
    return self.coversAll(self.currStatements(), self.currBranches(), catchUncaught=catchUncaught, checkProp=checkProp)

def coversMoreThan(self, test, catchUncaught=False, checkProp=False):
    self.replay(test,catchUncaught=catchUncaught,checkProp=checkProp)
    return self.coversMore(self.currStatements(), self.currBranches(), catchUncaught=catchUncaught, checkProp=checkProp)
