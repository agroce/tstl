from playdom import GameState

def initializeGame(p, k, s):
	g = GameState()
	g.initializeGame(p, k, s)
	return g

def buyCard(c,g):
	return g.currentPlayer().buy(c,0)

def endTurn(g):
	g.nextPlayer().startTurn()

def isGameOver(g):
	g.isGameOver()

def numHandCards(g):
	return len(g.currentPlayer().hand)

def handCard(i, g):
	if i >= numHandCards(g):
		return -1
	return g.currentPlayer().hand[i]

def whoseTurn(g):
	return g.playerTurn

def scoreFor(i, g):
	g.players[i].score()

def playCard(c, ch1, ch2, ch3, g):
	return g.currentPlayer().playCard(c, ch1, ch2, ch3, g)






