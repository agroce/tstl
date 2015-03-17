# from enum import Enum
import sys
import random
from cardnames import CardName


class Card:

	def __init__(self,n,a,t,c):
		# self.name = n.name
		# self.value = n.value
		self.value = n
		self.action = a
		self.type = t
		self.cost = c
		self.embargoTokens = 0 
		self.count = -1

	def defaultAction(self,p, ch1, ch2, ch3, h):
		return -1

	def copper(self,p, ch1, ch2, ch3, h):
		# p.coin_bonus += 1
		return -1

	def silver(self,p, ch1, ch2, ch3, h):
		# p.coin_bonus += 2
		return -1

	def gold(self,p, ch1, ch2, ch3, h):
		# p.coin_bonus += 3
		return -1

	def adventurer(self, p, ch1, ch2, ch3, h):
		treasureCount = 0
		while treasureCount < 2:
			c = p.pickCard()
			if cards[c].type == 1:
				p.hand.append(c)
				treasureCount += 1
			else:
				p.discard.append(c)

		p.discardCard(CardName.adventurer)
		p.updateCoins()
		return 0

	def ambassador(self,p,ch1, ch2, ch3, h):
		if ch2 > 2 or ch2 < 0:
			return -1

		if ch1 > len(p.hand) or ch1 < 0:
			return -1

		card = p.hand[ch1]
		if p.hand.count(card) <= ch2:
			return -1

		p.discardCard(CardName.ambassador)

		for x in range(0,ch2):
			p.hand.remove(card)
			cards[card].count += 1

		for player in p.gameState.players:
			if player != p:
				player.gainCard(card,0)
		
		return 0

	def baron(self,p,ch1, ch2, ch3, h):
		p.numBuys += 1
		p.discardCard(CardName.baron)
		if p.hand.count(CardName.estate) > 0:
			if ch1 != 0:
				p.hand.remove(CardName.estate)
				p.coin_bonus += 4
				p.updateCoins()
				return 0

		p.gainCard(CardName.estate,0)
		if cards[CardName.estate].count <= 0:
			p.gameState.isGameOver()

		return 0
			


	def council_room(self,p,ch1, ch2, ch3, h):
		g = p.gameState
		for player in g.players:
			player.drawCard()

		p.drawCard()
		p.drawCard()
		p.drawCard()
		p.numBuys += 1
		p.discardCard(CardName.council_room)

	def cutpurse(self,p,ch1, ch2, ch3, h):
		p.coin_bonus += 2
		for player in p.gameState.players:
			if player != p:
				player.discardCard(CardName.copper)
		p.updateCoins()
		return 0

	def embargo(self,p,ch1, ch2, ch3, h):
		p.coin_bonus += 2
		cards[ch1].embargoTokens += 1

		p.hand.remove(CardName.embargo)
		p.updateCoins()


	def feast(self,p,ch1, ch2, ch3, h):
		# p.discard.pop()
		coins = p.coins
		p.coins = 5
		numBuys = p.numBuys
		r = p.buy(ch1,0)
		p.numBuys = numBuys
		p.updateCoins()

		p.hand.remove(CardName.feast)

		return r
		

	def mine(self,p,ch1, ch2, ch3, h):
		c = p.hand[ch1]
		if cards[c].type != 1:
			return -1

		if cards[ch2].type != 1:
			return -1
		if cards[c].cost + 3 > cards[ch2].cost:
			return -1

		p.hand.remove(c)
		p.hand.append(ch2)
		p.discardCard(CardName.mine)
		return 0

	def great_hall(self,p,ch1, ch2, ch3, h):
		p.numActions += 1
		p.drawCard()

		p.discardCard(CardName.great_hall)

		return 0

# adventurer,
#    ambassador, /* choice1 = hand#, choice2 = number to return to supply */
#    baron, /* choice1: boolean for discard of estate */
#    council_room,
#    cutpurse,
#    embargo, /* choice1 = supply# */
#    feast, /* choice1 is supply # of card gained) */
#    gardens,
#    great_hall,
#    mine, /* choice1 is hand# of money to trash, choice2 is supply# of


