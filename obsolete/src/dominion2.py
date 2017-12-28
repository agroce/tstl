__author__ = 'Will'
import random
MAX_HAND = 500
MAX_DECK = 500
MAX_PLAYERS =  4
DEBUG = 0
cardlist = ["Curse","Estate","Duchy","Province",#0-3
        "Copper", "Silver", "Gold",             #4-6
        "Adventurer", "Ambassador", "Baron",    #7-9
        "Council Room", "Cutpurse", "Embargo",  #10-12
        "Feast", "Gardens", "Great Hall",       #13-15
        "Mine", "Smithy", "Village", "Sea Hag"] #16-19

class gameState:
    def __init__(self,p):
        self.players = p
        self.supplyCount = {}
        self.embargoTokens = {}
        self.whoseTurn = 0
        self.phase = 0
        self.numActions = 1
        self.coins = 0
        self.bonus = 0
        self.numBuys = 1
        self.hand = {}
        self.deck = {}
        self.discard = {}
        self.playedCards = []
        self.kingdomCards = []
        self.scores = {}
        self.winners = []
        self.randomState = 0

def initializeGame(players,cardsetnum,seed):
    if players > MAX_PLAYERS or players < 2:
        return -1
    random.seed(seed)
    game = gameState(players)
    game.randomState = random.getstate()
    cardset = []
    for i in cardsetnum:
        cardset.append(cardlist[i])
    
    game.kingdomCards = cardset
    if len(cardset) > 10:
        return -1
    for i in range(10):
        for j in range(10):
            if j != i and cardset[i] == cardset[j]:
                return -1

    if players == 2:
        game.supplyCount["Curse"] = 10
        game.supplyCount["Estate"] = 8
        game.supplyCount["Duchy"] = 8
        game.supplyCount["Province"] = 8
    elif players == 3:
        game.supplyCount["Curse"] = 20
        game.supplyCount["Estate"] = 12
        game.supplyCount["Duchy"] = 12
        game.supplyCount["Province"] = 12
    else:
        game.supplyCount["Curse"] = 30
        game.supplyCount["Estate"] = 12
        game.supplyCount["Duchy"] = 12
        game.supplyCount["Province"] = 12
    game.supplyCount["Copper"] = 60-7*players
    game.supplyCount["Silver"] = 40
    game.supplyCount["Gold"] = 30
    for card in cardset:
        if card in cardlist[7:20]:
            game.supplyCount[card] = 10
            if card == "Gardens":
                if players == 2:
                    game.supplyCount[card] = 8
                else:
                    game.supplyCount[card] = 12

    for player in range(players):
        game.deck[player] = []
        game.hand[player] = []
        game.discard[player]= []
    for player in range(players):
        for e in range(3):
            game.deck[player].append("Estate")
        for d in range(7):
            game.deck[player].append("Copper")
    for player in range(players):
        shuffle(player,game)
    for card in cardset:
        game.embargoTokens[card] = 0
    for card in cardlist[0:7]:
        game.embargoTokens[card] = 0
    for player in range(players):
        for i in range(5):
            drawCard(player,game)
    updateCoins(game.whoseTurn,game,0)
    return game

def shuffle(player,state):
    random.setstate(state.randomState)
    array = []
    for card in state.deck[player]:
        array.append(cardlist.index(card))
    array.sort()
    random.shuffle(array)
    # print(array)
    shuffled = []
    for i in array:
        shuffled.append(cardlist[i])
    state.deck[player] = shuffled
    state.randomState = random.getstate()

def thehand(state):
    return map(lambda x: cardlist.index(x), state.hand[state.whoseTurn])

def drawCard(player,state):
    if len(state.deck[player])>= 1:
        state.hand[player].append(state.deck[player][len(state.deck[player])-1])
        state.deck[player].pop(len(state.deck[player])-1)
    else:
        state.deck[player] = state.discard[player]
        state.discard[player] = []
        shuffle(player,state)
        state.hand[player].append(state.deck[player][len(state.deck[player])-1])
        state.deck[player].pop(len(state.deck[player])-1)
    return 0

