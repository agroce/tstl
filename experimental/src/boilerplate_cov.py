def __updateCov(self):
    self.__newBranches = set()
    self.__newStatements = set()
    self.__newCurrBranches = set()
    self.__newCurrStatements = set()
    for src_file, arcs in self.__cov.collector.get_arc_data().iteritems():
        for arc in arcs:
            branch = (src_file, arc)
            if branch not in self.__allBranches:
                self.__allBranches.add(branch)
                self.__newBranches.add(branch)
            if branch not in self.__currBranches:
                self.__currBranches.add(branch)
                self.__newCurrBranches.add(branch)
    for src_file, lines in self.__cov.collector.get_line_data().iteritems():
        for line in lines:
            statement = (src_file, line)
            if statement not in self.__allStatements:
                self.__allStatements.add(statement)
                self.__newStatements.add(statement)
            if statement not in self.__currStatements:
                self.__currStatements.add(branch)
                self.__newCurrStatements.add(branch)        

def resetCov(self):
    self.__cov.collector.reset()

def report(self):
    self.__cov.html_report()

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

def coversStatements(self, statements, catchUnCaught=False):
    def coverPred(test):
        try:
            self.replay(test, catchUnCaught)
        except:
            pass
        cs = self.currStatements()
        for s in statements:
            if s not in cs:
                return False
        return True
    return coverPred