MAX_PLAYERS = 4
cards = {}
cards[CardName.curse] = Card(CardName.curse,Card.defaultAction,1,0)
cards[CardName.estate] = Card(CardName.estate,Card.defaultAction,0,2)
cards[CardName.duchy] = Card(CardName.duchy,Card.defaultAction,0,5)
cards[CardName.province] = Card(CardName.province,Card.defaultAction,0,8)
cards[CardName.copper] = Card(CardName.copper,Card.copper,1,0)
cards[CardName.silver] = Card(CardName.silver,Card.silver,1,3)
cards[CardName.gold] = Card(CardName.gold,Card.gold,1,6)
cards[CardName.adventurer] = Card(CardName.adventurer,Card.adventurer,2,6)
cards[CardName.ambassador] = Card(CardName.ambassador,Card.ambassador,9,3)
cards[CardName.baron] = Card(CardName.baron,Card.baron,9,4)
cards[CardName.council_room] = Card(CardName.council_room,Card.council_room,2,5)
cards[CardName.cutpurse] = Card(CardName.cutpurse,Card.cutpurse,9,4)
cards[CardName.embargo] = Card(CardName.embargo,Card.embargo,9,2)
cards[CardName.feast] = Card(CardName.feast,Card.feast,2,4)
cards[CardName.gardens] = Card(CardName.gardens,Card.defaultAction,9,4)
cards[CardName.great_hall] = Card(CardName.great_hall,Card.great_hall,9,3)
cards[CardName.mine] = Card(CardName.mine,Card.mine,2,5)
cards[CardName.minion] = Card(CardName.minion,Card.defaultAction,9,9)
cards[CardName.outpost] = Card(CardName.outpost,Card.defaultAction,9,9)
cards[CardName.remodel] = Card(CardName.remodel,Card.defaultAction,2,4)
cards[CardName.salvager] = Card(CardName.salvager,Card.defaultAction,9,9)
cards[CardName.sea_hag] = Card(CardName.sea_hag,Card.defaultAction,9,9)
cards[CardName.smithy] = Card(CardName.smithy,Card.defaultAction,2,4)
cards[CardName.steward] = Card(CardName.steward,Card.defaultAction,9,9)
cards[CardName.treasure_map] = Card(CardName.treasure_map,Card.defaultAction,9,9)
cards[CardName.tribute] = Card(CardName.tribute,Card.defaultAction,9,9)
cards[CardName.village] = Card(CardName.village,Card.defaultAction,2,3)


class GameState:

	def __init__(self):
		self.numPlayers = 0
		self.playerTurn = 0

	def initializeGame(self, p, k, s):
		# check number of players

		# self.numPlayers = 2
		self.players = []
		self.decks =[]
		self.hand =[]
		self.discard =[]
		self.cards = cards
		self.playerTurn = 0

		if not (2 <= p <= MAX_PLAYERS):
			return -1

		random.seed(s)


		# set number of players
		self.numPlayers = p

		self.playerTurn = 0
		# check selected kingdom cards are different
		cardNames = set(k)

		# ADD check for 10 kingdom cards
		if len(cardNames) != 10:
			return -1

		# set number of Curse cards
		# set number of Victory cards
		# set number of Treasure cards
		# set number of Kingdom cards
		for cardName in cardNames:
			if cardName == CardName.great_hall or cardName == CardName.gardens:
				if self.numPlayers == 2:
					cards[cardName].count = 8
				else:
					cards[cardName].count = 12
			else:
				cards[cardName].count = 10
			cards[cardName].embargoTokens = 0

		if self.numPlayers == 2:
			cards[CardName.curse].count = 10
			cards[CardName.estate].count = 8
			cards[CardName.duchy].count = 8
			cards[CardName.province].count = 8
		elif self.numPlayers == 3:
			cards[CardName.curse].count = 20
			cards[CardName.estate].count = 12
			cards[CardName.duchy].count = 12
			cards[CardName.province].count = 12
		else:
			cards[CardName.curse].count = 30
			cards[CardName.estate].count = 12
			cards[CardName.duchy].count = 12
			cards[CardName.province].count = 12

		cards[CardName.copper].count = 10
		cards[CardName.silver].count = 10
		cards[CardName.gold].count = 10
		cards[CardName.copper].embargoTokens = 0
		cards[CardName.silver].embargoTokens = 0
		cards[CardName.gold].embargoTokens = 0


		# set player decks
		#shuffle player decks
		for i in range(0,self.numPlayers):
			self.players.append(Player(self))
			self.players[i].shuffle()
			# print(self.players[i].deck)

		# //set embargo tokens to 0 for all supply piles
  # for (i = 0; i <= treasure_map; i++)
  #   {
  #     state->embargoTokens[i] = 0;
  #   }
		for p in self.players:
			for i in range(0,5):
				p.drawCard()
		self.players[0].startTurn()
		# print(cards[CardName.silver].count)

	def currentPlayer(self):
		if self.playerTurn >= self.numPlayers:
			self.playerTurn = 0
		return self.players[self.playerTurn];

	def nextPlayer(self):
		self.playerTurn += 1
		if self.playerTurn >= self.numPlayers:
			self.playerTurn = 0
		return self.currentPlayer()

	def isGameOver(self):
		if self.cards[CardName.province].count == 0:
			return 1
		count = 0
		for c in self.cards:
			if self.cards[c].count == 0:
				count += 1
		if count >= 3:
			return 1
		return 0




