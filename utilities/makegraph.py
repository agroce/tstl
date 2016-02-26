import sut
import sys
from graphviz import Digraph
import random

def breakByNumber(s):
    breaks = []
    curr = ""
    for c in xrange(0,len(s)):
        if curr == "":
            curr += s[c]
        elif (s[c] in ['0','1','2','3','4','5','6','7','8','9']) == (curr[-1] in ['0','1','2','3','4','5','6','7','8','9']):
            curr += s[c]
        else:
            breaks.append(curr)
            curr = s[c]
    if curr != "":
        breaks.append(curr)
    return breaks

def breakByRanges(s):
    breaks = []
    s2 = str(s)
    while "<[" in s2:
        p1 = s2.find("<[")
        p2 = s2.find("]>")
        breaks.append(s2[:p1])
        breaks.append(s2[p1+2:p2])
        s2 = s2[p2+2:]
    if s2 != "":
        breaks.append(s2)
    return breaks

def intOrNone(v):
    try:
        return int(v)
    except:
        return None

def tempMatches(template,list):
    nonMatch = []
    abstractions = []
    tbreaks = breakByNumber(template)
    indices = {}
    p = 0
    for i in tbreaks:
        if intOrNone(i) != None:
            indices[p] = [intOrNone(i)]
            p += 1
    tindices = filter(lambda x: x != None, map (lambda y: intOrNone(y), tbreaks))
    allindices = [tindices]
    for i in list:
        breaks = breakByNumber(i)
        if len(breaks) != len(tlist):
            nonMatch.append(i)
        else:
            badMatch = False
            bindices = []
            for b in xrange(len(breaks)):
                if breaks[i] != tbreaks[i]:
                    v = intOrNone(breaks[i])
                    tv = intOrNone(tbreaks[i])
                    if (v == None) or (tv == None):
                        badMatch = True
                        break
                    bindices.append(v)
        allindices.append(bindices)
    maxes = list(tindices)
    mins = list(tindices)
    for i in allindices:
        for j in len(i):
            if j[i] > maxes[i]:
                maxes[i] = j[i]
            if j[i] < mins[i]:
                mins[i] = j[i]                
    iranges = zip(mins,maxes)
    rangesets = [iranges]
    while changed:
        for irange in rangesets:
            return None
    

def merge1(s1,s2):
    alreadyDiverge = False
    b1 = breakByNumber(s1)
    b2 = breakByNumber(s2)
    if len(b1) != len(b2):
        return None
    news = ""
    for i in xrange(0,len(b1)):
        if b1[i] != b2[i]:
            if alreadyDiverge:
                return None
            try:
                v1 = int(b1[i])
                v2 = int(b2[i])
                alreadyDiverge = True
                if (v2 == (v1 + 1)):
                    news += "<[" + b1[i] + ".." + b2[i] + "]>"
                else:
                    return None
            except ValueError:
                return None
        else:
            news += b1[i]
    return news



def merge2(s1,s2):
    alreadyDiverge = False
    b1 = breakByRanges(s1)
    b2 = breakByRanges(s2)
    if len(b1) != len(b2):
        return None
    news = ""
    for i in xrange(0,len(b1)):
        if b1[i] != b2[i]:
            if alreadyDiverge:
                return None
            try:
                low1 = int(b1[i].split("..")[0])
                high1 = int(b1[i].split("..")[1])
                low2 = int(b2[i].split("..")[0])
                high2 = int(b2[i].split("..")[1])                                
                alreadyDiverge = True
                if (high1 + 1) == low2:
                    news += "<[" + str(low1) + ".." + str(high2) + "]>"
                else:
                    return None
            except ValueError:
                return None
        else:
            if ".." in b1[i]:
                news += "<[" + b1[i] + "]>"
            else:
                news += b1[i]
    return news

