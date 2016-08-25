import sys

lengthCounts = {}

for f in sys.argv[1:]:
    currlen = None
    for l in open(f):
        if l[0:3] == "def":
            if currlen != None:
                if currlen in lengthCounts:
                    lengthCounts[currlen] += 1
                else:
                    lengthCounts[currlen] = 1
    
            currlen = -1
        else:
            if currlen == None:
                currlen = 0
            else:
                currlen += 1

for l in sorted(lengthCounts.keys()):
    print l,lengthCounts[l]
