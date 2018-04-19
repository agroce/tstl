from collections import defaultdict
from functools import wraps
import random

r = random.Random()
r.seed(10)


try:
    import psyco
    psyco.full()
except ImportError:
    pass


# Set whether most strategies will buy Duchies and Estates.  This is useful to
# reduce draws in simulations of full games.  In 4-Province Solitaire, it just
# slows the deck down.
BUY_DUCHIES = BUY_ESTATES = True


def main():
    tries = 10000
    # Test Big Money, Chapel, and Smithy in 4-Province Solitaire.
    test("Big Money", tries, big_money)
    test(CHAPEL, tries, chapel)
    test(SMITHY, tries, smithy)
    # Run a test match between Smithy and Chapel.
    test_matches(tries, [
        (SMITHY, smithy, {}),
        (CHAPEL, chapel, {}),
    ])


# Card name constants
ADVENTURER = 'Adventurer'
BARON = 'Baron'
BUREAUCRAT = 'Bureaucrat'
CHANCELLOR = 'Chancellor'
CHAPEL = 'Chapel'
COPPER = 'Copper'
COUNCIL_ROOM = 'Council Room'
COURTYARD = 'Courtyard'
CURSE = 'Curse'
DUCHY = 'Duchy'
DUKE = 'Duke'
ENVOY = 'Envoy'
ESTATE = 'Estate'
GARDENS = 'Gardens'
GREAT_HALL = 'Great Hall'
GOLD = 'Gold'
HAREM = 'Harem'
ISLAND = 'Island'
LABORATORY = 'Laboratory'
MARKET = 'Market'
MILITIA = 'Militia'
MINE = 'Mine'
MINION = 'Minion'
MOAT = 'Moat'
NOBLES = 'Nobles'
PROVINCE = 'Province'
REMODEL = 'Remodel'
SCOUT = 'Scout'
SEA_HAG = 'Sea Hag'
SILVER = 'Silver'
SMITHY = 'Smithy'
THRONE_ROOM = 'Throne Room'
VILLAGE = 'Village'
WHARF = 'Wharf'
WITCH = 'Witch'


# Card costs
COST = {
    ADVENTURER: 6,
    BARON: 4,
    BUREAUCRAT: 4,
    CHANCELLOR: 3,
    CHAPEL: 2,
    COPPER: 0,
    COUNCIL_ROOM: 5,
    COURTYARD: 2,
    CURSE: 0,
    DUCHY: 5,
    DUKE: 5,
    ENVOY: 4,
    ESTATE: 2,
    GARDENS: 4,
    GREAT_HALL: 3,
    GOLD: 6,
    HAREM: 6,
    ISLAND: 4,
    LABORATORY: 5,
    MARKET: 5,
    MILITIA: 4,
    MINE: 5,
    MINION: 5,
    MOAT: 2,
    NOBLES: 6,
    PROVINCE: 8,
    REMODEL: 4,
    SCOUT: 4,
    SEA_HAG: 4,
    SILVER: 3,
    SMITHY: 4,
    THRONE_ROOM: 4,
    VILLAGE: 3,
    WHARF: 5,
    WITCH: 5,
}


TREASURE_CARDS = [COPPER, SILVER, GOLD, HAREM]
VICTORY_CARDS = [ESTATE, DUCHY, PROVINCE, GARDENS,
                 DUKE, GREAT_HALL, HAREM, NOBLES,
                 ISLAND]


# Utility functions


def setup():
    "Set up a starting deck and discard pile."
    deck = [COPPER] * 7 + [ESTATE] * 3
    r.shuffle(deck)
    discard = []
    return deck, discard, 0


def setup_supply(players):
    "Set up a supply."
    supply = defaultdict(lambda: 10)
    victory_cards = 8 if players <= 2 else 12
    for card in VICTORY_CARDS:
        supply[card] = victory_cards
    if players > 4:
        supply[PROVINCE] = 3 * players
    supply[CURSE] = 10 * (players - 1)
    supply[COPPER] = 60
    supply[SILVER] = 40
    supply[GOLD] = 30
    return supply


def match_setup(base_setup=setup):
    "Set up a starting deck, discard pile, and hand."
    deck, discard, turn = base_setup()
    hand = draw(deck, discard, 5)
    return [deck, discard, hand, turn, []]


def draw(deck, discard, n):
    "Draw n cards, shuffling if needed.  Returns the cards drawn."
    if n == 0:
        return []
    d = min(len(deck), n)
    hand = deck[-d:]
    del deck[-d:]
    if d < n:
        deck[:] = discard
        del discard[:]
        r.shuffle(deck)
        d = min(len(deck), n - d)
        hand += deck[-d:]
        del deck[-d:]
    return hand


def move(card, from_, to):
    """Move a card from one location to another.

    If the destination is the deck, the card will be on the top.
    """
    from_.remove(card)
    to.append(card)


def gain(card, supply, to):
    """Gain a card from the supply, putting it in the 'to' location.

    Returns True iff successful.
    """
    if supply[card]:
        supply[card] -= 1
        to.append(card)
        return True
    else:
        return False


def count_coins(hand):
    "Count the total coins from Treasure cards in a list of cards."
    return (hand.count(COPPER) + 2 * hand.count(SILVER) +
            3 * hand.count(GOLD) + 2 * hand.count(HAREM))


def treasure_value(deck):
    "Compute the average value of the Treasure cards in a deck."
    treasure =  [1] * deck.count(COPPER)
    treasure += [2] * deck.count(SILVER)
    treasure += [3] * deck.count(GOLD)
    treasure += [2] * deck.count(HAREM)
    if treasure:
        return float(sum(treasure)) / len(treasure)


