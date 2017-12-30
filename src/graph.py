import sys
from graphviz import Digraph
import random
import os

def breakByNumber(s):
    breaks = []
    curr = ""
    for c in range(0,len(s)):
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

def breaksApart(s):
    breaks1 = []
    s2 = str(s)
    while "<[" in s2:
        p1 = s2.find("<[")
        p2 = s2.find("]>")
        breaks1.append(s2[:p1])
        breaks1.append(s2[p1:p2+2])
        s2 = s2[p2+2:]
    breaks1.append(s2)
    breaks2 = []
    for b1 in breaks1:
        if b1.find("<[") != 0:
            breaks3 = breakByNumber(b1)
            for b3 in breaks3:
                breaks2.append(b3)
        else:
            breaks2.append(b1)
    return breaks2

def intOrNone(v):
    try:
        return int(v)
    except:
        return None

def rangeOrNone(v):
    try:
        if "<[" in v:
            vs = v.split("..")
            return (int(vs[0][2:]),int(vs[1][:-2]))
        return None
    except:
        return None
    
def merge(s1,s2):
    b1 = breaksApart(s1)
    b2 = breaksApart(s2)
    if len(b1) != len(b2):
        return None
    merged = ""
    diverged = False
    for i in range(len(b1)):
        if b1[i] == b2[i]:
            merged += b1[i]
        elif not diverged:
            diverged = True
            v1 = intOrNone(b1[i])
            v2 = intOrNone(b2[i])
            r1 = rangeOrNone(b1[i])
            r2 = rangeOrNone(b2[i])
            if (v1 != None):
                if (v2 != None): # 2 values
                    if (min(v1,v2) + 1 == max(v1,v2)):
                        merged += "<[" + str(min(v1,v2)) + ".." + str(max(v1,v2)) + "]>"
                    else:
                        return None
                elif (r2 != None): # value and range
                    (low2,high2) = r2
                    if (v1 == (low2 - 1)) or (v1 == (high2 + 1)):
                        merged += "<[" + str(min(v1,low2)) + ".." + str(max(v1,high2)) + "]>"
                    else:
                        return None
            elif (r1 != None):
                if (v2 != None): # range and value
                    (low1,high1) = r1
                    if (v2 == (low1 - 1)) or (v2 == (high1 + 1)):
                        merged += "<[" + str(min(v2,low1)) + ".." + str(max(v2,high1)) + "]>"
                    else:
                        return None
                elif (r2 != None): # range and range
                    (low1,high1) = r1
                    (low2,high2) = r2
                    if ((high1+1) == low2) or ((high2+1) == low1):
                        merged += "<[" + str(min(low1,low2)) + ".." + str(max(high1,high2)) + "]>"
                    else:
                        return None
                else:
                    return None
            else:
                return None
        else:
            return None
    return merged

def collapse(strings):
    changed = True
    cstrings = list(strings)
    while changed:
        changed = False
        for s1 in cstrings:
            for s2 in cstrings:
                if (s1 == s2):
                    continue
                m = merge(s1,s2)
                if m != None:
                    cstrings.remove(s1)
                    cstrings.remove(s2)
                    cstrings.append(m)
                    changed = True
                    break                
            if changed:
                break
    return cstrings
                

# Appending current working directory to sys.path
# So that user can run randomtester from the directory where sut.py is located
current_working_dir = os.getcwd()
sys.path.append(current_working_dir)

if not "--help" in sys.argv:
    import sut as SUT

def main():

    if "--help" in sys.argv:
        print("Usage:  tstl_graph <outfile> <depth> <width> [<seed>] [<traces> (default 1)] [<skip> (default none)]")
        sys.exit(0)
    
    outfile = sys.argv[1]
    depth = int(sys.argv[2])
    k = int(sys.argv[3])
    if len(sys.argv) > 5:
        seed = int(sys.argv[4])
        random.seed(seed)
    if len(sys.argv) > 5:
        traces = int(sys.argv[5])
    else:
        traces = 1
    if len(sys.argv) > 6:
        skiplen = int(sys.argv[6])
    else:
        skiplen = -1

    print("Producing graph of",traces,"traces with depth",depth,"and width",k,"starting from",skiplen)

    dot = Digraph(comment="Depth " + str(depth))

    for i in range(0,traces):
        d = 0
        s = 0
        state = str(i) + "\<init\>"
        dot.node(state, "\<init\>", penwidth="3.0",shape='box')

        t = SUT.sut()
        t.restart()

        s = 0

        states = []

        d = 1

        last = state

        midFlip = True

        sd = 0
        while sd <= skiplen:
            nexta = t.enabled()
            act = random.choice(nexta)
            t.safely(act)
            sd += 1

        while d <= depth:
            nexta = t.enabled()
            act = random.choice(nexta)
            aname = t.prettyName(act[0])
            nexts = [t.prettyName(a[0]) for a in nexta]
            eqnexts = nexts
            eqnexts = collapse(eqnexts)
            eqnexts = [x for x in eqnexts if x != aname]
            random.shuffle(eqnexts)
            eqnexts = eqnexts[-(k-1):]
            mid = len(eqnexts) / 2
            if ((len(eqnexts) % 2) != 0):
                if midFlip:
                    mid = mid + 1
                midFlip = not midFlip
            eqnexts = eqnexts[:mid] + [aname] + eqnexts[mid:]
            for name in eqnexts:
                s += 1
                state = str(i) + "s" + str(s)
                if name == aname:
                    newLast = state
                    dot.node(state,name,penwidth="3.0",shape='box')
                    dot.edge(last,state,penwidth="3.0")            
                else:
                    dot.node(state,name,fontsize="10.0")
                    dot.edge(last,state)
            last = newLast
            t.safely(act)
            d += 1

    dot.render(outfile,view=True)
