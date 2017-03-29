mtext = '''      |
----- |
      |
 -----|
      *'''

mlist = []
for l in mtext.split("\n"):
   mlist.append(l)

def drawMaze(pos):
    print
    print "X"*20
    py = 0
    for l in mlist:
    	px = 0
    	for c in l:
	    if (px,py) == pos:
	       print "?",
	    else:
	       print c,
	    px += 1
	print
	py += 1
    print "X"*20	
	
        

def tryMove(m,pos):
    (x,y) = pos
    if m == "U":
       newPos = (x,y-1)
    elif m == "D":
       newPos = (x,y+1)
    elif m == "L":
       newPos = (x-1,y)
    elif m == "R":
       newPos = (x+1,y)
    else:
       return pos
    (x,y) = newPos
    if (x < 0) or (y < 0) or (y >= len(mlist)) or (x >= len(mlist[0])):
       return pos
    if mlist[y][x] == "*":
       assert False
    if mlist[y][x] != " ":
       return pos
    drawMaze(newPos)
    return newPos
