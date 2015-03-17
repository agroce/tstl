import random
DEBUG = True
MAX_PLAYERS = 4
MAX_DECK = 10
MAX_HAND = 10
MAX_CARDS = 27


Curse = 0
Estate = 1
Duchy = 2
Province = 3
Copper = 4
Silver = 5
Gold = 6
Adventurer = 7
Ambassador = 8
Baron = 9
Council_Room = 10
Cutpurse = 11
Embargo = 12
Feast = 13
Gardens = 14
Great_Hall = 15
Mine = 16
Minion = 17
Outpost = 18
Remodel = 19
Salvager = 20
Sea_Hag = 21
Smithy = 22
Steward = 23
Treasure_Map = 24
Tribute = 25
Village = 26

class Game():
    numPlayers =2
    supplyCount = [0] * MAX_CARDS
    embargoTokens = [0] * MAX_CARDS
    outpostPlayed = 0
    outpostTurn = 0
    whoseTurn = 0
    phase = 0
    bonus = 0
    numActions = 0  
    coins = 0    
    numBuys = 0
    kingdomCards = []
    deck = {}
    deckCount = [0] * MAX_PLAYERS
    discard = {}
    discardCount = [0] * MAX_PLAYERS
    hand = {}
    handCount = [0] * MAX_PLAYERS
    playedCards = []
    playedCardCount = 0


def initializeGame(numPlayers, kingdomCards, randomSeed):
    game = Game()
    game.numPlayers = numPlayers
    if numPlayers > MAX_PLAYERS or numPlayers < 2:
        return -1
    random.seed(randomSeed)
    game.kingdomCards = kingdomCards
    if len(kingdomCards) > 10 or len(kingdomCards) < 10:
        return -1
    for i in range(10):
        if kingdomCards[i] not in [Adventurer, Ambassador, Baron ,Council_Room ,Cutpurse ,Embargo ,Feast ,Gardens ,Great_Hall ,Mine ,Minion ,Outpost ,Remodel ,Salvager ,Sea_Hag ,Smithy ,Steward ,Treasure_Map, Tribute, Village]:
            return -1;
    for i in range(10):
        for j in range(10):
            if j != i and kingdomCards[i] == kingdomCards[j]:
                return -1
    if (numPlayers == 2):
        game.supplyCount[Curse] = 10
    elif (numPlayers == 3):
        game.supplyCount[Curse] = 20
    else:
        game.supplyCount[Curse] = 30
    if (numPlayers == 2):
      game.supplyCount[Estate] = 8
      game.supplyCount[Duchy] = 8
      game.supplyCount[Province] = 8
    else:
      game.supplyCount[Estate] = 12
      game.supplyCount[Duchy] = 12
      game.supplyCount[Province] = 12
    game.supplyCount[Copper] = 60 - (7 * numPlayers)
    game.supplyCount[Silver] = 40
    game.supplyCount[Gold] = 30
    for i in range(Adventurer,MAX_CARDS):
        for j in range(10):
            if (kingdomCards[j] == i):
                if (kingdomCards[j] == Great_Hall or kingdomCards[j] == Gardens):
                    if (numPlayers == 2):
                        game.supplyCount[i] = 8
                    else:
                        game.supplyCount[i] = 12
                else:
                    game.supplyCount[i] = 10

                break
            else:
                game.supplyCount[i] = -1

    for i in range(numPlayers):
        game.deckCount[i] = 0
        game.deck[i] = []
        game.hand[i] = []
        game.discard[i] = []

        for j in range(3):
            game.deck[i].append(Estate)
            game.deckCount[i] += 1
        for j in range(3, 10):
            game.deck[i].append(Copper)
            game.deckCount[i] += 1
    for i in range(numPlayers):
        shuffle(i, game)
    for i in range(numPlayers):
        game.handCount[i] = 0
        game.discardCount[i] = 0
    for i in range(Village):
        game.embargoTokens[i] = 0

    game.outpostPlayed = 0
    game.phase = 0
    game.numActions = 1
    game.numBuys = 1
    game.playedCardCount = 0
    game.whoseTurn = 0
    game.handCount[game.whoseTurn] = 0     
    for it in range(5):
        drawCard(game.whoseTurn, game)
    updateCoins(game.whoseTurn, game, 0)
    return game
def shuffle(player, g):
    if (g.deckCount[player] < 1):
        return -1
    g.deck[player].sort()
    random.shuffle(g.deck[player])
    return 0