def score(deck):
    "Count the total score of a deck."
    return (  deck.count(ESTATE)
            + deck.count(GREAT_HALL)
            + 2 * deck.count(HAREM)
            + 2 * deck.count(NOBLES)
            + 2 * deck.count(ISLAND)
            + (3 + deck.count(DUKE)) * deck.count(DUCHY)
            + 6 * deck.count(PROVINCE)
            + len(deck) // 10 * deck.count(GARDENS)
            - deck.count(CURSE))


def default_attack_handler(deck, discard, hand, turn, supply, attack):
    """Handle some basic attacks in a default manner.  Returns True iff the
    attack was handled."""
    if attack == COUNCIL_ROOM:
        # Not really an attack, but this is an easy way to handle it.
        hand += draw(deck, discard, 1)
        return True
    elif MOAT in hand:
        return True
    elif attack == MINION and len(hand) > 4:
        discard += hand
        hand[:] = draw(deck, discard, 4)
        return True
    elif attack == WITCH:
        gain(CURSE, supply, discard)
        return True
    elif attack == SEA_HAG:
        discard += draw(deck, discard, 1)
        gain(CURSE, supply, deck)
        return True
    else:
        return False


def handle_attacks(deck, discard, hand, turn, supply, attacks,
                   handlers=[default_attack_handler]):
    """Dispatch attacks to handlers.  For each attack in order, attempts to
    apply each handler in order.  Raises an UnhandledAttack exception if any
    attack remains unhandled.
    """
    for attack in attacks:
        for handler in handlers:
            if handler(deck, discard, hand, turn, supply, attack):
                break
        else:
            raise UnhandledAttack(attack)


def wrap_attacks(strategy):
    "Decorator to handle basic attacks quietly without code modification."
    @wraps(strategy)
    def wrapper(deck, discard, hand, turn, supply, attacks=None, **kwargs):
        if attacks:
            handle_attacks(deck, discard, hand, turn, supply, attacks)
        return strategy(deck, discard, hand, turn, supply, **kwargs)
    return wrapper


class UnhandledAttack(Exception):
    "Signal that an attack has not been handled."


class InvalidGameError(Exception):
    "Signal that a simulation should be aborted and not counted."


def test_game(strategy, setup=setup, **kwargs):
    """Run a single test game using a given strategy.

    Returns the total number of turns taken to reach 4 Provinces and the
    final score of the deck.
    """
    deck, discard, turns = setup()
    supply = setup_supply(2)
    while (deck + discard).count(PROVINCE) < 4:
        turns += 1
        hand = draw(deck, discard, 5)
        strategy(deck, discard, hand, turns, supply, **kwargs)
        discard += hand
    return turns, score(deck + discard)


def test_minion(strategy, setup=setup, **kwargs):
    """Run a single test game against a strong Minion deck using a given strategy.

    Returns the total number of turns taken to reach 4 Provinces and the
    final score of the deck.
    """
    deck, discard, turns = setup()
    supply = setup_supply(2)
    while (deck + discard).count(PROVINCE) < 4:
        turns += 1
        # Assume that we get hit by a Minion on turn 3, turn 5, and every turn
        # thereafter.
        if turns == 3 or turns >= 5:
            discard += draw(deck, discard, 5)
            hand = draw(deck, discard, 4)
        else:
            hand = draw(deck, discard, 5)
        strategy(deck, discard, hand, turns, supply, **kwargs)
        discard += hand
    return turns, score(deck + discard)


def test_match(strategies, setup=match_setup):
    """Run a single test match between multiple decks.

    Returns the winning strategies.
    """
    DECK, DISCARD, HAND, TURNS, ATTACKS = range(5)
    supply = setup_supply(len(strategies))
    players = [setup() for _ in strategies]
    player_index = 0

    while True:
        if supply[PROVINCE] == 0:
            break
        if len(strategies) <= 4 and supply.values().count(0) >= 3:
            break
        if len(strategies) > 4 and supply.values().count(0) >= 4:
            break
        p = players[player_index]
        name, strategy, kwargs = strategies[player_index]
        p[TURNS] += 1
        my_attacks = strategy(p[DECK], p[DISCARD], p[HAND], p[TURNS], supply,
                              attacks=p[ATTACKS], **kwargs) or []
        p[DISCARD] += p[HAND]
        p[HAND] = draw(p[DECK], p[DISCARD], 5)
        p[ATTACKS] = []
        for i, opp in enumerate(players):
            if i != player_index:
                opp[ATTACKS] += my_attacks
        player_index = (player_index + 1) % len(strategies)

    best_score = None
    winners = []
    for strategy, p in zip(strategies, players):
        player_score = (score(p[DECK] + p[DISCARD] + p[HAND]), -p[TURNS])
        if player_score > best_score:
            best_score = player_score
            winners = [strategy[0]]
        elif player_score == best_score:
            winners.append(strategy[0])
    return winners


def test_coins(strategy, setup=setup, turns=None, **kwargs):
    """Run a single test game using a given strategy through a given turn.

    Returns the total number of coins received.
    """
    coins = 0
    deck, discard, turns_taken = setup()
    supply = setup_supply(2)
    while turns_taken < turns:
        turns_taken += 1
        hand = draw(deck, discard, 5)
        coins += strategy(deck, discard, hand, turns_taken, supply, **kwargs)
        discard += hand
    return turns_taken, coins


