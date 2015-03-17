import copy

currentCov = {}
totalCov = {}

def cover(string):
    if string in currentCov:
        currentCov[string] += 1
    else:
        currentCov[string] = 1
    if string in totalCov:
        totalCov[string] += 1
    else:
        totalCov[string] = 1        

def clearCoverage():
    global currentCov
    currentCov = {}

def getCoverage():
    return copy.copy(currentCov)

def setCoverage(c):
    currentCov = c

def getTotalCoverage():
    return totalCov