def drawCard(player, g):
    if (g.deckCount[player] <= 0):
        g.deck[player] = g.discard[player]
        g.discard[player] = []
        g.deckCount[player] = g.discardCount[player]
        g.discardCount[player] = 0
        shuffle(player, g)
        g.discardCount[player] = 0
        count = g.handCount[player]
        deckCounter = g.deckCount[player]
        if (deckCounter == 0):
            return -1
        g.hand[player].append(g.deck[player][deckCounter - 1])
        g.deck[player].pop(deckCount[player]-1)
        g.deckCount[player] -= 1
        g.handCount[player] += 1
    else:
        count = g.handCount[player]     
        deckCounter = g.deckCount[player]       
        g.hand[player].append(g.deck[player][deckCounter - 1])
        g.deck[player].pop(g.deckCount[player]-1)
        g.deckCount[player] -= 1                            
        g.handCount[player] += 1   

    return 0

def updateCoins(player, g, bonus):
    g.coins = 0
    g.bonus+= bonus
    for card in g.hand[player]:
        if (card == Copper):
            g.coins += 1

        elif (card == Silver):
            g.coins += 2

        elif (card == Gold):
            g.coins += 3
    g.coins += bonus
    return 0
def gainCard(supplyPos, g, toFlag, player):
    if g.supplyCount[supplyPos] < 1 :
        return -1
    if (toFlag == 1):
        g.deck[player].append(supplyPos)
        g.deckCount[player]+=1
        g.supplyCount[supplyPos]-=1
    elif (toFlag == 2):
        g.hand[ player ].append(supplyPos)
        g.handCount[player]+=1
        g.supplyCount[supplyPos]-=1
    else:
        g.discard[player].append(supplyPos)
        g.discardCount[player]+=1
        g.supplyCount[supplyPos]-=1
    return 0

def discardCard(handPos, currentPlayer, g, trashFlag):
    if handPos not in g.hand[currentPlayer]:
        return -1
    else:
        if (trashFlag == 0):
            g.playedCards.append(handPos)
            g.playedCardCount+=1
        elif (trashFlag == 2):
            g.discard[currentPlayer].append(handPos)
            g.discardCount[currentPlayer]+=1
        g.hand[currentPlayer].remove(handPos)
    return 0 ##fixCardHole(handPos, currentPlayer, g)

def buyCard(supplyPos, g):
    if (g.numBuys < 1):
        return -1
    elif (g.supplyCount[supplyPos] <1):
        return -1
    elif (g.coins < getCost(supplyPos)):
        return -1
    else:
        g.phase=1
        gainCard(supplyPos,g, 0, g.whoseTurn)  
        g.coins = (g.coins) - (getCost(supplyPos))
        g.numBuys-=1
        for i in range(g.embargoTokens[supplyPos]):
            gainCard('Curse',g,0,g.whoseTurn)
    return 0

def getCost(cardNumber):
    if cardNumber == Curse: return 0
    if cardNumber == Estate: return 2
    if cardNumber == Duchy: return 5
    if cardNumber == Province: return 8
    if cardNumber == Copper: return 0
    if cardNumber == Silver: return 3
    if cardNumber == Gold: return 6
    if cardNumber == Adventurer: return 6
    if cardNumber == Ambassador: return 3
    if cardNumber == Baron: return 4
    if cardNumber == Council_Room: return 5
    if cardNumber == Cutpurse: return 4
    if cardNumber == Embargo: return 2
    if cardNumber == Feast: return 4
    if cardNumber == Gardens: return 4
    if cardNumber == Great_Hall: return 3
    if cardNumber == Mine: return 5
    if cardNumber == Minion: return 5
    if cardNumber == Outpost: return 5
    if cardNumber == Remodel: return 4
    if cardNumber == Salvager: return 4
    if cardNumber == Sea_Hag: return 4
    if cardNumber == Smithy: return 4
    if cardNumber == Steward: return 3
    if cardNumber == Treasure_Map: return 4
    if cardNumber == Tribute: return 5
    if cardNumber == Village: return 3
    else: return -1
def endTurn(g):
    currentPlayer = g.whoseTurn
    g.discard[currentPlayer].extend(g.hand[currentPlayer])
    g.discardCount[currentPlayer]+=1
    g.hand[currentPlayer] = []
    g.handCount[currentPlayer] = 0
    if currentPlayer < (g.numPlayers - 1):
        g.whoseTurn = currentPlayer + 1
    else:
        g.whoseTurn = 0
    g.outpostPlayed = 0
    g.phase = 0
    g.numActions = 1
    g.coins = 0
    g.numBuys = 1
    g.playedCards = []
    g.bonus = 0
    g.playedCardCount = 0
    g.handCount[g.whoseTurn] = 0
    for k in range(5):
        drawCard(g.whoseTurn, g)
    updateCoins(g.whoseTurn, g , 0)
    return 0