def updateCoins(player, state, bonus):
    state.coins = 0
    state.bonus+=bonus
    for card in state.hand[player]:
        if card == "Copper":
            state.coins += 1
        if card == "Silver":
            state.coins += 2
        if card == "Gold":
            state.coins += 3
    state.coins += bonus
    return 0

def gainCard(card,state,toFlag,player):
    if state.supplyCount[card] < 1:
        return -1
    if toFlag == 1:
        state.deck[player].append(card)
    elif toFlag == 2:
        state.hand[player].append(card)
    else:
        state.discard[player].append(card)
    state.supplyCount[card]-=1
    return 0

def discardCard(card,player,state,trashFlag):
    if trashFlag == 0:
        state.playedCards.append(card)
    elif trashFlag == 2:
        state.discard[player].append(card)
    state.hand[player].remove(card)
    return 0

def getCost(card):
    if card == "Curse": return 0
    if card == "Estate": return 2
    if card == "Duchy": return 5
    if card == "Province": return 8
    if card == "Copper": return 0
    if card == "Silver": return 3
    if card == "Gold": return 6
    if card == "Adventurer": return 6
    if card == "Council Room": return 5
    if card == "Feast": return 4
    if card == "Gardens": return 4
    if card == "Mine": return 5
    if card == "Smithy": return 4
    if card == "Vilage": return 3
    if card == "Baron": return 4
    if card == "Great Hall": return 3
    if card == "Ambassador": return 3
    if card == "Cutpurse": return 4
    if card == "Embargo": return 2
    if card == "Sea Hag": return 4
    else: return 100000

def whoseTurn(state):
    return state.whoseTurn


def buyCard(position,state):
    card = cardlist[position]

    if state.numBuys < 1:
        #print("You do not have any buys left 2\n")
        return -1
    elif state.supplyCount[card] < 1:
        #print("There are not any of that type of card left 2\n")
        return -1
    elif state.coins < getCost(card):
        #print(state.hand[state.whoseTurn])
        #print("You do not have enough money to buy that. You have "+ repr(state.coins) +" coins. 2\n")
        return -1
    else:
        state.phase = 1
        gainCard(card,state,0,state.whoseTurn)
        state.coins -= getCost(card)
        state.numBuys-=1
        for i in range(state.embargoTokens[card]):
            gainCard('Curse',state,0,state.whoseTurn)
    return 0

def endTurn(state):
    state.discard[state.whoseTurn].extend(state.hand[state.whoseTurn])
    state.hand[state.whoseTurn] = []
    for i in range(5):
        drawCard(state.whoseTurn,state)
    state.discard[state.whoseTurn].extend(state.playedCards)
    state.whoseTurn = (state.whoseTurn+1)%state.players
    state.phase = 0
    state.numActions = 1
    state.coins = 0
    updateCoins(state.whoseTurn,state,0)
    state.numBuys = 1
    state.playedCards = []
    state.bonus = 0
    return 0

def playCard(pos,choice1, choice2,choice3,state):
    if pos >= len(state.hand[state.whoseTurn]):
        return -1
    card = state.hand[state.whoseTurn][pos]
    if state.phase != 0:
        return -1
    if state.numActions < 1:
        return -1
    if card not in state.kingdomCards:
        return -1
    if card not in state.hand[state.whoseTurn]:
        return -1
    if cardEffect(card,choice1,choice2,choice3,state,state.bonus) < 0:
        return -1
    state.numActions-=1
    discardCard(card,state.whoseTurn,state,0)
    updateCoins(state.whoseTurn,state,state.bonus)
    return 0