def merge3(s1,s2):
    alreadyDiverge = False
    b1 = breakByRanges(s1)
    b2 = breakByNumber(s2)
    matching = True
    news = ""
    while matching:
        matching = False
        if b1[0] == b2[0]:
            news += b1[0]
            b1 = b1[1:]
            b2 = b2[1:]
            matching = True
        elif b1[0].find(b2[0]) == 0:
            news += b2[0]
            b1[0] = b1[0].split(b2[0],1)[1]
            if b1[0] == "":
                b1 = b1[1:]
            b2 = b2[1:]
            matching = True
        elif b2[0].find(b1[0]) == 0:
            news += b1[0]            
            b2[0] = b2[0].split(b1[0],1)[1]
            if b2[0] == "":
                b2 = b2[1:]
            b2 = b1[1:]
            matching = True
    try:
        low1 = int(b1[0].split("..")[0])
        high1 = int(b1[0].split("..")[1])
        v2 = int(b2[0])
        if v2 == high1 + 1:
            news += "<[" + str(low1) + ".." + str(v2) + "]>"
        b1 = b1[1:]
        b2 = b2[1:]
        matching = True
        while matching and not ((b1 == []) and (b2 == [])):
            matching = False
            if b1[0] == b2[0]:
                news += b1[0]
                b1 = b1[1:]
                b2 = b2[1:]
                matching = True
            elif b1[0].find(b2[0]) == 0:
                news += b2[0]
                b1[0] = b1[0].split(b2[0],1)[1]
                if b1[0] == "":
                    b1 = b1[1:]
                b2 = b2[1:]
                matching = True
            elif b2[0].find(b1[0]) == 0:
                news += b1[0]            
                b2[0] = b2[0].split(b1[0],1)[1]
                if b2[0] == "":
                    b2 = b2[1:]
                b2 = b1[1:]
                matching = True
        if (b1 != []) or (b2 != []):
            return None
    except:
        return None
    return news

def collapse(strings):
    changed = True
    cstrings = list(strings)
    while changed:
        changed = False
        for s1 in cstrings:
            for s2 in cstrings:
                if (s1 == s2):
                    continue
                m = merge1(s1,s2)
                if m != None:
                    print "MERGED1",s1,"AND",s2,"INTO",m
                    cstrings.remove(s1)
                    cstrings.remove(s2)
                    cstrings.append(m)
                    changed = True
                    break
                m = merge2(s1,s2)
                if m != None:
                    print "MERGED2",s1,"AND",s2,"INTO",m
                    cstrings.remove(s1)
                    cstrings.remove(s2)
                    cstrings.append(m)
                    changed = True
                    break
                m = merge3(s1,s2)
                if m != None:
                    print "MERGED3",s1,"AND",s2,"INTO",m
                    cstrings.remove(s1)
                    cstrings.remove(s2)
                    cstrings.append(m)
                    changed = True
                    break
            if changed:
                break
    return cstrings
                

outfile = sys.argv[1]
depth = int(sys.argv[2])
k = int(sys.argv[3])
seed = int(sys.argv[4])

random.seed(seed)

dot = Digraph(comment="Depth " + str(depth))

d = 0
s = 0
state = "\<init\>"
dot.node(state, state)

t = sut.sut()
t.restart()

s = 0

states = []

d = 1

last = state

while d <= depth:
    nexta = t.enabled()
    act = random.choice(nexta)
    aname = t.prettyName(act[0])
    nexts = map(lambda a: t.prettyName(a[0]), nexta)
    eqnexts = nexts
    eqnexts = collapse(eqnexts)
    eqnexts = filter(lambda x: x != aname, eqnexts)
    random.shuffle(eqnexts)
    print eqnexts
    eqnexts = eqnexts[-(k-1):]
    mid = len(eqnexts) / 2
    eqnexts = eqnexts[:mid] + [aname] + eqnexts[mid:]
    for name in eqnexts:
        s += 1
        state = "s" + str(s)
        dot.node(state,name)
        if name == aname:
            newLast = state
        dot.edge(last,state)
    last = newLast
    t.safely(act)
    d += 1

dot.render(outfile,view=True)