def playCard(handPos, choice1, choice2, choice3, g):
    card = g.hand[g.whoseTurn][handPos]
    if (g.phase != 0):
        return -1
    if (g.numActions < 1 ):
        return -1
    if card not in g.kingdomCards:
        return -1
    if card not in g.hand[g.whoseTurn]:
        return -1
    if ( cardEffect(card, choice1, choice2, choice3, g, handPos, g.bonus) < 0 ):
        return -1
    g.numActions-=1
    discardCard(card,g.whoseTurn,g,0)
    updateCoins(g.whoseTurn, g, g.bonus)
    return 0
def cardEffect(card, choice1, choice2, choice3, g, handPos, bonus):
    currentPlayer = g.whoseTurn
    nextPlayer = (g.whoseTurn+1)%g.numPlayers
    tributeRevealedCards = [-1, -1]
    temphand = []
    drawntreasure = 0
    if card == Adventurer:
        while(drawntreasure<2):
            if (g.deckCount[currentPlayer] <1):
                    shuffle(currentPlayer, g)
            drawCard(currentPlayer, g)
            cardDrawn = g.hand[currentPlayer][g.handCount[currentPlayer]-1]
            if (cardDrawn == Copper or cardDrawn == Silver or cardDrawn == Gold):
                drawntreasure+=1
            else:
                temphand.append(g.hand[currentPlayer].pop(g.handCount[currentPlayer]-1))
        discardCard(handPos, currentPlayer, g, 0)
        return 0
    elif card == Ambassador:
        if g.hand[currentPlayer][choice1] not in g.hand[currentPlayer]:
            return -1
        for i in range(2):
            if g.hand[currentPlayer][choice1] in g.hand[currentPlayer]:
                g.hand[currentPlayer].remove(g.hand[currentPlayer][choice1])
                g.supplyCount[g.hand[currentPlayer][choice1]]+=1
        discardCard(handPos, currentPlayer, g, 0)
        return 0
    elif card == Baron:
        g.numBuys+=1
        if (g.hand[currentPlayer][choice1] == Estate) and (g.hand[currentPlayer][choice1] in g.hand[currentPlayer]):
            discardCard(g.hand[currentPlayer][choice1],currentPlayer,g,2)
            updateCoins(currentPlayer,g,4)
        else:
            gainCard(Estate,g,0,currentPlayer)
        discardCard(handPos, currentPlayer, g, 0)
        return 0
    elif card == Council_Room:
        for i in range(4):
            drawCard(currentPlayer, g)
        g.numBuys+=1
        for i in range(g.numPlayers):
            if ( i != currentPlayer ):
                drawCard(i, g)
        discardCard(handPos, currentPlayer, g, 0)
        return 0
    elif card == Cutpurse:
        updateCoins(currentPlayer, g, 2)
        for i in range(g.numPlayers):
            if (i != currentPlayer):
                if (Copper in g.hand[i]):
                    discardCard(Copper, i, g, 0)
        discardCard(handPos, currentPlayer, g, 0)
        return 0
    elif card == Embargo:
        updateCoins(currentPlayer,g,2)
        if ( g.supplyCount[choice1] == -1 ):
            return -1
        g.embargoTokens[choice1]+=1
        discardCard(handPos, currentPlayer, g, 1)            
        return 0
    elif card == Feast:
        if (g.supplyCount[choice1] <= 0):
            return -1
        elif (getCost(choice1) > 5):
            return -1
        elif (getCost(choice1) < 6):
            gainCard(choice1, g, 0, currentPlayer)
        discardCard(handPos, currentPlayer, g, 1)
        return 0
    elif card == Gardens:
        return -1
    elif card == Great_Hall:
        drawCard(currentPlayer,g);
        g.numActions+=1
        discardCard(handPos, currentPlayer, g, 0)
        return 0
    elif card == Mine:
        if (g.hand[currentPlayer][choice1] not in g.hand[currentPlayer]):
            return -1
        elif (g.hand[currentPlayer][choice1] < Copper or g.hand[currentPlayer][choice1] > Gold):
            return -1
        if (g.hand[currentPlayer][choice1] == Copper and choice2 == Silver):
            discardCard(Copper,currentPlayer,g,1)
            gainCard(Silver,g,2,currentPlayer)
            return 0
        elif (g.hand[currentPlayer][choice1] == Copper and choice2 == Gold):
            discardCard(Copper,currentPlayer,g,1)
            gainCard(Gold,g,2,currentPlayer)
            return 0
        elif (g.hand[currentPlayer][choice1] == Copper and choice2 == Copper):
            discardCard(Copper,currentPlayer,g,1)
            gainCard(Copper,g,2,currentPlayer)
            return 0
        elif (choice2 > Gold or choice2 < Copper):
            return -1
        elif( (getCost(g.hand[currentPlayer][choice1]) + 3) > getCost(choice2) ):
            return -1
        else:
            return -1
        discardCard(handPos, currentPlayer, g, 0)
        return 0
    elif card == Minion:
        g.numActions+=1
        discardCard(handPos, currentPlayer,g, 0)
        if (choice1):
            updateCoins(currentPlayer,g,2)
        elif (choice2):
            while(g.handcount[currentPlayer] > 0):
                discardCard(handPos, currentPlayer, g, 0)
            for i in range(4):
                drawCard(currentPlayer, g)
            for i in range(g.numPlayers):
                if (i != currentPlayer):
                    if ( g.handCount[i] > 4 ):
                        while( g.handCount[i] > 0 ):
                            discardCard(handPos, i, g, 0)
                        for j in range(4):
                            drawCard(i, g)
        discardCard(handPos, currentPlayer, g, 0)
        return 0
    elif card == Outpost:
        g.outpostPlayed+=1
        discardCard(handPos, currentPlayer, g, 0)
        return 0
    elif card == Remodel:
        j = g.hand[currentPlayer][choice1]
        if ( (getCost(g.hand[currentPlayer][choice1]) + 2) < getCost(choice2) ):
            return -1
        else:
            gainCard(choice2, g, 0, currentPlayer)
            discardCard(handPos, currentPlayer, g, 1)
        discardCard(handPos, currentPlayer, g, 0)
        return 0
    elif card == Salvager:
        g.numBuys+=1
        if (choice1):
            g.coins = g.coins + getCost( g.hand[currentPlayer][handPos] )
            discardCard(choice1, currentPlayer, g, 1)      
        discardCard(handPos, currentPlayer, g, 0)
        return 0
    elif card == Sea_Hag:
        for i in range(g.numPlayers):
            if (i != currentPlayer):
                drawCard(i,g)
                discardCard(g.hand[i][handCount[i]-1],i,g,2)
                gainCard(Curse,g,1,i)
        discardCard(handPos, currentPlayer, g, 0)
        return 0
    elif card == Smithy:
        for i in range(3):
            drawCard(currentPlayer,g)
        discardCard(handPos,currentPlayer,g, 0)
        return 0
    elif card == Steward:
        if (choice1 == 1):                     
            drawCard(currentPlayer, g)
            drawCard(currentPlayer, g)
        elif (choice1 == 2):
            g.coins = g.coins + 2
        else:
            discardCard(choice2, currentPlayer, g, 1)
            discardCard(choice3, currentPlayer, g, 1)
        discardCard(handPos, currentPlayer, g, 0)
        return 0
    elif card == Treasure_Map:
        index = -1
        for i in range(handCount[currentPlayer]):
            if (g.hand[currentPlayer][i] == Treasure_Map and i != handPos):
                index = i
                break
        if (index > -1):
            discardCard(handPos, currentPlayer, g, 1)
            discardCard(index, currentPlayer, g, 1)
            for i in range(4):
                gainCard(Gold, g, 1, currentPlayer)
        discardCard(handPos, currentPlayer, g, 0)
        return 0
    elif card == Village:
        drawCard(currentPlayer, g)
        g.numActions = g.numActions + 2
        discardCard(handPos, currentPlayer, g, 0)
        return 0