def test(name, tries, strategy, runner=test_game, **kwargs):
    "Run a series of test games and print the results."
    times = []
    scores = []
    total_tries = 0
    while len(times) < tries:
        total_tries += 1
        try:
            time, score = runner(strategy, **kwargs)
        except InvalidGameError:
            pass
        else:
            times.append(time)
            scores.append(score)
    times.sort()
    scores.sort()
    print name
    num = len(times)
    print "Num = %d" % num
    print "Tot = %d" % total_tries
    print "Min = %d" % times[0]
    if num % 2 == 1:
        print "Med = %d" % times[num // 2]
    else:
        print "Med = %f" % (float(times[num // 2 - 1] + times[num // 2]) / 2)
    print "Max = %d" % times[-1]
    avg = float(sum(times)) / num
    print "Avg = %f" % avg
    print "StD = %f" % ((sum((x-avg)**2 for x in times) / (num-1)) ** 0.5)
    print "Avg Score = %f" % (float(sum(scores)) / num)
    print


def test_matches(tries, strategies, runner=test_match, **kwargs):
    "Run a series of test matches and print the results."
    winners = []
    total_tries = matches = 0
    _strategies = strategies[:]
    while matches < tries:
        total_tries += 1
        try:
            r.shuffle(_strategies)
            winners += runner(_strategies, **kwargs)
            matches += 1
        except InvalidGameError:
            pass
    print "Num = %d" % matches
    print "Tot = %d" % total_tries
    for strategy in strategies:
        name = strategy[0]
        print name, winners.count(name), float(winners.count(name)) / matches
    print


# Strategy functions

@wrap_attacks
def adventurer(deck, discard, hand, turn, supply, n=1):
    # Buy n Adventurers
    if ADVENTURER in hand:
        aside = []
        treasures_found = 0
        while (deck or discard) and treasures_found < 2:
            card = draw(deck, discard, 1)
            if card[0] in TREASURE_CARDS:
                hand += card
                treasures_found += 1
            else:
                aside += card
        discard += aside
    coins = count_coins(hand)
    all_cards = deck + discard + hand
    provinces = all_cards.count(PROVINCE)
    if coins >= COST[PROVINCE] and gain(PROVINCE, supply, discard): pass
    elif BUY_DUCHIES and coins >= COST[DUCHY] and provinces > 3 and gain(DUCHY, supply, discard): pass
    elif BUY_ESTATES and coins >= COST[ESTATE] and provinces > 3 and gain(ESTATE, supply, discard): pass
    elif coins >= COST[ADVENTURER] and all_cards.count(ADVENTURER) < n and gain(ADVENTURER, supply, discard): pass
    elif coins >= COST[GOLD] and gain(GOLD, supply, discard): pass
    elif coins >= COST[SILVER]:
        gain(SILVER, supply, discard)


@wrap_attacks
def baron(deck, discard, hand, turn, supply):
    # Buy 1 Baron
    coins = count_coins(hand)
    buys = 1
    if BARON in hand and ESTATE in hand:
        coins += 4
        buys += 1
    all_cards = deck + discard + hand
    provinces = all_cards.count(PROVINCE)
    has_baron = BARON in all_cards
    while coins >= 3 and buys > 0:
        buys -= 1
        if coins >= COST[PROVINCE] and gain(PROVINCE, supply, discard):
            coins -= COST[PROVINCE]
            provinces += 1
        elif BUY_DUCHIES and coins >= COST[DUCHY] and provinces > 3 and gain(DUCHY, supply, discard):
            coins -= COST[DUCHY]
        elif BUY_ESTATES and coins >= COST[ESTATE] and provinces > 3 and gain(ESTATE, supply, discard):
            coins -= COST[ESTATE]
        elif coins >= COST[GOLD] and gain(GOLD, supply, discard):
            coins -= COST[GOLD]
        elif coins >= COST[BARON] and not has_baron and gain(BARON, supply, discard):
            coins -= COST[BARON]
            has_baron = True
        elif coins >= COST[SILVER] and gain(SILVER, supply, discard):
            coins -= COST[SILVER]
        else:
            break


@wrap_attacks
def baron_estate(deck, discard, hand, turn, supply):
    # Buy 1 Baron, use it even without an Estate in hand
    coins = count_coins(hand)
    buys = 1
    if BARON in hand:
        buys += 1
        if ESTATE in hand:
            coins += 4
        else:
            gain(ESTATE, supply, discard)
    all_cards = deck + discard + hand
    provinces = all_cards.count(PROVINCE)
    has_baron = BARON in all_cards
    while coins >= 3 and buys > 0:
        buys -= 1
        if coins >= COST[PROVINCE] and gain(PROVINCE, supply, discard):
            coins -= COST[PROVINCE]
            provinces += 1
        elif BUY_DUCHIES and coins >= COST[DUCHY] and provinces > 3 and gain(DUCHY, supply, discard):
            coins -= COST[DUCHY]
        elif BUY_ESTATES and coins >= COST[ESTATE] and provinces > 3 and gain(ESTATE, supply, discard):
            coins -= COST[ESTATE]
        elif coins >= COST[GOLD] and gain(GOLD, supply, discard):
            coins -= COST[GOLD]
        elif coins >= COST[BARON] and not has_baron and gain(BARON, supply, discard):
            coins -= COST[BARON]
            has_baron = True
        elif coins >= COST[SILVER] and gain(SILVER, supply, discard):
            coins -= COST[SILVER]
        else:
            break


@wrap_attacks
def bureaucrat(deck, discard, hand, turn, supply, n=1):
    # Buy n Bureaucrats
    all_cards = deck + discard + hand
    provinces = all_cards.count(PROVINCE)
    my_attacks = []
    if BUREAUCRAT in hand:
        gain(SILVER, supply, deck)
        my_attacks.append(BUREAUCRAT)
    coins = count_coins(hand)
    if coins >= COST[PROVINCE] and gain(PROVINCE, supply, discard): pass
    elif BUY_DUCHIES and coins >= COST[DUCHY] and provinces > 3 and gain(DUCHY, supply, discard): pass
    elif BUY_ESTATES and coins >= COST[ESTATE] and provinces > 3 and gain(ESTATE, supply, discard): pass
    elif coins >= COST[GOLD] and gain(GOLD, supply, discard): pass
    elif coins >= COST[BUREAUCRAT] and all_cards.count(BUREAUCRAT) < n and gain(BUREAUCRAT, supply, discard): pass
    elif coins >= COST[SILVER] and gain(SILVER, supply, discard): pass
    return my_attacks


@wrap_attacks
def chancellor(deck, discard, hand, turn, supply, n=0):
    # Buy n Chancellors, always choose to r.shuffle.
    coins = count_coins(hand)
    if CHANCELLOR in hand:
        coins += 2
        discard += deck
        del deck[:]
    all_cards = deck + discard + hand
    provinces = all_cards.count(PROVINCE)
    if coins >= COST[PROVINCE] and gain(PROVINCE, supply, discard): pass
    elif BUY_DUCHIES and coins >= COST[DUCHY] and provinces > 3 and gain(DUCHY, supply, discard): pass
    elif BUY_ESTATES and coins >= COST[ESTATE] and provinces > 3 and gain(ESTATE, supply, discard): pass
    elif coins >= COST[GOLD] and gain(GOLD, supply, discard): pass
    elif coins >= COST[CHANCELLOR] and all_cards.count(CHANCELLOR) < n and gain(CHANCELLOR, supply, discard): pass
    elif coins >= COST[SILVER]: gain(SILVER, supply, discard)


@wrap_attacks
def chancellor_b(deck, discard, hand, turn, supply, f=1.0):
    # Buy 1 Chancellor, r.shuffle when ratio of coin density in
    # hand / discard pile to coin density in deck is greater than f.
    coins = count_coins(hand)
    if CHANCELLOR in hand:
        coins += 2
        if deck:
            discard_coins = coins + count_coins(discard)
            deck_coins = count_coins(deck)
            if COST[GOLD] <= coins < COST[PROVINCE]:
                discard_coins += 3
            elif COST[SILVER] <= coins < COST[GOLD]:
                discard_coins += 2
            discard_p = float(discard_coins) / (len(hand) + len(discard) + 1)
            deck_p = float(deck_coins) / len(deck)
            if discard_p >= deck_p * f:
                discard += deck
                del deck[:]
    all_cards = deck + discard + hand
    provinces = all_cards.count(PROVINCE)
    if coins >= COST[PROVINCE] and gain(PROVINCE, supply, discard): pass
    elif BUY_DUCHIES and coins >= COST[DUCHY] and provinces > 3 and gain(DUCHY, supply, discard): pass
    elif BUY_ESTATES and coins >= COST[ESTATE] and provinces > 3 and gain(ESTATE, supply, discard): pass
    elif coins >= COST[GOLD] and gain(GOLD, supply, discard): pass
    elif coins >= COST[CHANCELLOR] and CHANCELLOR not in all_cards and gain(CHANCELLOR, supply, discard): pass
    elif coins >= COST[SILVER]: gain(SILVER, supply, discard)


def chapel(deck, discard, hand, turn, supply, attacks=None):
    # Buy 1 Chapel
    def handle_bureaucrat(deck, discard, hand, turn, supply, attack):
        if attack == BUREAUCRAT:
            if CHAPEL in hand:
                priority = [PROVINCE, DUCHY, ESTATE]
            else:
                priority = [ESTATE, DUCHY, PROVINCE]
            for card in priority:
                if card in hand:
                    move(card, hand, deck)
                    break
            return True
    if attacks:
        handle_attacks(deck, discard, hand, turn, supply, attacks,
                       [handle_bureaucrat, default_attack_handler])
    coins = count_coins(hand)
    all_cards = deck + discard + hand
    provinces = all_cards.count(PROVINCE)
    if CHAPEL in hand:
        while CURSE in hand:
            hand.remove(CURSE)
        if provinces <= 3:
            while ESTATE in hand:
                hand.remove(ESTATE)
        coppers = hand.count(COPPER)
        all_coins = count_coins(all_cards)
        coppers = min(coppers, all_coins - COST[SILVER])
        if coins >= COST[PROVINCE]:
            coppers = min(coppers, coins - COST[PROVINCE])
        elif BUY_DUCHIES and coins >= COST[DUCHY] and provinces > 3:
            coppers = min(coppers, coins - COST[DUCHY])
        elif coins >= COST[GOLD]:
            coppers = min(coppers, coins - COST[GOLD])
        for i in xrange(coppers):
            hand.remove(COPPER)
        coins -= coppers
    if coins < 5 and CHAPEL not in all_cards and gain(CHAPEL, supply, discard): pass
    elif coins >= COST[PROVINCE] and gain(PROVINCE, supply, discard): pass
    elif BUY_DUCHIES and coins >= COST[DUCHY] and provinces > 3 and gain(DUCHY, supply, discard): pass
    elif BUY_ESTATES and coins >= COST[ESTATE] and provinces > 3 and gain(ESTATE, supply, discard): pass
    elif coins >= COST[GOLD] and gain(GOLD, supply, discard): pass
    elif coins >= COST[SILVER]: gain(SILVER, supply, discard)


@wrap_attacks
def multi_chapel(deck, discard, hand, turn, supply):
    # Buy 2+ Chapels
    coins = count_coins(hand)
    all_cards = deck + discard + hand
    provinces = all_cards.count(PROVINCES)
    if CHAPEL in hand:
        for target in [CURSE, ESTATE]:
            while target in hand:
                hand.remove(target)
        if turn > 4:
            chapels = hand.count(CHAPEL) - 1
            for i in xrange(chapels):
                hand.remove(CHAPEL)
        coppers = hand.count(COPPER)
        all_coins = count_coins(all_cards)
        coppers = min(coppers, all_coins - COST[SILVER])
        if coins >= COST[PROVINCE]:
            coppers = min(coppers, coins - COST[PROVINCE])
        elif coins >= COST[GOLD]:
            coppers = min(coppers, coins - COST[GOLD])
        for i in xrange(coppers):
            hand.remove(COPPER)
        coins -= coppers
    if turn <= 2 and gain(CHAPEL, supply, discard): pass
    elif coins >= COST[PROVINCE] and gain(PROVINCE, supply, discard): pass
    elif BUY_DUCHIES and coins >= COST[DUCHY] and provinces > 3 and gain(DUCHY, supply, discard): pass
    elif BUY_ESTATES and coins >= COST[ESTATE] and provinces > 3 and gain(ESTATE, supply, discard): pass
    elif coins >= COST[GOLD] and gain(GOLD, supply, discard): pass
    elif turn == 3 and coins >= COST[CHAPEL] and hand.count(CHAPEL) == 2 and gain(CHAPEL, supply, discard): pass
    elif turn == 4 and coins >= COST[CHAPEL] and discard and hand.count(CHAPEL) == 2 and gain(CHAPEL, supply, discard): pass
    elif turn == 4 and coins >= COST[CHAPEL] and discard and hand.count(CHAPEL) == 1 and discard.count(CHAPEL) == 1 and gain(CHAPEL, supply, discard): pass
    elif coins >= COST[SILVER]: gain(SILVER, supply, discard)


@wrap_attacks
def chapel_lab(deck, discard, hand, turn, supply, labs=2):
    # Buy 1 Chapel, n Laboratories
    labs_used = 0
    while labs_used < hand.count(LABORATORY):
        labs_used += 1
        hand += draw(deck, discard, 2)
    coins = count_coins(hand)
    all_cards = deck + discard + hand
    if CHAPEL in hand:
        chapeled = 0
        for target in [CURSE, ESTATE]:
            while chapeled < 4 and target in hand:
                chapeled += 1
                hand.remove(target)
        all_coins = count_coins(all_cards)
        coppers = min(hand.count(COPPER), all_coins - COST[SILVER], 4 - chapeled)
        if coins >= COST[PROVINCE]:
            coppers = min(coppers, coins - COST[PROVINCE])
        elif coins >= COST[GOLD]:
            coppers = min(coppers, coins - COST[GOLD])
        elif coins >= COST[LABORATORY] and labs > 0 and LABORATORY not in all_cards:
            coppers = min(coppers, coins - COST[LABORATORY])
        for i in xrange(coppers):
            hand.remove(COPPER)
        coins -= coppers
    if coins < 5 and CHAPEL not in all_cards and gain(CHAPEL, supply, discard): pass
    elif coins >= COST[PROVINCE] and gain(PROVINCE, supply, discard): pass
    elif BUY_DUCHIES and coins >= COST[DUCHY] and all_cards.count(PROVINCE) > 3 and gain(DUCHY, supply, discard): pass
    elif BUY_ESTATES and coins >= COST[ESTATE] and all_cards.count(PROVINCE) > 3 and gain(ESTATE, supply, discard): pass
    elif coins >= COST[GOLD] and gain(GOLD, supply, discard): pass
    elif coins >= COST[LABORATORY] and all_cards.count(LABORATORY) < labs and gain(LABORATORY, supply, discard): pass
    elif coins >= COST[SILVER]: gain(SILVER, supply, discard)


@wrap_attacks
def courtyard(deck, discard, hand, turn, supply, n=1):
    # Buy n Courtyards
    played = []
    courtyards = (deck+discard+hand).count(COURTYARD)
    if COURTYARD in hand:
        move(COURTYARD, hand, played)
        hand += draw(deck, discard, 3)
        coins = count_coins(hand)
        if COURTYARD in hand:
            move(COURTYARD, hand, deck)
        else:
            best = (None, -1)
            # Put back the best card for next turn that still lets us make
            # the best possible buy this turn.
            for card, delta in [(GOLD, 3), (SILVER, 2), (COPPER, 1),
                                (ESTATE, 0), (PROVINCE, 0), (CURSE, 0)]:
                if card in hand:
                    reduced_coins = coins - delta
                    if reduced_coins >= COST[PROVINCE]:
                        value = 4
                    elif reduced_coins >= COST[GOLD]:
                        value = 3
                    elif reduced_coins >= COST[SILVER] and courtyards >= n:
                        value = 2
                    elif reduced_coins >= COST[COURTYARD] and courtyards < n:
                        value = 1
                    else:
                        value = 0
                    if value > best[1]:
                        best = (card, value)
            move(best[0], hand, deck)
    discard += played
    coins = count_coins(hand)
    all_cards = deck + discard + hand
    provinces = all_cards.count(PROVINCE)
    if coins >= COST[PROVINCE] and gain(PROVINCE, supply, discard): pass
    elif BUY_DUCHIES and coins >= COST[DUCHY] and provinces > 3 and gain(DUCHY, supply, discard): pass
    elif BUY_ESTATES and coins >= COST[ESTATE] and provinces > 3 and gain(ESTATE, supply, discard): pass
    elif coins >= COST[GOLD] and gain(GOLD, supply, discard): pass
    elif coins >= COST[COURTYARD] and courtyards < n and gain(COURTYARD, supply, discard): pass
    elif coins >= COST[SILVER]: gain(SILVER, supply, discard)


@wrap_attacks
def envoy(deck, discard, hand, turn, supply, n=1):
    # Buy n Envoys
    if ENVOY in hand:
        drawn = draw(deck, discard, 5)
        for card in [GOLD, SILVER, COPPER]:
            if card in drawn:
                move(card, drawn, discard)
                break
        hand += drawn
    coins = count_coins(hand)
    all_cards = deck + discard + hand
    if coins >= COST[PROVINCE] and gain(PROVINCE, supply, discard): pass
    elif BUY_DUCHIES and coins >= COST[DUCHY] and all_cards.count(PROVINCE) > 3 and gain(DUCHY, supply, discard): pass
    elif BUY_ESTATES and coins >= COST[ESTATE] and all_cards.count(PROVINCE) > 3 and gain(ESTATE, supply, discard): pass
    elif coins >= COST[GOLD] and gain(GOLD, supply, discard): pass
    elif coins >= COST[ENVOY] and all_cards.count(ENVOY) < n and gain(ENVOY, supply, discard): pass
    elif coins >= COST[SILVER]: gain(SILVER, supply, discard)


@wrap_attacks
def council_room(deck, discard, hand, turn, supply, n=1):
    # Buy n Council Rooms
    buys = 1
    my_attacks = []
    if COUNCIL_ROOM in hand:
        hand += draw(deck, discard, 4)
        buys += 1
        # Not really an attack, but this is an easy way to handle it.
        my_attacks.append(COUNCIL_ROOM)
    coins = count_coins(hand)
    all_cards = deck + discard + hand
    provinces = all_cards.count(PROVINCE)
    council_rooms = all_cards.count(COUNCIL_ROOM)
    while coins >= COST[SILVER] and buys > 0:
        buys -= 1
        if coins >= COST[PROVINCE] and gain(PROVINCE, supply, discard):
            coins -= COST[PROVINCE]
            provinces += 1
        elif BUY_DUCHIES and coins >= COST[DUCHY] and provinces > 3 and gain(DUCHY, supply, discard):
            coins -= COST[DUCHY]
        elif BUY_ESTATES and coins >= COST[ESTATE] and provinces > 3 and gain(ESTATE, supply, discard):
            coins -= COST[ESTATE]
        elif coins >= COST[GOLD] and gain(GOLD, supply, discard):
            coins -= COST[GOLD]
        elif coins >= COST[COUNCIL_ROOM] and council_rooms < n and gain(COUNCIL_ROOM, supply, discard):
            coins -= COST[COUNCIL_ROOM]
            council_rooms += 1
        elif gain(SILVER, supply, discard):
            coins -= COST[SILVER]
    return my_attacks


@wrap_attacks
def laboratory(deck, discard, hand, turn, supply, n=1):
    # Buy n Laboratories
    played = []
    while LABORATORY in hand:
        move(LABORATORY, hand, played)
        hand += draw(deck, discard, 2)
    discard += played
    coins = count_coins(hand)
    all_cards = deck + discard + hand
    provinces = all_cards.count(PROVINCE)
    if coins >= COST[PROVINCE] and gain(PROVINCE, supply, discard): pass
    elif BUY_DUCHIES and coins >= COST[DUCHY] and provinces > 3 and gain(DUCHY, supply, discard): pass
    elif BUY_ESTATES and coins >= COST[ESTATE] and provinces > 3 and gain(ESTATE, supply, discard): pass
    elif coins >= COST[GOLD] and gain(GOLD, supply, discard): pass
    elif coins >= COST[LABORATORY] and all_cards.count(LABORATORY) < n and gain(LABORATORY, supply, discard): pass
    elif coins >= 3: gain(SILVER, supply, discard)


@wrap_attacks
def market(deck, discard, hand, turn, supply, n=1):
    # Buy n Markets
    played = []
    while MARKET in hand:
        move(MARKET, hand, played)
        hand += draw(deck, discard, 1)
    coins = count_coins(hand) + len(played)
    buys = 1 + len(played)
    discard += played
    all_cards = deck + discard + hand
    provinces = all_cards.count(PROVINCE)
    markets = all_cards.count(MARKET)
    while coins >= COST[SILVER] and buys > 0:
        buys -= 1
        if coins >= COST[PROVINCE] and gain(PROVINCE, supply, discard):
            coins -= COST[PROVINCE]
            provinces += 1
        elif BUY_DUCHIES and coins >= COST[DUCHY] and provinces > 3 and gain(DUCHY, supply, discard):
            coins -= COST[DUCHY]
        elif BUY_ESTATES and coins >= COST[ESTATE] and provinces > 3 and gain(ESTATE, supply, discard):
            coins -= COST[ESTATE]
        elif coins >= COST[GOLD] and gain(GOLD, supply, discard):
            coins -= COST[GOLD]
        elif coins >= COST[MARKET] and markets < n and gain(MARKET, supply, discard):
            coins -= COST[MARKET]
            markets += 1
        elif gain(SILVER, supply, discard):
            coins -= COST[SILVER]


@wrap_attacks
def militia(deck, discard, hand, turn, supply, n=1):
    # Buy n Militias
    my_attacks = []
    coins = count_coins(hand)
    if MILITIA in hand:
        coins += 2
        my_attacks.append(MILITIA)
    all_cards = deck + discard + hand
    provinces = all_cards.count(PROVINCE)
    if coins >= COST[PROVINCE] and gain(PROVINCE, supply, discard): pass
    elif BUY_DUCHIES and coins >= COST[DUCHY] and provinces > 3 and gain(DUCHY, supply, discard): pass
    elif BUY_ESTATES and coins >= COST[ESTATE] and provinces > 3 and gain(ESTATE, supply, discard): pass
    elif coins >= COST[GOLD] and gain(GOLD, supply, discard): pass
    elif coins >= COST[MILITIA] and all_cards.count(MILITIA) < n and gain(MILITIA, supply, discard): pass
    elif coins >= COST[SILVER]: gain(SILVER, supply, discard)
    return my_attacks


@wrap_attacks
def mine_copper(deck, discard, hand, turn, supply, n=1):
    # Buy n Mines, prefer upgrading copper
    if MINE in hand:
        if COPPER in hand:
            hand.remove(COPPER)
            hand.append(SILVER)
        elif SILVER in hand:
            hand.remove(SILVER)
            hand.append(GOLD)
    all_cards = deck + discard + hand
    provinces = all_cards.count(PROVINCE)
    coins = count_coins(hand)
    if coins >= COST[PROVINCE] and gain(PROVINCE, supply, discard): pass
    elif BUY_DUCHIES and coins >= COST[DUCHY] and provinces > 3 and gain(DUCHY, supply, discard): pass
    elif BUY_ESTATES and coins >= COST[ESTATE] and provinces > 3 and gain(ESTATE, supply, discard): pass
    elif coins >= COST[GOLD] and gain(GOLD, supply, discard): pass
    elif coins >= COST[MINE] and all_cards.count(MINE) < n and gain(MINE, supply, discard): pass
    elif coins >= COST[SILVER]: gain(SILVER, supply, discard)


@wrap_attacks
def mine_silver(deck, discard, hand, turn, supply, n=1):
    # Buy n Mines, prefer upgrading silver
    if MINE in hand:
        if SILVER in hand:
            hand.remove(SILVER)
            hand.append(GOLD)
        elif COPPER in hand:
            hand.remove(COPPER)
            hand.append(SILVER)
    all_cards = deck + discard + hand
    provinces = all_cards.count(PROVINCE)
    coins = count_coins(hand)
    if coins >= COST[PROVINCE] and gain(PROVINCE, supply, discard): pass
    elif BUY_DUCHIES and coins >= COST[DUCHY] and provinces > 3 and gain(DUCHY, supply, discard): pass
    elif BUY_ESTATES and coins >= COST[ESTATE] and provinces > 3 and gain(ESTATE, supply, discard): pass
    elif coins >= COST[GOLD] and gain(GOLD, supply, discard): pass
    elif coins >= COST[MINE] and all_cards.count(MINE) < n and gain(MINE, supply, discard): pass
    elif coins >= COST[SILVER]: gain(SILVER, supply, discard)


@wrap_attacks
def minion(deck, discard, hand, turn, supply):
    my_attacks = []
    coins = count_coins(hand)
    bonus_coins = 0
    played = []
    while MINION in hand:
        move(MINION, hand, played)
        if MINION in hand or (coins + bonus_coins + 2) >= COST[PROVINCE]:
            bonus_coins += 2
        else:
            discard += hand
            hand[:] = draw(deck, discard, 4)
            coins = count_coins(hand)
            my_attacks.append(MINION)
    discard += played
    coins = coins + bonus_coins
    all_cards = deck + discard + hand
    provinces = all_cards.count(PROVINCE)
    if coins >= COST[PROVINCE] and gain(PROVINCE, supply, discard): pass
    elif BUY_DUCHIES and coins >= COST[DUCHY] and provinces > 3 and gain(DUCHY, supply, discard): pass
    elif BUY_ESTATES and coins >= COST[ESTATE] and provinces > 3 and gain(ESTATE, supply, discard): pass
    elif coins >= COST[GOLD] and gain(GOLD, supply, discard): pass
    elif coins >= COST[MINION] and gain(MINION, supply, discard): pass
    elif coins >= COST[SILVER]: gain(SILVER, supply, discard)
    return my_attacks


@wrap_attacks
def moat(deck, discard, hand, turn, supply, n=1):
    # Buy n Moats
    if MOAT in hand:
        hand += draw(deck, discard, 2)
    coins = count_coins(hand)
    all_cards = deck + discard + hand
    provinces = all_cards.count(PROVINCE)
    if coins >= COST[PROVINCE] and gain(PROVINCE, supply, discard): pass
    elif BUY_DUCHIES and coins >= COST[DUCHY] and provinces > 3 and gain(DUCHY, supply, discard): pass
    elif BUY_ESTATES and coins >= COST[ESTATE] and provinces > 3 and gain(ESTATE, supply, discard): pass
    elif coins >= COST[GOLD] and gain(GOLD, supply, discard): pass
    elif coins >= COST[MOAT] and all_cards.count(MOAT) < n and gain(MOAT, supply, discard): pass
    elif coins >= COST[SILVER]: gain(SILVER, supply, discard)


@wrap_attacks
def smithy(deck, discard, hand, turn, supply, n=1):
    # Buy n Smithies
    if SMITHY in hand:
        hand += draw(deck, discard, 3)
    coins = count_coins(hand)
    all_cards = deck + discard + hand
    provinces = all_cards.count(PROVINCE)
    smithies = all_cards.count(SMITHY)
    if coins >= COST[PROVINCE] and gain(PROVINCE, supply, discard): pass
    elif BUY_DUCHIES and coins >= COST[DUCHY] and provinces > 3 and gain(DUCHY, supply, discard): pass
    elif BUY_ESTATES and coins >= COST[ESTATE] and provinces > 3 and gain(ESTATE, supply, discard): pass
    elif coins >= COST[GOLD] and gain(GOLD, supply, discard): pass
    elif coins >= COST[SMITHY] and all_cards.count(SMITHY) < n and gain(SMITHY, supply, discard): pass
    elif coins >= COST[SILVER]: gain(SILVER, supply, discard)


def wharf(deck, discard, hand, turn, supply, n=1, attacks=None):
    # Buy n Wharfs
    buys = 1
    durations = []
    if "Wharf 1" in hand:
        durations.append(WHARF)
        hand.remove("Wharf 1")
        hand += draw(deck, discard, 3)
        buys += 1
    if attacks:
        handle_attacks(deck, discard, hand, turn, supply, attacks)
    if WHARF in hand:
        hand.remove(WHARF)
        hand += draw(deck, discard, 2)
        buys += 1
        deck.append("Wharf 1")  # Wharf duration placeholder
    coins = count_coins(hand)
    all_cards = deck + discard + hand
    provinces = all_cards.count(PROVINCE)
    wharves = all_cards.count(WHARF)
    while buys > 0:
        buys -= 1
        if coins >= COST[PROVINCE] and gain(PROVINCE, supply, discard):
            coins -= COST[PROVINCE]
            provinces += 1
        elif BUY_DUCHIES and coins >= COST[DUCHY] and provinces > 3 and gain(DUCHY, supply, discard):
            coins -= COST[DUCHY]
        elif BUY_ESTATES and coins >= COST[ESTATE] and provinces > 3 and gain(ESTATE, supply, discard):
            coins -= COST[ESTATE]
        elif coins >= COST[GOLD] and gain(GOLD, supply, discard):
            coins -= COST[GOLD]
        elif coins >= COST[WHARF] and wharves < n and gain(WHARF, supply, discard):
            coins -= COST[WHARF]
            wharves += 1
        elif coins >= COST[SILVER] and gain(SILVER, supply, discard):
            coins -= COST[SILVER]
        else:
            break


@wrap_attacks
def witch(deck, discard, hand, turn, supply, n=1):
    # Buy n Witches
    my_attacks = []
    if WITCH in hand:
        hand += draw(deck, discard, 2)
        my_attacks.append(WITCH)
    coins = count_coins(hand)
    all_cards = deck + discard + hand
    provinces = all_cards.count(PROVINCE)
    if coins >= COST[PROVINCE] and gain(PROVINCE, supply, discard): pass
    elif BUY_DUCHIES and coins >= COST[DUCHY] and provinces > 3 and gain(DUCHY, supply, discard): pass
    elif BUY_ESTATES and coins >= COST[ESTATE] and provinces > 3 and gain(ESTATE, supply, discard): pass
    elif coins >= COST[GOLD] and gain(GOLD, supply, discard): pass
    elif coins >= COST[WITCH] and all_cards.count(WITCH) < n and gain(WITCH, supply, discard): pass
    elif coins >= COST[SILVER]: gain(SILVER, supply, discard)
    return my_attacks


@wrap_attacks
def big_money(deck, discard, hand, turn, supply):
    # Buy no kingdom cards at all
    coins = count_coins(hand)
    all_cards = deck + discard + hand
    provinces = all_cards.count(PROVINCE)
    if coins >= COST[PROVINCE] and gain(PROVINCE, supply, discard): pass
    elif BUY_DUCHIES and coins >= COST[DUCHY] and provinces > 3 and gain(DUCHY, supply, discard): pass
    elif BUY_ESTATES and coins >= COST[ESTATE] and provinces > 3 and gain(ESTATE, supply, discard): pass
    elif coins >= COST[GOLD] and gain(GOLD, supply, discard): pass
    elif coins >= COST[SILVER]: gain(SILVER, supply, discard)


@wrap_attacks
def early_gold(deck, discard, hand, turn, supply, g=0):
    # Test buying a gold when drawing 8+ coins after buying only g gold.
    if SMITHY in hand:
        hand += draw(deck, discard, 3)
    coins = count_coins(hand)
    all_cards = (deck + discard + hand)
    if coins >= COST[GOLD] and all_cards.count(GOLD) < g and gain(GOLD, supply, discard): pass
    elif coins >= COST[PROVINCE] and all_cards.count(GOLD) == g and gain(GOLD, supply, discard): pass
    elif coins >= COST[PROVINCE] and gain(PROVINCE, supply, discard): pass
    elif coins >= COST[GOLD] and all_cards.count(GOLD) == g:
        raise InvalidGameError
    elif coins >= COST[GOLD] and gain(GOLD, supply, discard): pass
    elif coins >= COST[SMITHY] and SMITHY not in all_cards and gain(SMITHY, supply, discard): pass
    elif coins >= COST[SILVER]: gain(SILVER, supply, discard)


@wrap_attacks
def early_province(deck, discard, hand, turn, supply, g=0):
    # Test buying a province when drawing 8+ coins after buying only g gold.
    if SMITHY in hand:
        hand += draw(deck, discard, 3)
    coins = count_coins(hand)
    all_cards = (deck + discard + hand)
    if coins >= COST[GOLD] and all_cards.count(GOLD) < g and gain(GOLD, supply, discard): pass
    elif coins >= COST[PROVINCE] and gain(PROVINCE, supply, discard): pass
    elif coins >= COST[GOLD] and PROVINCE not in all_cards:
        raise InvalidGameError
    elif coins >= COST[GOLD] and gain(GOLD, supply, discard): pass
    elif coins >= COST[SMITHY] and SMITHY not in all_cards and gain(SMITHY, supply, discard): pass
    elif coins >= COST[SILVER]: gain(SILVER, supply, discard)


@wrap_attacks
def turn3_gold(deck, discard, hand, turn, supply):
    # Test buying a gold when drawing 8+ coins on turn 3.
    coins = count_coins(hand)
    if BARON in hand and ESTATE in hand:
        move(ESTATE, hand, discard)
        coins += 4
    all_cards = (deck + discard + hand)
    if coins >= COST[PROVINCE] and GOLD not in all_cards and gain(GOLD, supply, discard): pass
    elif coins >= COST[PROVINCE] and gain(PROVINCE, supply, discard): pass
    elif turn == 3:
        raise InvalidGameError
    elif coins >= COST[GOLD] and gain(GOLD, supply, discard): pass
    elif coins >= COST[BARON] and BARON not in all_cards and gain(BARON, supply, discard): pass
    elif coins >= COST[SILVER]: gain(SILVER, supply, discard)


@wrap_attacks
def super_early_province(deck, discard, hand, turn, supply):
    # Test buying a province when drawing 8+ coins on turn 3.
    coins = count_coins(hand)
    if BARON in hand and ESTATE in hand:
        move(ESTATE, hand, discard)
        coins += 4
    all_cards = (deck + discard + hand)
    if coins >= COST[PROVINCE] and gain(PROVINCE, supply, discard): pass
    elif turn == 3:
        raise InvalidGameError
    elif coins >= COST[GOLD] and gain(GOLD, supply, discard): pass
    elif coins >= COST[BARON] and BARON not in all_cards and gain(BARON, supply, discard): pass
    elif coins >= COST[SILVER]: gain(SILVER, supply, discard)


if __name__ == "__main__":
    main()