def cardEffect(card,c1,c2,c3,state,bonus):
    nextPlayer = (state.whoseTurn+1)%state.players
    if card == "Adventurer":
        treasures = 0
        temp = []
        while treasures < 2:
            drawCard(state.whoseTurn,state)
            if state.hand[state.whoseTurn][len(state.hand[state.whoseTurn])-1] not in ("Copper","Silver","Gold"):
                temp.append(state.hand[state.whoseTurn].pop(len(state.hand[state.whoseTurn])-1))
            else:
                treasures+=1
        state.discard[state.whoseTurn].extend(temp)
        temp = []
        return 0
    elif card == "Ambassador":
        choice1 = state.hand[state.whoseTurn][c1]
        if choice1 not in state.hand[state.whoseTurn]:
            return -1
        for i in range(2):
            if choice1 in state.hand[state.whoseTurn]:
                state.hand[state.whoseTurn].remove(choice1)
                state.supplyCount[choice1]+=1
        return 0
    elif card == "Baron":
        choice1 = state.hand[state.whoseTurn][c1]
        state.numBuys+=1
        if choice1 == "Estate" and choice1 in state.hand[state.whoseTurn]:
            discardCard(choice1,state.whoseTurn,state,0)
            updateCoins(state.whoseTurn,state,4)
        else:
            gainCard("Estate",state,0,state.whoseTurn)
        return 0

    elif card == "Council Room":
        for i in range(3):
            drawCard(state.whoseTurn,state)
        for i in range(state.players):
            drawCard(i,state)
        return 0
    elif card == "Cut purse":
        updateCoins(state.whoseTurn,state,2)
        for player in range(state.players):
            if player != state.whoseTurn:
                if "Copper" in state.hand[player]:
                    discardCard("Copper",player,state,0)
        return 0
    elif card == "Embargo":
        choice1 = cardlist[c1]
        if choice1 not in state.embargoTokens.keys():
            return -1
        updateCoins(state.whoseTurn,state,2)
        discardCard("Embargo",state.whoseTurn,state,1)
        state.embargoTokens[choice1]+=1
        return 0
    elif card == "Feast":
        choice1 = cardlist[c1]
        if getCost(choice1) > 6:
            gainCard(choice1,state,0,state.whoseTurn)
        else:
            return -1
        return 0
    elif card == "Great Hall":
        drawCard(state.whoseTurn,state)
        state.numActions+=1
        return 0
    elif card == "Mine":
        choice1 = state.hand[state.whoseTurn][c1]
        choice2 = cardlist[c2]
        if choice1 not in state.hand[state.whoseTurn]:
            return -1
        if choice1 == "Copper" and choice2 == "Silver":
            discardCard("Copper",state.whoseTurn,state,1)
            gainCard("Silver",state,2,state.whoseTurn)
            return 0
        elif choice1 == "Silver" and choice2 == "Gold":
            discardCard("Silver",state.whoseTurn,state,1)
            gainCard("Gold",state,2,state.whoseTurn)
            return 0
        else:
            return -1
    elif card == "Smithy":
        for i in range(4):
            drawCard(state.whoseTurn,state)
        return 0
    elif card == "Village":
        drawCard(state.whoseTurn,state)
        state.numActions+=2
        return 0
    elif card == "Sea Hag":
        for player in range(state.players):
            if player != state.whoseTurn:
                drawCard(player,state)
                discardCard(state.hand[player][len(state.hand[player])-1],player,state,2)
                gainCard("Curse",state,1,player)
        return 0

    return -1

def isGameOver(state):
    if state.supplyCount["Province"] == 0:
        return True
    count = 0
    for i in state.supplyCount:
        if state.supplyCount[i] == 0:
            count+=1
        if count > 2:
            return True
    if count > 2:
        return True
    return False

def getWinners(state):
    high_score = 0
    players = []
    for player in range(state.players):
        state.scores[player] = scoreFor(player,state)
    for i in state.scores:
        high_score = max(high_score,state.scores[i])
    for i in state.scores:
        players.append(int(state.scores[i]/high_score))
    state.winners = players
    return players

def score(set):
    score = 0
    for card in set:
        if card == "Estate":
            score+=1
        if card == "Duchy":
            score+=3
        if card == "Province":
            score+=6
        if card == "Great Hall":
            score+=1
        if card == "Curse":
            score-=1
        if card == "Gardens":
            score += (len(set)/10)
    return score

def scoreFor(player,state):
    if player >= state.players:
        return -1
    library = state.deck[player]+state.hand[player]+state.discard[player]
    return score(library)



cards = ["Adventurer", "Ambassador", "Baron",   #7-9
        "Council Room", "Cutpurse", "Embargo", #10-12
        "Feast", "Gardens", "Great Hall",      #13-15
        "Mine"]

#sample game state:
# x = initializeGame(2,cards,10)
# print(x.hand)