def isGameOver(g):
    j=0
    if (g.supplyCount[Province] == 0):
        return 1
    for i in range(MAX_CARDS):
        if (g.supplyCount[i] == 0):
            j+=1
    if ( j >= 3):
        return 1
    return 0
def scoreFor (player, g):
    score = 0
    fullDeck = g.deck[player]+g.hand[player]+g.discard[player]
    for card in fullDeck:
        if card == Estate:
            score+=1
        if card == Duchy:
            score+=3
        if card == Province:
            score+=6
        if card == Great_Hall:
            score+=2
        if card == Curse:
            score-=1
        if card == Gardens:
            score = (len(fullDeck)%10)
    return score
def getWinners(g):
    players =[0] * MAX_PLAYERS
    for i in range(MAX_PLAYERS):
        if (i >= g.numPlayers):
            players[i] = -9999
        else:
            players[i] = scoreFor (i, g)
    j = 0
    for i in range(MAX_PLAYERS):
        if (players[i] > players[j]):
            j = i
    highScore = players[j]
    currentPlayer = g.whoseTurn
    for i in range(MAX_PLAYERS):
        if ( players[i] == highScore and i > currentPlayer ):
            players[i]+=1
    j = 0
    for i in range(MAX_PLAYERS):
        if ( players[i] > players[j] ):
            j = i
    highScore = players[j]
    for i in range(MAX_PLAYERS):
        if ( players[i] == highScore ):
            players[i] = 1
        else:
            players[i] = 0
    return players