class Player:
	def __init__(self,game):
		self.deck = [CardName.estate,CardName.estate,CardName.estate,CardName.copper,CardName.copper,CardName.copper,CardName.copper,CardName.copper,CardName.copper,CardName.copper]
		self.gameState = game
		self.discard = []
		self.hand = []
		self.outpostPlayed = 0;
		self.phase = 0;
		self.numActions = 1;
		self.numBuys = 1;
		self.playedCardCount = 0;
		self.coins = 0
		self.coin_bonus = 0

	def shuffle(self):
		self.deck.sort()
		random.shuffle(self.deck)

	def startTurn(self):
		self.outpostPlayed = 0;
		self.phase = 0;
		self.numActions = 1;
		self.numBuys = 1;
		self.playedCardCount = 0;
		self.coin_bonus = 0
		self.updateCoins()
		return 0
		

	def takeTurn(self):
		return self.startTurn()

		

	# def playCard(self, i):
	# 	n = self.hand.pop(i)
	# 	self.discard.append(n)
	# 	c = cards[n]
	# 	c.action(c,self)

	def drawCard(self):
		c = self.pickCard()
		if c == -1:
			return -1

		self.hand.append(c)
		return c

	def pickCard(self):
		if len(self.deck) == 0:
			self.deck = self.discard
			self.discard = []
			self.shuffle()
			if len(self.deck) == 0:
				return -1
		
		return self.deck.pop()

	def buy(self,c,f):
		if self.numBuys < 1:
			return -1
		if self.coins < cards[c].cost:
			#print("You do not have enough money to buy that. You have "+ repr(self.coins) +" coins.\n")
			return -1


		self.phase = 1

		r = self.gainCard(c,f)
		if r == -1:
			return -1
		self.numBuys -= 1

		for i in range(0,cards[c].embargoTokens):
			self.gainCard(CardName.curse,0)

		return 0

	def gainCard(self,c,f):
		if cards[c].count < 1:
			#print("There are not any of that type of card left\n")
			return -1

		if f == 1:
			self.deck.append(c)
		elif f == 2:
			self.hand.append(c)
		else:
			self.discard.append(c)

		self.coins -= cards[c].cost
		cards[c].count -= 1
		return 0

	def score(self):
		score = 0
		gardenPoints = (len(self.hand) + len(self.discard) + len(self.deck))/10

		for c in self.hand:
			if c == CardName.curse:
				score -= 1
			if c == CardName.estate:
				score += 1
			if c == CardName.duchy:
				score += 3
			if c == CardName.province:
				score += 6
			if c == CardName.great_hall:
				score += 1
			if c == CardName.gardens: 
				score += gardenPoints

		for c in self.discard:
			if c == CardName.curse: 
				score -= 1
			if c == CardName.estate: 
				score += 1
			if c == CardName.duchy: 
				score += 3
			if c == CardName.province: 
				score += 6
			if c == CardName.great_hall: 
				score += 1
			if c == CardName.gardens: 
				score += gardenPoints

		for c in self.deck:
			if c == CardName.curse: 
				score -= 1
			if c == CardName.estate: 
				score += 1
			if c == CardName.duchy: 
				score += 3
			if c == CardName.province: 
				score += 6
			if c == CardName.great_hall: 
				score += 1
			if c == CardName.gardens: 
				score += gardenPoints
	
		return score

	def discardCard(self,c):
		if self.hand.count(c) != 0:
			self.hand.remove(c)
			self.discard.append(c)

	def playCard(self,c, ch1, ch2, ch3, g):
		coin_bonus = 0

		if self.phase != 0:
			return -1

		if self.numActions < 1:
			return -1

		if len(self.hand) <= c:
			return -1

		card = self.hand[c]
		#print "Card: "+str(cards[card].value)


		r = cards[card].action(cards[card],self, ch1, ch2, ch3, c)

		if r == -1:
			return -1

		self.numActions -= 1

		self.updateCoins()

		return coin_bonus

	def updateCoins(self):
		coins = self.coin_bonus
		for c in self.hand:
			if c == CardName.copper:
				coins+=1
			elif c == CardName.silver:
				coins+=1
			elif c == CardName.gold:
				coins+=1
		self.coins = coins
		return coins

# def main():
# 	k = [CardName.adventurer, CardName.gardens, CardName.embargo, CardName.village, CardName.minion, CardName.mine, CardName.cutpurse, CardName.sea_hag, CardName.tribute, CardName.smithy]
# 	g = GameState()
# 	print(sys.getsizeof(CardName.adventurer.value))
# 	g.initializeGame(2, k, 1337)





# if __name__ == "__main__":
# 	main()
