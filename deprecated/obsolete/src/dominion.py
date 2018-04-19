from playdom import GameState

def initializeGame(p, k, s):
	g = GameState()
	g.initializeGame(p, k, s)
	return g

def buyCard(c,g):
	return g.currentPlayer().buy(c,0)

def thehand(g):
	return g.currentPlayer().hand

def endTurn(g):
	g.currentPlayer().discard.extend(g.currentPlayer().hand)
	g.currentPlayer().hand = []
	for c in xrange(0,5):
		g.currentPlayer().drawCard()
	return g.nextPlayer().startTurn()

def isGameOver(g):
	return g.isGameOver()

def numHandCards(g):
	return len(g.currentPlayer().hand)

def handCard(i, g):
	if i >= numHandCards(g):
		return -1
	return g.currentPlayer().hand[i]

def whoseTurn(g):
	return g.playerTurn

def scoreFor(i, g):
	if i >= len(g.players):
		return -1
	return g.players[i].score()

def playCard(c, ch1, ch2, ch3, g):
	return g.currentPlayer().playCard(c, ch1, ch2, ch3, g)






