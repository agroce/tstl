import covertool
covertool.cover("domsim.py:1")
from collections import defaultdict
covertool.cover("domsim.py:2")
from functools import wraps
covertool.cover("domsim.py:3")
from random import shuffle

covertool.cover("domsim.py:5")
try:
    import psyco
    covertool.cover("domsim.py:7")
    psyco.full()
except ImportError:
    covertool.cover("domsim.py:9")
    pass


# Set whether most strategies will buy Duchies and Estates.  This is useful to
# reduce draws in simulations of full games.  In 4-Province Solitaire, it just
# slows the deck down.
covertool.cover("domsim.py:15")
BUY_DUCHIES = BUY_ESTATES = True


def main():
    covertool.cover("domsim.py:19")
    tries = 10000
    # Test Big Money, Chapel, and Smithy in 4-Province Solitaire.
    covertool.cover("domsim.py:21")
    test("Big Money", tries, big_money)
    covertool.cover("domsim.py:22")
    test(CHAPEL, tries, chapel)
    covertool.cover("domsim.py:23")
    test(SMITHY, tries, smithy)
    # Run a test match between Smithy and Chapel.
    covertool.cover("domsim.py:25")
    test_matches(tries, [
        (SMITHY, smithy, {}),
        (CHAPEL, chapel, {}),
    covertool.cover("domsim.py:28")
    ])


# Card name constants
covertool.cover("domsim.py:32")
ADVENTURER = 'Adventurer'
covertool.cover("domsim.py:33")
BARON = 'Baron'
covertool.cover("domsim.py:34")
BUREAUCRAT = 'Bureaucrat'
covertool.cover("domsim.py:35")
CHANCELLOR = 'Chancellor'
covertool.cover("domsim.py:36")
CHAPEL = 'Chapel'
covertool.cover("domsim.py:37")
COPPER = 'Copper'
covertool.cover("domsim.py:38")
COUNCIL_ROOM = 'Council Room'
covertool.cover("domsim.py:39")
COURTYARD = 'Courtyard'
covertool.cover("domsim.py:40")
CURSE = 'Curse'
covertool.cover("domsim.py:41")
DUCHY = 'Duchy'
covertool.cover("domsim.py:42")
DUKE = 'Duke'
covertool.cover("domsim.py:43")
ENVOY = 'Envoy'
covertool.cover("domsim.py:44")
ESTATE = 'Estate'
covertool.cover("domsim.py:45")
GARDENS = 'Gardens'
covertool.cover("domsim.py:46")
GREAT_HALL = 'Great Hall'
covertool.cover("domsim.py:47")
GOLD = 'Gold'
covertool.cover("domsim.py:48")
HAREM = 'Harem'
covertool.cover("domsim.py:49")
ISLAND = 'Island'
covertool.cover("domsim.py:50")
LABORATORY = 'Laboratory'
covertool.cover("domsim.py:51")
MARKET = 'Market'
covertool.cover("domsim.py:52")
MILITIA = 'Militia'
covertool.cover("domsim.py:53")
MINE = 'Mine'
covertool.cover("domsim.py:54")
MINION = 'Minion'
covertool.cover("domsim.py:55")
MOAT = 'Moat'
covertool.cover("domsim.py:56")
NOBLES = 'Nobles'
covertool.cover("domsim.py:57")
PROVINCE = 'Province'
covertool.cover("domsim.py:58")
REMODEL = 'Remodel'
covertool.cover("domsim.py:59")
SCOUT = 'Scout'
covertool.cover("domsim.py:60")
SEA_HAG = 'Sea Hag'
covertool.cover("domsim.py:61")
SILVER = 'Silver'
covertool.cover("domsim.py:62")
SMITHY = 'Smithy'
covertool.cover("domsim.py:63")
THRONE_ROOM = 'Throne Room'
covertool.cover("domsim.py:64")
VILLAGE = 'Village'
covertool.cover("domsim.py:65")
WHARF = 'Wharf'
covertool.cover("domsim.py:66")
WITCH = 'Witch'


# Card costs
covertool.cover("domsim.py:70")
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


covertool.cover("domsim.py:109")
TREASURE_CARDS = [COPPER, SILVER, GOLD, HAREM]
covertool.cover("domsim.py:110")
VICTORY_CARDS = [ESTATE, DUCHY, PROVINCE, GARDENS,
                 DUKE, GREAT_HALL, HAREM, NOBLES,
                 ISLAND]


# Utility functions


def setup():
    covertool.cover("domsim.py:119")
    "Set up a starting deck and discard pile."
    covertool.cover("domsim.py:120")
    deck = [COPPER] * 7 + [ESTATE] * 3
    covertool.cover("domsim.py:121")
    shuffle(deck)
    covertool.cover("domsim.py:122")
    discard = []
    covertool.cover("domsim.py:123")
    return deck, discard, 0


def setup_supply(players):
    covertool.cover("domsim.py:127")
    "Set up a supply."
    covertool.cover("domsim.py:128")
    supply = defaultdict(lambda: 10)
    covertool.cover("domsim.py:129")
    victory_cards = 8 if players <= 2 else 12
    covertool.cover("domsim.py:130")
    for card in VICTORY_CARDS:
        covertool.cover("domsim.py:131")
        supply[card] = victory_cards
    covertool.cover("domsim.py:132")
    if players > 4:
        covertool.cover("domsim.py:133")
        supply[PROVINCE] = 3 * players
    covertool.cover("domsim.py:134")
    supply[CURSE] = 10 * (players - 1)
    covertool.cover("domsim.py:135")
    supply[COPPER] = 60
    covertool.cover("domsim.py:136")
    supply[SILVER] = 40
    covertool.cover("domsim.py:137")
    supply[GOLD] = 30
    covertool.cover("domsim.py:138")
    return supply


def match_setup(base_setup=setup):
    covertool.cover("domsim.py:142")
    "Set up a starting deck, discard pile, and hand."
    covertool.cover("domsim.py:143")
    deck, discard, turn = base_setup()
    covertool.cover("domsim.py:144")
    hand = draw(deck, discard, 5)
    covertool.cover("domsim.py:145")
    return [deck, discard, hand, turn, []]


def draw(deck, discard, n):
    covertool.cover("domsim.py:149")
    "Draw n cards, shuffling if needed.  Returns the cards drawn."
    covertool.cover("domsim.py:150")
    if n == 0:
        covertool.cover("domsim.py:151")
        return []
    covertool.cover("domsim.py:152")
    d = min(len(deck), n)
    covertool.cover("domsim.py:153")
    hand = deck[-d:]
    covertool.cover("domsim.py:154")
    del deck[-d:]
    covertool.cover("domsim.py:155")
    if d < n:
        covertool.cover("domsim.py:156")
        deck[:] = discard
        covertool.cover("domsim.py:157")
        del discard[:]
        covertool.cover("domsim.py:158")
        shuffle(deck)
        covertool.cover("domsim.py:159")
        d = min(len(deck), n - d)
        covertool.cover("domsim.py:160")
        hand += deck[-d:]
        covertool.cover("domsim.py:161")
        del deck[-d:]
    covertool.cover("domsim.py:162")
    return hand


def move(card, from_, to):
    """Move a card from one location to another.

    If the destination is the deck, the card will be on the top.
    """
    covertool.cover("domsim.py:170")
    from_.remove(card)
    covertool.cover("domsim.py:171")
    to.append(card)


def gain(card, supply, to):
    """Gain a card from the supply, putting it in the 'to' location.

    Returns True iff successful.
    """
    covertool.cover("domsim.py:179")
    if supply[card]:
        covertool.cover("domsim.py:180")
        supply[card] -= 1
        covertool.cover("domsim.py:181")
        to.append(card)
        covertool.cover("domsim.py:182")
        return True
    else:
        covertool.cover("domsim.py:184")
        return False


def count_coins(hand):
    covertool.cover("domsim.py:188")
    "Count the total coins from Treasure cards in a list of cards."
    covertool.cover("domsim.py:189")
    return (hand.count(COPPER) + 2 * hand.count(SILVER) +
            3 * hand.count(GOLD) + 2 * hand.count(HAREM))


def treasure_value(deck):
    covertool.cover("domsim.py:194")
    "Compute the average value of the Treasure cards in a deck."
    covertool.cover("domsim.py:195")
    treasure =  [1] * deck.count(COPPER)
    covertool.cover("domsim.py:196")
    treasure += [2] * deck.count(SILVER)
    covertool.cover("domsim.py:197")
    treasure += [3] * deck.count(GOLD)
    covertool.cover("domsim.py:198")
    treasure += [2] * deck.count(HAREM)
    covertool.cover("domsim.py:199")
    if treasure:
        covertool.cover("domsim.py:200")
        return float(sum(treasure)) / len(treasure)


def score(deck):
    covertool.cover("domsim.py:204")
    "Count the total score of a deck."
    covertool.cover("domsim.py:205")
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
    covertool.cover("domsim.py:219")
    if attack == COUNCIL_ROOM:
        # Not really an attack, but this is an easy way to handle it.
        covertool.cover("domsim.py:221")
        hand += draw(deck, discard, 1)
        covertool.cover("domsim.py:222")
        return True
    elif MOAT in hand:
        covertool.cover("domsim.py:224")
        return True
    elif attack == MINION and len(hand) > 4:
        covertool.cover("domsim.py:226")
        discard += hand
        covertool.cover("domsim.py:227")
        hand[:] = draw(deck, discard, 4)
        covertool.cover("domsim.py:228")
        return True
    elif attack == WITCH:
        covertool.cover("domsim.py:230")
        gain(CURSE, supply, discard)
        covertool.cover("domsim.py:231")
        return True
    elif attack == SEA_HAG:
        covertool.cover("domsim.py:233")
        discard += draw(deck, discard, 1)
        covertool.cover("domsim.py:234")
        gain(CURSE, supply, deck)
        covertool.cover("domsim.py:235")
        return True
    else:
        covertool.cover("domsim.py:237")
        return False


def handle_attacks(deck, discard, hand, turn, supply, attacks,
                   handlers=[default_attack_handler]):
    """Dispatch attacks to handlers.  For each attack in order, attempts to
    apply each handler in order.  Raises an UnhandledAttack exception if any
    attack remains unhandled.
    """
    covertool.cover("domsim.py:246")
    for attack in attacks:
        covertool.cover("domsim.py:247")
        for handler in handlers:
            covertool.cover("domsim.py:248")
            if handler(deck, discard, hand, turn, supply, attack):
                covertool.cover("domsim.py:249")
                break
        else:
            covertool.cover("domsim.py:251")
            raise UnhandledAttack(attack)


def wrap_attacks(strategy):
    covertool.cover("domsim.py:255")
    "Decorator to handle basic attacks quietly without code modification."
    covertool.cover("domsim.py:256")
    @wraps(strategy)
    def wrapper(deck, discard, hand, turn, supply, attacks=None, **kwargs):
        covertool.cover("domsim.py:258")
        if attacks:
            covertool.cover("domsim.py:259")
            handle_attacks(deck, discard, hand, turn, supply, attacks)
        covertool.cover("domsim.py:260")
        return strategy(deck, discard, hand, turn, supply, **kwargs)
    covertool.cover("domsim.py:261")
    return wrapper


class UnhandledAttack(Exception):
    covertool.cover("domsim.py:265")
    "Signal that an attack has not been handled."


class InvalidGameError(Exception):
    covertool.cover("domsim.py:269")
    "Signal that a simulation should be aborted and not counted."


def test_game(strategy, setup=setup, **kwargs):
    """Run a single test game using a given strategy.

    Returns the total number of turns taken to reach 4 Provinces and the
    final score of the deck.
    """
    covertool.cover("domsim.py:278")
    deck, discard, turns = setup()
    covertool.cover("domsim.py:279")
    supply = setup_supply(2)
    covertool.cover("domsim.py:280")
    while (deck + discard).count(PROVINCE) < 4:
        covertool.cover("domsim.py:281")
        turns += 1
        covertool.cover("domsim.py:282")
        hand = draw(deck, discard, 5)
        covertool.cover("domsim.py:283")
        strategy(deck, discard, hand, turns, supply, **kwargs)
        covertool.cover("domsim.py:284")
        discard += hand
    covertool.cover("domsim.py:285")
    return turns, score(deck + discard)


def test_minion(strategy, setup=setup, **kwargs):
    """Run a single test game against a strong Minion deck using a given strategy.

    Returns the total number of turns taken to reach 4 Provinces and the
    final score of the deck.
    """
    covertool.cover("domsim.py:294")
    deck, discard, turns = setup()
    covertool.cover("domsim.py:295")
    supply = setup_supply(2)
    covertool.cover("domsim.py:296")
    while (deck + discard).count(PROVINCE) < 4:
        covertool.cover("domsim.py:297")
        turns += 1
        # Assume that we get hit by a Minion on turn 3, turn 5, and every turn
        # thereafter.
        covertool.cover("domsim.py:300")
        if turns == 3 or turns >= 5:
            covertool.cover("domsim.py:301")
            discard += draw(deck, discard, 5)
            covertool.cover("domsim.py:302")
            hand = draw(deck, discard, 4)
        else:
            covertool.cover("domsim.py:304")
            hand = draw(deck, discard, 5)
        covertool.cover("domsim.py:305")
        strategy(deck, discard, hand, turns, supply, **kwargs)
        covertool.cover("domsim.py:306")
        discard += hand
    covertool.cover("domsim.py:307")
    return turns, score(deck + discard)


def test_match(strategies, setup=match_setup):
    """Run a single test match between multiple decks.

    Returns the winning strategies.
    """
    covertool.cover("domsim.py:315")
    DECK, DISCARD, HAND, TURNS, ATTACKS = range(5)
    covertool.cover("domsim.py:316")
    supply = setup_supply(len(strategies))
    covertool.cover("domsim.py:317")
    players = [setup() for _ in strategies]
    covertool.cover("domsim.py:318")
    player_index = 0

    while True:
        covertool.cover("domsim.py:321")
        if supply[PROVINCE] == 0:
            covertool.cover("domsim.py:322")
            break
        covertool.cover("domsim.py:323")
        if len(strategies) <= 4 and supply.values().count(0) >= 3:
            covertool.cover("domsim.py:324")
            break
        covertool.cover("domsim.py:325")
        if len(strategies) > 4 and supply.values().count(0) >= 4:
            covertool.cover("domsim.py:326")
            break
        covertool.cover("domsim.py:327")
        p = players[player_index]
        covertool.cover("domsim.py:328")
        name, strategy, kwargs = strategies[player_index]
        covertool.cover("domsim.py:329")
        p[TURNS] += 1
        covertool.cover("domsim.py:330")
        my_attacks = strategy(p[DECK], p[DISCARD], p[HAND], p[TURNS], supply,
                              attacks=p[ATTACKS], **kwargs) or []
        covertool.cover("domsim.py:332")
        p[DISCARD] += p[HAND]
        covertool.cover("domsim.py:333")
        p[HAND] = draw(p[DECK], p[DISCARD], 5)
        covertool.cover("domsim.py:334")
        p[ATTACKS] = []
        covertool.cover("domsim.py:335")
        for i, opp in enumerate(players):
            covertool.cover("domsim.py:336")
            if i != player_index:
                covertool.cover("domsim.py:337")
                opp[ATTACKS] += my_attacks
        covertool.cover("domsim.py:338")
        player_index = (player_index + 1) % len(strategies)

    best_score = None
    winners = []
    for strategy, p in zip(strategies, players):
        covertool.cover("domsim.py:343")
        player_score = (score(p[DECK] + p[DISCARD] + p[HAND]), -p[TURNS])
        covertool.cover("domsim.py:344")
        if player_score > best_score:
            covertool.cover("domsim.py:345")
            best_score = player_score
            covertool.cover("domsim.py:346")
            winners = [strategy[0]]
        elif player_score == best_score:
            covertool.cover("domsim.py:348")
            winners.append(strategy[0])
    covertool.cover("domsim.py:349")
    return winners


def test_coins(strategy, setup=setup, turns=None, **kwargs):
    """Run a single test game using a given strategy through a given turn.

    Returns the total number of coins received.
    """
    covertool.cover("domsim.py:357")
    coins = 0
    covertool.cover("domsim.py:358")
    deck, discard, turns_taken = setup()
    covertool.cover("domsim.py:359")
    supply = setup_supply(2)
    covertool.cover("domsim.py:360")
    while turns_taken < turns:
        covertool.cover("domsim.py:361")
        turns_taken += 1
        covertool.cover("domsim.py:362")
        hand = draw(deck, discard, 5)
        covertool.cover("domsim.py:363")
        coins += strategy(deck, discard, hand, turns_taken, supply, **kwargs)
        covertool.cover("domsim.py:364")
        discard += hand
    covertool.cover("domsim.py:365")
    return turns_taken, coins


def test(name, tries, strategy, runner=test_game, **kwargs):
    covertool.cover("domsim.py:369")
    "Run a series of test games and print the results."
    covertool.cover("domsim.py:370")
    times = []
    covertool.cover("domsim.py:371")
    scores = []
    covertool.cover("domsim.py:372")
    total_tries = 0
    covertool.cover("domsim.py:373")
    while len(times) < tries:
        covertool.cover("domsim.py:374")
        total_tries += 1
        covertool.cover("domsim.py:375")
        try:
            covertool.cover("domsim.py:376")
            time, score = runner(strategy, **kwargs)
        except InvalidGameError as e:
            covertool.cover("domsim.py:378")
            raise e
        else:
            covertool.cover("domsim.py:380")
            times.append(time)
            covertool.cover("domsim.py:381")
            scores.append(score)
    covertool.cover("domsim.py:382")
    times.sort()
    covertool.cover("domsim.py:383")
    scores.sort()
    covertool.cover("domsim.py:384")
    print name
    covertool.cover("domsim.py:385")
    num = len(times)
    covertool.cover("domsim.py:386")
    print "Num = %d" % num
    covertool.cover("domsim.py:387")
    print "Tot = %d" % total_tries
    covertool.cover("domsim.py:388")
    print "Min = %d" % times[0]
    covertool.cover("domsim.py:389")
    if num % 2 == 1:
        covertool.cover("domsim.py:390")
        print "Med = %d" % times[num // 2]
    else:
        covertool.cover("domsim.py:392")
        print "Med = %f" % (float(times[num // 2 - 1] + times[num // 2]) / 2)
    covertool.cover("domsim.py:393")
    print "Max = %d" % times[-1]
    covertool.cover("domsim.py:394")
    avg = float(sum(times)) / num
    covertool.cover("domsim.py:395")
    print "Avg = %f" % avg
    covertool.cover("domsim.py:396")
    print "StD = %f" % ((sum((x-avg)**2 for x in times) / (num-1)) ** 0.5)
    covertool.cover("domsim.py:397")
    print "Avg Score = %f" % (float(sum(scores)) / num)
    covertool.cover("domsim.py:398")
    print


def test_matches(tries, strategies, runner=test_match, **kwargs):
    covertool.cover("domsim.py:402")
    "Run a series of test matches and print the results."
    covertool.cover("domsim.py:403")
    winners = []
    covertool.cover("domsim.py:404")
    total_tries = matches = 0
    covertool.cover("domsim.py:405")
    _strategies = strategies[:]
    covertool.cover("domsim.py:406")
    while matches < tries:
        covertool.cover("domsim.py:407")
        total_tries += 1
        covertool.cover("domsim.py:408")
        try:
            covertool.cover("domsim.py:409")
            shuffle(_strategies)
            covertool.cover("domsim.py:410")
            winners += runner(_strategies, **kwargs)
            covertool.cover("domsim.py:411")
            matches += 1
        except InvalidGameError as e:
            covertool.cover("domsim.py:413")
            raise e
    covertool.cover("domsim.py:414")
    print "Num = %d" % matches
    covertool.cover("domsim.py:415")
    print "Tot = %d" % total_tries
    covertool.cover("domsim.py:416")
    for strategy in strategies:
        covertool.cover("domsim.py:417")
        name = strategy[0]
        covertool.cover("domsim.py:418")
        print name, winners.count(name), float(winners.count(name)) / matches
    covertool.cover("domsim.py:419")
    print


# Strategy functions

covertool.cover("domsim.py:424")
@wrap_attacks
def adventurer(deck, discard, hand, turn, supply, n=1):
    # Buy n Adventurers
    covertool.cover("domsim.py:427")
    if ADVENTURER in hand:
        covertool.cover("domsim.py:428")
        aside = []
        covertool.cover("domsim.py:429")
        treasures_found = 0
        covertool.cover("domsim.py:430")
        while (deck or discard) and treasures_found < 2:
            covertool.cover("domsim.py:431")
            card = draw(deck, discard, 1)
            covertool.cover("domsim.py:432")
            if card[0] in TREASURE_CARDS:
                covertool.cover("domsim.py:433")
                hand += card
                covertool.cover("domsim.py:434")
                treasures_found += 1
            else:
                covertool.cover("domsim.py:436")
                aside += card
        covertool.cover("domsim.py:437")
        discard += aside
    covertool.cover("domsim.py:438")
    coins = count_coins(hand)
    covertool.cover("domsim.py:439")
    all_cards = deck + discard + hand
    covertool.cover("domsim.py:440")
    provinces = all_cards.count(PROVINCE)
    covertool.cover("domsim.py:441")
    if coins >= COST[PROVINCE] and gain(PROVINCE, supply, discard):
            covertool.cover("domsim.py:441:True")
            pass

    elif BUY_DUCHIES and coins >= COST[DUCHY] and provinces > 3 and gain(DUCHY, supply, discard):
            covertool.cover("domsim.py:442:True")
            pass

    elif BUY_ESTATES and coins >= COST[ESTATE] and provinces > 3 and gain(ESTATE, supply, discard):
            covertool.cover("domsim.py:443:True")
            pass

    elif coins >= COST[ADVENTURER] and all_cards.count(ADVENTURER) < n and gain(ADVENTURER, supply, discard):
            covertool.cover("domsim.py:444:True")
            pass

    elif coins >= COST[GOLD] and gain(GOLD, supply, discard):
            covertool.cover("domsim.py:445:True")
            pass

    elif coins >= COST[SILVER]:
        covertool.cover("domsim.py:447")
        gain(SILVER, supply, discard)


covertool.cover("domsim.py:450")
@wrap_attacks
def baron(deck, discard, hand, turn, supply):
    # Buy 1 Baron
    covertool.cover("domsim.py:453")
    coins = count_coins(hand)
    covertool.cover("domsim.py:454")
    buys = 1
    covertool.cover("domsim.py:455")
    if BARON in hand and ESTATE in hand:
        covertool.cover("domsim.py:456")
        coins += 4
        covertool.cover("domsim.py:457")
        buys += 1
    covertool.cover("domsim.py:458")
    all_cards = deck + discard + hand
    covertool.cover("domsim.py:459")
    provinces = all_cards.count(PROVINCE)
    covertool.cover("domsim.py:460")
    has_baron = BARON in all_cards
    covertool.cover("domsim.py:461")
    while coins >= 3 and buys > 0:
        covertool.cover("domsim.py:462")
        buys -= 1
        covertool.cover("domsim.py:463")
        if coins >= COST[PROVINCE] and gain(PROVINCE, supply, discard):
            covertool.cover("domsim.py:464")
            coins -= COST[PROVINCE]
            covertool.cover("domsim.py:465")
            provinces += 1
        elif BUY_DUCHIES and coins >= COST[DUCHY] and provinces > 3 and gain(DUCHY, supply, discard):
            covertool.cover("domsim.py:467")
            coins -= COST[DUCHY]
        elif BUY_ESTATES and coins >= COST[ESTATE] and provinces > 3 and gain(ESTATE, supply, discard):
            covertool.cover("domsim.py:469")
            coins -= COST[ESTATE]
        elif coins >= COST[GOLD] and gain(GOLD, supply, discard):
            covertool.cover("domsim.py:471")
            coins -= COST[GOLD]
        elif coins >= COST[BARON] and not has_baron and gain(BARON, supply, discard):
            covertool.cover("domsim.py:473")
            coins -= COST[BARON]
            covertool.cover("domsim.py:474")
            has_baron = True
        elif coins >= COST[SILVER] and gain(SILVER, supply, discard):
            covertool.cover("domsim.py:476")
            coins -= COST[SILVER]
        else:
            covertool.cover("domsim.py:478")
            break


covertool.cover("domsim.py:481")
@wrap_attacks
def baron_estate(deck, discard, hand, turn, supply):
    # Buy 1 Baron, use it even without an Estate in hand
    covertool.cover("domsim.py:484")
    coins = count_coins(hand)
    covertool.cover("domsim.py:485")
    buys = 1
    covertool.cover("domsim.py:486")
    if BARON in hand:
        covertool.cover("domsim.py:487")
        buys += 1
        covertool.cover("domsim.py:488")
        if ESTATE in hand:
            covertool.cover("domsim.py:489")
            coins += 4
        else:
            covertool.cover("domsim.py:491")
            gain(ESTATE, supply, discard)
    covertool.cover("domsim.py:492")
    all_cards = deck + discard + hand
    covertool.cover("domsim.py:493")
    provinces = all_cards.count(PROVINCE)
    covertool.cover("domsim.py:494")
    has_baron = BARON in all_cards
    covertool.cover("domsim.py:495")
    while coins >= 3 and buys > 0:
        covertool.cover("domsim.py:496")
        buys -= 1
        covertool.cover("domsim.py:497")
        if coins >= COST[PROVINCE] and gain(PROVINCE, supply, discard):
            covertool.cover("domsim.py:498")
            coins -= COST[PROVINCE]
            covertool.cover("domsim.py:499")
            provinces += 1
        elif BUY_DUCHIES and coins >= COST[DUCHY] and provinces > 3 and gain(DUCHY, supply, discard):
            covertool.cover("domsim.py:501")
            coins -= COST[DUCHY]
        elif BUY_ESTATES and coins >= COST[ESTATE] and provinces > 3 and gain(ESTATE, supply, discard):
            covertool.cover("domsim.py:503")
            coins -= COST[ESTATE]
        elif coins >= COST[GOLD] and gain(GOLD, supply, discard):
            covertool.cover("domsim.py:505")
            coins -= COST[GOLD]
        elif coins >= COST[BARON] and not has_baron and gain(BARON, supply, discard):
            covertool.cover("domsim.py:507")
            coins -= COST[BARON]
            covertool.cover("domsim.py:508")
            has_baron = True
        elif coins >= COST[SILVER] and gain(SILVER, supply, discard):
            covertool.cover("domsim.py:510")
            coins -= COST[SILVER]
        else:
            covertool.cover("domsim.py:512")
            break


covertool.cover("domsim.py:515")
@wrap_attacks
def bureaucrat(deck, discard, hand, turn, supply, n=1):
    # Buy n Bureaucrats
    covertool.cover("domsim.py:518")
    all_cards = deck + discard + hand
    covertool.cover("domsim.py:519")
    provinces = all_cards.count(PROVINCE)
    covertool.cover("domsim.py:520")
    my_attacks = []
    covertool.cover("domsim.py:521")
    if BUREAUCRAT in hand:
        covertool.cover("domsim.py:522")
        gain(SILVER, supply, deck)
        covertool.cover("domsim.py:523")
        my_attacks.append(BUREAUCRAT)
    covertool.cover("domsim.py:524")
    coins = count_coins(hand)
    covertool.cover("domsim.py:525")
    if coins >= COST[PROVINCE] and gain(PROVINCE, supply, discard):
            covertool.cover("domsim.py:525:True")
            pass

    elif BUY_DUCHIES and coins >= COST[DUCHY] and provinces > 3 and gain(DUCHY, supply, discard):
            covertool.cover("domsim.py:526:True")
            pass

    elif BUY_ESTATES and coins >= COST[ESTATE] and provinces > 3 and gain(ESTATE, supply, discard):
            covertool.cover("domsim.py:527:True")
            pass

    elif coins >= COST[GOLD] and gain(GOLD, supply, discard):
            covertool.cover("domsim.py:528:True")
            pass

    elif coins >= COST[BUREAUCRAT] and all_cards.count(BUREAUCRAT) < n and gain(BUREAUCRAT, supply, discard):
            covertool.cover("domsim.py:529:True")
            pass

    elif coins >= COST[SILVER] and gain(SILVER, supply, discard):
            covertool.cover("domsim.py:530:True")
            pass

    covertool.cover("domsim.py:531")
    return my_attacks


covertool.cover("domsim.py:534")
@wrap_attacks
def chancellor(deck, discard, hand, turn, supply, n=0):
    # Buy n Chancellors, always choose to shuffle.
    covertool.cover("domsim.py:537")
    coins = count_coins(hand)
    covertool.cover("domsim.py:538")
    if CHANCELLOR in hand:
        covertool.cover("domsim.py:539")
        coins += 2
        covertool.cover("domsim.py:540")
        discard += deck
        covertool.cover("domsim.py:541")
        del deck[:]
    covertool.cover("domsim.py:542")
    all_cards = deck + discard + hand
    covertool.cover("domsim.py:543")
    provinces = all_cards.count(PROVINCE)
    covertool.cover("domsim.py:544")
    if coins >= COST[PROVINCE] and gain(PROVINCE, supply, discard):
            covertool.cover("domsim.py:544:True")
            pass

    elif BUY_DUCHIES and coins >= COST[DUCHY] and provinces > 3 and gain(DUCHY, supply, discard):
            covertool.cover("domsim.py:545:True")
            pass

    elif BUY_ESTATES and coins >= COST[ESTATE] and provinces > 3 and gain(ESTATE, supply, discard):
            covertool.cover("domsim.py:546:True")
            pass

    elif coins >= COST[GOLD] and gain(GOLD, supply, discard):
            covertool.cover("domsim.py:547:True")
            pass

    elif coins >= COST[CHANCELLOR] and all_cards.count(CHANCELLOR) < n and gain(CHANCELLOR, supply, discard):
            covertool.cover("domsim.py:548:True")
            pass

    elif coins >= COST[SILVER]:
            covertool.cover("domsim.py:549:True")
            gain(SILVER, supply, discard)



covertool.cover("domsim.py:552")
@wrap_attacks
def chancellor_b(deck, discard, hand, turn, supply, f=1.0):
    # Buy 1 Chancellor, shuffle when ratio of coin density in
    # hand / discard pile to coin density in deck is greater than f.
    covertool.cover("domsim.py:556")
    coins = count_coins(hand)
    covertool.cover("domsim.py:557")
    if CHANCELLOR in hand:
        covertool.cover("domsim.py:558")
        coins += 2
        covertool.cover("domsim.py:559")
        if deck:
            covertool.cover("domsim.py:560")
            discard_coins = coins + count_coins(discard)
            covertool.cover("domsim.py:561")
            deck_coins = count_coins(deck)
            covertool.cover("domsim.py:562")
            if COST[GOLD] <= coins < COST[PROVINCE]:
                covertool.cover("domsim.py:563")
                discard_coins += 3
            elif COST[SILVER] <= coins < COST[GOLD]:
                covertool.cover("domsim.py:565")
                discard_coins += 2
            covertool.cover("domsim.py:566")
            discard_p = float(discard_coins) / (len(hand) + len(discard) + 1)
            covertool.cover("domsim.py:567")
            deck_p = float(deck_coins) / len(deck)
            covertool.cover("domsim.py:568")
            if discard_p >= deck_p * f:
                covertool.cover("domsim.py:569")
                discard += deck
                covertool.cover("domsim.py:570")
                del deck[:]
    covertool.cover("domsim.py:571")
    all_cards = deck + discard + hand
    covertool.cover("domsim.py:572")
    provinces = all_cards.count(PROVINCE)
    covertool.cover("domsim.py:573")
    if coins >= COST[PROVINCE] and gain(PROVINCE, supply, discard):
            covertool.cover("domsim.py:573:True")
            pass

    elif BUY_DUCHIES and coins >= COST[DUCHY] and provinces > 3 and gain(DUCHY, supply, discard):
            covertool.cover("domsim.py:574:True")
            pass

    elif BUY_ESTATES and coins >= COST[ESTATE] and provinces > 3 and gain(ESTATE, supply, discard):
            covertool.cover("domsim.py:575:True")
            pass

    elif coins >= COST[GOLD] and gain(GOLD, supply, discard):
            covertool.cover("domsim.py:576:True")
            pass

    elif coins >= COST[CHANCELLOR] and CHANCELLOR not in all_cards and gain(CHANCELLOR, supply, discard):
            covertool.cover("domsim.py:577:True")
            pass

    elif coins >= COST[SILVER]:
            covertool.cover("domsim.py:578:True")
            gain(SILVER, supply, discard)



def chapel(deck, discard, hand, turn, supply, attacks=None):
    # Buy 1 Chapel
    def handle_bureaucrat(deck, discard, hand, turn, supply, attack):
        covertool.cover("domsim.py:584")
        if attack == BUREAUCRAT:
            covertool.cover("domsim.py:585")
            if CHAPEL in hand:
                covertool.cover("domsim.py:586")
                priority = [PROVINCE, DUCHY, ESTATE]
            else:
                covertool.cover("domsim.py:588")
                priority = [ESTATE, DUCHY, PROVINCE]
            covertool.cover("domsim.py:589")
            for card in priority:
                covertool.cover("domsim.py:590")
                if card in hand:
                    covertool.cover("domsim.py:591")
                    move(card, hand, deck)
                    covertool.cover("domsim.py:592")
                    break
            covertool.cover("domsim.py:593")
            return True
    covertool.cover("domsim.py:594")
    if attacks:
        covertool.cover("domsim.py:595")
        handle_attacks(deck, discard, hand, turn, supply, attacks,
                       [handle_bureaucrat, default_attack_handler])
    covertool.cover("domsim.py:597")
    coins = count_coins(hand)
    covertool.cover("domsim.py:598")
    all_cards = deck + discard + hand
    covertool.cover("domsim.py:599")
    provinces = all_cards.count(PROVINCE)
    covertool.cover("domsim.py:600")
    if CHAPEL in hand:
        covertool.cover("domsim.py:601")
        while CURSE in hand:
            covertool.cover("domsim.py:602")
            hand.remove(CURSE)
        covertool.cover("domsim.py:603")
        if provinces <= 3:
            covertool.cover("domsim.py:604")
            while ESTATE in hand:
                covertool.cover("domsim.py:605")
                hand.remove(ESTATE)
        covertool.cover("domsim.py:606")
        coppers = hand.count(COPPER)
        covertool.cover("domsim.py:607")
        all_coins = count_coins(all_cards)
        covertool.cover("domsim.py:608")
        coppers = min(coppers, all_coins - COST[SILVER])
        covertool.cover("domsim.py:609")
        if coins >= COST[PROVINCE]:
            covertool.cover("domsim.py:610")
            coppers = min(coppers, coins - COST[PROVINCE])
        elif BUY_DUCHIES and coins >= COST[DUCHY] and provinces > 3:
            covertool.cover("domsim.py:612")
            coppers = min(coppers, coins - COST[DUCHY])
        elif coins >= COST[GOLD]:
            covertool.cover("domsim.py:614")
            coppers = min(coppers, coins - COST[GOLD])
        covertool.cover("domsim.py:615")
        for i in xrange(coppers):
            covertool.cover("domsim.py:616")
            hand.remove(COPPER)
        covertool.cover("domsim.py:617")
        coins -= coppers
    covertool.cover("domsim.py:618")
    if coins < 5 and CHAPEL not in all_cards and gain(CHAPEL, supply, discard):
            covertool.cover("domsim.py:618:True")
            pass

    elif coins >= COST[PROVINCE] and gain(PROVINCE, supply, discard):
            covertool.cover("domsim.py:619:True")
            pass

    elif BUY_DUCHIES and coins >= COST[DUCHY] and provinces > 3 and gain(DUCHY, supply, discard):
            covertool.cover("domsim.py:620:True")
            pass

    elif BUY_ESTATES and coins >= COST[ESTATE] and provinces > 3 and gain(ESTATE, supply, discard):
            covertool.cover("domsim.py:621:True")
            pass

    elif coins >= COST[GOLD] and gain(GOLD, supply, discard):
            covertool.cover("domsim.py:622:True")
            pass

    elif coins >= COST[SILVER]:
            covertool.cover("domsim.py:623:True")
            gain(SILVER, supply, discard)



covertool.cover("domsim.py:626")
@wrap_attacks
def multi_chapel(deck, discard, hand, turn, supply):
    # Buy 2+ Chapels
    covertool.cover("domsim.py:629")
    coins = count_coins(hand)
    covertool.cover("domsim.py:630")
    all_cards = deck + discard + hand
    covertool.cover("domsim.py:631")
    provinces = all_cards.count(PROVINCES)
    covertool.cover("domsim.py:632")
    if CHAPEL in hand:
        covertool.cover("domsim.py:633")
        for target in [CURSE, ESTATE]:
            covertool.cover("domsim.py:634")
            while target in hand:
                covertool.cover("domsim.py:635")
                hand.remove(target)
        covertool.cover("domsim.py:636")
        if turn > 4:
            covertool.cover("domsim.py:637")
            chapels = hand.count(CHAPEL) - 1
            covertool.cover("domsim.py:638")
            for i in xrange(chapels):
                covertool.cover("domsim.py:639")
                hand.remove(CHAPEL)
        covertool.cover("domsim.py:640")
        coppers = hand.count(COPPER)
        covertool.cover("domsim.py:641")
        all_coins = count_coins(all_cards)
        covertool.cover("domsim.py:642")
        coppers = min(coppers, all_coins - COST[SILVER])
        covertool.cover("domsim.py:643")
        if coins >= COST[PROVINCE]:
            covertool.cover("domsim.py:644")
            coppers = min(coppers, coins - COST[PROVINCE])
        elif coins >= COST[GOLD]:
            covertool.cover("domsim.py:646")
            coppers = min(coppers, coins - COST[GOLD])
        covertool.cover("domsim.py:647")
        for i in xrange(coppers):
            covertool.cover("domsim.py:648")
            hand.remove(COPPER)
        covertool.cover("domsim.py:649")
        coins -= coppers
    covertool.cover("domsim.py:650")
    if turn <= 2 and gain(CHAPEL, supply, discard):
            covertool.cover("domsim.py:650:True")
            pass

    elif coins >= COST[PROVINCE] and gain(PROVINCE, supply, discard):
            covertool.cover("domsim.py:651:True")
            pass

    elif BUY_DUCHIES and coins >= COST[DUCHY] and provinces > 3 and gain(DUCHY, supply, discard):
            covertool.cover("domsim.py:652:True")
            pass

    elif BUY_ESTATES and coins >= COST[ESTATE] and provinces > 3 and gain(ESTATE, supply, discard):
            covertool.cover("domsim.py:653:True")
            pass

    elif coins >= COST[GOLD] and gain(GOLD, supply, discard):
            covertool.cover("domsim.py:654:True")
            pass

    elif turn == 3 and coins >= COST[CHAPEL] and hand.count(CHAPEL) == 2 and gain(CHAPEL, supply, discard):
            covertool.cover("domsim.py:655:True")
            pass

    elif turn == 4 and coins >= COST[CHAPEL] and discard and hand.count(CHAPEL) == 2 and gain(CHAPEL, supply, discard):
            covertool.cover("domsim.py:656:True")
            pass

    elif turn == 4 and coins >= COST[CHAPEL] and discard and hand.count(CHAPEL) == 1 and discard.count(CHAPEL) == 1 and gain(CHAPEL, supply, discard):
            covertool.cover("domsim.py:657:True")
            pass

    elif coins >= COST[SILVER]:
            covertool.cover("domsim.py:658:True")
            gain(SILVER, supply, discard)



covertool.cover("domsim.py:661")
@wrap_attacks
def chapel_lab(deck, discard, hand, turn, supply, labs=2):
    # Buy 1 Chapel, n Laboratories
    covertool.cover("domsim.py:664")
    labs_used = 0
    covertool.cover("domsim.py:665")
    while labs_used < hand.count(LABORATORY):
        covertool.cover("domsim.py:666")
        labs_used += 1
        covertool.cover("domsim.py:667")
        hand += draw(deck, discard, 2)
    covertool.cover("domsim.py:668")
    coins = count_coins(hand)
    covertool.cover("domsim.py:669")
    all_cards = deck + discard + hand
    covertool.cover("domsim.py:670")
    if CHAPEL in hand:
        covertool.cover("domsim.py:671")
        chapeled = 0
        covertool.cover("domsim.py:672")
        for target in [CURSE, ESTATE]:
            covertool.cover("domsim.py:673")
            while chapeled < 4 and target in hand:
                covertool.cover("domsim.py:674")
                chapeled += 1
                covertool.cover("domsim.py:675")
                hand.remove(target)
        covertool.cover("domsim.py:676")
        all_coins = count_coins(all_cards)
        covertool.cover("domsim.py:677")
        coppers = min(hand.count(COPPER), all_coins - COST[SILVER], 4 - chapeled)
        covertool.cover("domsim.py:678")
        if coins >= COST[PROVINCE]:
            covertool.cover("domsim.py:679")
            coppers = min(coppers, coins - COST[PROVINCE])
        elif coins >= COST[GOLD]:
            covertool.cover("domsim.py:681")
            coppers = min(coppers, coins - COST[GOLD])
        elif coins >= COST[LABORATORY] and labs > 0 and LABORATORY not in all_cards:
            covertool.cover("domsim.py:683")
            coppers = min(coppers, coins - COST[LABORATORY])
        covertool.cover("domsim.py:684")
        for i in xrange(coppers):
            covertool.cover("domsim.py:685")
            hand.remove(COPPER)
        covertool.cover("domsim.py:686")
        coins -= coppers
    covertool.cover("domsim.py:687")
    if coins < 5 and CHAPEL not in all_cards and gain(CHAPEL, supply, discard):
            covertool.cover("domsim.py:687:True")
            pass

    elif coins >= COST[PROVINCE] and gain(PROVINCE, supply, discard):
            covertool.cover("domsim.py:688:True")
            pass

    elif BUY_DUCHIES and coins >= COST[DUCHY] and all_cards.count(PROVINCE) > 3 and gain(DUCHY, supply, discard):
            covertool.cover("domsim.py:689:True")
            pass

    elif BUY_ESTATES and coins >= COST[ESTATE] and all_cards.count(PROVINCE) > 3 and gain(ESTATE, supply, discard):
            covertool.cover("domsim.py:690:True")
            pass

    elif coins >= COST[GOLD] and gain(GOLD, supply, discard):
            covertool.cover("domsim.py:691:True")
            pass

    elif coins >= COST[LABORATORY] and all_cards.count(LABORATORY) < labs and gain(LABORATORY, supply, discard):
            covertool.cover("domsim.py:692:True")
            pass

    elif coins >= COST[SILVER]:
            covertool.cover("domsim.py:693:True")
            gain(SILVER, supply, discard)



covertool.cover("domsim.py:696")
@wrap_attacks
def courtyard(deck, discard, hand, turn, supply, n=1):
    # Buy n Courtyards
    covertool.cover("domsim.py:699")
    played = []
    covertool.cover("domsim.py:700")
    courtyards = (deck+discard+hand).count(COURTYARD)
    covertool.cover("domsim.py:701")
    if COURTYARD in hand:
        covertool.cover("domsim.py:702")
        move(COURTYARD, hand, played)
        covertool.cover("domsim.py:703")
        hand += draw(deck, discard, 3)
        covertool.cover("domsim.py:704")
        coins = count_coins(hand)
        covertool.cover("domsim.py:705")
        if COURTYARD in hand:
            covertool.cover("domsim.py:706")
            move(COURTYARD, hand, deck)
        else:
            covertool.cover("domsim.py:708")
            best = (None, -1)
            # Put back the best card for next turn that still lets us make
            # the best possible buy this turn.
            covertool.cover("domsim.py:711")
            for card, delta in [(GOLD, 3), (SILVER, 2), (COPPER, 1),
                                (ESTATE, 0), (PROVINCE, 0), (CURSE, 0)]:
                covertool.cover("domsim.py:713")
                if card in hand:
                    covertool.cover("domsim.py:714")
                    reduced_coins = coins - delta
                    covertool.cover("domsim.py:715")
                    if reduced_coins >= COST[PROVINCE]:
                        covertool.cover("domsim.py:716")
                        value = 4
                    elif reduced_coins >= COST[GOLD]:
                        covertool.cover("domsim.py:718")
                        value = 3
                    elif reduced_coins >= COST[SILVER] and courtyards >= n:
                        covertool.cover("domsim.py:720")
                        value = 2
                    elif reduced_coins >= COST[COURTYARD] and courtyards < n:
                        covertool.cover("domsim.py:722")
                        value = 1
                    else:
                        covertool.cover("domsim.py:724")
                        value = 0
                    covertool.cover("domsim.py:725")
                    if value > best[1]:
                        covertool.cover("domsim.py:726")
                        best = (card, value)
            covertool.cover("domsim.py:727")
            move(best[0], hand, deck)
    covertool.cover("domsim.py:728")
    discard += played
    covertool.cover("domsim.py:729")
    coins = count_coins(hand)
    covertool.cover("domsim.py:730")
    all_cards = deck + discard + hand
    covertool.cover("domsim.py:731")
    provinces = all_cards.count(PROVINCE)
    covertool.cover("domsim.py:732")
    if coins >= COST[PROVINCE] and gain(PROVINCE, supply, discard):
            covertool.cover("domsim.py:732:True")
            pass

    elif BUY_DUCHIES and coins >= COST[DUCHY] and provinces > 3 and gain(DUCHY, supply, discard):
            covertool.cover("domsim.py:733:True")
            pass

    elif BUY_ESTATES and coins >= COST[ESTATE] and provinces > 3 and gain(ESTATE, supply, discard):
            covertool.cover("domsim.py:734:True")
            pass

    elif coins >= COST[GOLD] and gain(GOLD, supply, discard):
            covertool.cover("domsim.py:735:True")
            pass

    elif coins >= COST[COURTYARD] and courtyards < n and gain(COURTYARD, supply, discard):
            covertool.cover("domsim.py:736:True")
            pass

    elif coins >= COST[SILVER]:
            covertool.cover("domsim.py:737:True")
            gain(SILVER, supply, discard)



covertool.cover("domsim.py:740")
@wrap_attacks
def envoy(deck, discard, hand, turn, supply, n=1):
    # Buy n Envoys
    covertool.cover("domsim.py:743")
    if ENVOY in hand:
        covertool.cover("domsim.py:744")
        drawn = draw(deck, discard, 5)
        covertool.cover("domsim.py:745")
        for card in [GOLD, SILVER, COPPER]:
            covertool.cover("domsim.py:746")
            if card in drawn:
                covertool.cover("domsim.py:747")
                move(card, drawn, discard)
                covertool.cover("domsim.py:748")
                break
        covertool.cover("domsim.py:749")
        hand += drawn
    covertool.cover("domsim.py:750")
    coins = count_coins(hand)
    covertool.cover("domsim.py:751")
    all_cards = deck + discard + hand
    covertool.cover("domsim.py:752")
    if coins >= COST[PROVINCE] and gain(PROVINCE, supply, discard):
            covertool.cover("domsim.py:752:True")
            pass

    elif BUY_DUCHIES and coins >= COST[DUCHY] and all_cards.count(PROVINCE) > 3 and gain(DUCHY, supply, discard):
            covertool.cover("domsim.py:753:True")
            pass

    elif BUY_ESTATES and coins >= COST[ESTATE] and all_cards.count(PROVINCE) > 3 and gain(ESTATE, supply, discard):
            covertool.cover("domsim.py:754:True")
            pass

    elif coins >= COST[GOLD] and gain(GOLD, supply, discard):
            covertool.cover("domsim.py:755:True")
            pass

    elif coins >= COST[ENVOY] and all_cards.count(ENVOY) < n and gain(ENVOY, supply, discard):
            covertool.cover("domsim.py:756:True")
            pass

    elif coins >= COST[SILVER]:
            covertool.cover("domsim.py:757:True")
            gain(SILVER, supply, discard)



covertool.cover("domsim.py:760")
@wrap_attacks
def council_room(deck, discard, hand, turn, supply, n=1):
    # Buy n Council Rooms
    covertool.cover("domsim.py:763")
    buys = 1
    covertool.cover("domsim.py:764")
    my_attacks = []
    covertool.cover("domsim.py:765")
    if COUNCIL_ROOM in hand:
        covertool.cover("domsim.py:766")
        hand += draw(deck, discard, 4)
        covertool.cover("domsim.py:767")
        buys += 1
        # Not really an attack, but this is an easy way to handle it.
        covertool.cover("domsim.py:769")
        my_attacks.append(COUNCIL_ROOM)
    covertool.cover("domsim.py:770")
    coins = count_coins(hand)
    covertool.cover("domsim.py:771")
    all_cards = deck + discard + hand
    covertool.cover("domsim.py:772")
    provinces = all_cards.count(PROVINCE)
    covertool.cover("domsim.py:773")
    council_rooms = all_cards.count(COUNCIL_ROOM)
    covertool.cover("domsim.py:774")
    while coins >= COST[SILVER] and buys > 0:
        covertool.cover("domsim.py:775")
        buys -= 1
        covertool.cover("domsim.py:776")
        if coins >= COST[PROVINCE] and gain(PROVINCE, supply, discard):
            covertool.cover("domsim.py:777")
            coins -= COST[PROVINCE]
            covertool.cover("domsim.py:778")
            provinces += 1
        elif BUY_DUCHIES and coins >= COST[DUCHY] and provinces > 3 and gain(DUCHY, supply, discard):
            covertool.cover("domsim.py:780")
            coins -= COST[DUCHY]
        elif BUY_ESTATES and coins >= COST[ESTATE] and provinces > 3 and gain(ESTATE, supply, discard):
            covertool.cover("domsim.py:782")
            coins -= COST[ESTATE]
        elif coins >= COST[GOLD] and gain(GOLD, supply, discard):
            covertool.cover("domsim.py:784")
            coins -= COST[GOLD]
        elif coins >= COST[COUNCIL_ROOM] and council_rooms < n and gain(COUNCIL_ROOM, supply, discard):
            covertool.cover("domsim.py:786")
            coins -= COST[COUNCIL_ROOM]
            covertool.cover("domsim.py:787")
            council_rooms += 1
        elif gain(SILVER, supply, discard):
            covertool.cover("domsim.py:789")
            coins -= COST[SILVER]
    covertool.cover("domsim.py:790")
    return my_attacks


covertool.cover("domsim.py:793")
@wrap_attacks
def laboratory(deck, discard, hand, turn, supply, n=1):
    # Buy n Laboratories
    covertool.cover("domsim.py:796")
    played = []
    covertool.cover("domsim.py:797")
    while LABORATORY in hand:
        covertool.cover("domsim.py:798")
        move(LABORATORY, hand, played)
        covertool.cover("domsim.py:799")
        hand += draw(deck, discard, 2)
    covertool.cover("domsim.py:800")
    discard += played
    covertool.cover("domsim.py:801")
    coins = count_coins(hand)
    covertool.cover("domsim.py:802")
    all_cards = deck + discard + hand
    covertool.cover("domsim.py:803")
    provinces = all_cards.count(PROVINCE)
    covertool.cover("domsim.py:804")
    if coins >= COST[PROVINCE] and gain(PROVINCE, supply, discard):
            covertool.cover("domsim.py:804:True")
            pass

    elif BUY_DUCHIES and coins >= COST[DUCHY] and provinces > 3 and gain(DUCHY, supply, discard):
            covertool.cover("domsim.py:805:True")
            pass

    elif BUY_ESTATES and coins >= COST[ESTATE] and provinces > 3 and gain(ESTATE, supply, discard):
            covertool.cover("domsim.py:806:True")
            pass

    elif coins >= COST[GOLD] and gain(GOLD, supply, discard):
            covertool.cover("domsim.py:807:True")
            pass

    elif coins >= COST[LABORATORY] and all_cards.count(LABORATORY) < n and gain(LABORATORY, supply, discard):
            covertool.cover("domsim.py:808:True")
            pass

    elif coins >= 3:
            covertool.cover("domsim.py:809:True")
            gain(SILVER, supply, discard)



covertool.cover("domsim.py:812")
@wrap_attacks
def market(deck, discard, hand, turn, supply, n=1):
    # Buy n Markets
    covertool.cover("domsim.py:815")
    played = []
    covertool.cover("domsim.py:816")
    while MARKET in hand:
        covertool.cover("domsim.py:817")
        move(MARKET, hand, played)
        covertool.cover("domsim.py:818")
        hand += draw(deck, discard, 1)
    covertool.cover("domsim.py:819")
    coins = count_coins(hand) + len(played)
    covertool.cover("domsim.py:820")
    buys = 1 + len(played)
    covertool.cover("domsim.py:821")
    discard += played
    covertool.cover("domsim.py:822")
    all_cards = deck + discard + hand
    covertool.cover("domsim.py:823")
    provinces = all_cards.count(PROVINCE)
    covertool.cover("domsim.py:824")
    markets = all_cards.count(MARKET)
    covertool.cover("domsim.py:825")
    while coins >= COST[SILVER] and buys > 0:
        covertool.cover("domsim.py:826")
        buys -= 1
        covertool.cover("domsim.py:827")
        if coins >= COST[PROVINCE] and gain(PROVINCE, supply, discard):
            covertool.cover("domsim.py:828")
            coins -= COST[PROVINCE]
            covertool.cover("domsim.py:829")
            provinces += 1
        elif BUY_DUCHIES and coins >= COST[DUCHY] and provinces > 3 and gain(DUCHY, supply, discard):
            covertool.cover("domsim.py:831")
            coins -= COST[DUCHY]
        elif BUY_ESTATES and coins >= COST[ESTATE] and provinces > 3 and gain(ESTATE, supply, discard):
            covertool.cover("domsim.py:833")
            coins -= COST[ESTATE]
        elif coins >= COST[GOLD] and gain(GOLD, supply, discard):
            covertool.cover("domsim.py:835")
            coins -= COST[GOLD]
        elif coins >= COST[MARKET] and markets < n and gain(MARKET, supply, discard):
            covertool.cover("domsim.py:837")
            coins -= COST[MARKET]
            covertool.cover("domsim.py:838")
            markets += 1
        elif gain(SILVER, supply, discard):
            covertool.cover("domsim.py:840")
            coins -= COST[SILVER]


covertool.cover("domsim.py:843")
@wrap_attacks
def militia(deck, discard, hand, turn, supply, n=1):
    # Buy n Militias
    covertool.cover("domsim.py:846")
    my_attacks = []
    covertool.cover("domsim.py:847")
    coins = count_coins(hand)
    covertool.cover("domsim.py:848")
    if MILITIA in hand:
        covertool.cover("domsim.py:849")
        coins += 2
        covertool.cover("domsim.py:850")
        my_attacks.append(MILITIA)
    covertool.cover("domsim.py:851")
    all_cards = deck + discard + hand
    covertool.cover("domsim.py:852")
    provinces = all_cards.count(PROVINCE)
    covertool.cover("domsim.py:853")
    if coins >= COST[PROVINCE] and gain(PROVINCE, supply, discard):
            covertool.cover("domsim.py:853:True")
            pass

    elif BUY_DUCHIES and coins >= COST[DUCHY] and provinces > 3 and gain(DUCHY, supply, discard):
            covertool.cover("domsim.py:854:True")
            pass

    elif BUY_ESTATES and coins >= COST[ESTATE] and provinces > 3 and gain(ESTATE, supply, discard):
            covertool.cover("domsim.py:855:True")
            pass

    elif coins >= COST[GOLD] and gain(GOLD, supply, discard):
            covertool.cover("domsim.py:856:True")
            pass

    elif coins >= COST[MILITIA] and all_cards.count(MILITIA) < n and gain(MILITIA, supply, discard):
            covertool.cover("domsim.py:857:True")
            pass

    elif coins >= COST[SILVER]:
            covertool.cover("domsim.py:858:True")
            gain(SILVER, supply, discard)

    covertool.cover("domsim.py:859")
    return my_attacks


covertool.cover("domsim.py:862")
@wrap_attacks
def mine_copper(deck, discard, hand, turn, supply, n=1):
    # Buy n Mines, prefer upgrading copper
    covertool.cover("domsim.py:865")
    if MINE in hand:
        covertool.cover("domsim.py:866")
        if COPPER in hand:
            covertool.cover("domsim.py:867")
            hand.remove(COPPER)
            covertool.cover("domsim.py:868")
            hand.append(SILVER)
        elif SILVER in hand:
            covertool.cover("domsim.py:870")
            hand.remove(SILVER)
            covertool.cover("domsim.py:871")
            hand.append(GOLD)
    covertool.cover("domsim.py:872")
    all_cards = deck + discard + hand
    covertool.cover("domsim.py:873")
    provinces = all_cards.count(PROVINCE)
    covertool.cover("domsim.py:874")
    coins = count_coins(hand)
    covertool.cover("domsim.py:875")
    if coins >= COST[PROVINCE] and gain(PROVINCE, supply, discard):
            covertool.cover("domsim.py:875:True")
            pass

    elif BUY_DUCHIES and coins >= COST[DUCHY] and provinces > 3 and gain(DUCHY, supply, discard):
            covertool.cover("domsim.py:876:True")
            pass

    elif BUY_ESTATES and coins >= COST[ESTATE] and provinces > 3 and gain(ESTATE, supply, discard):
            covertool.cover("domsim.py:877:True")
            pass

    elif coins >= COST[GOLD] and gain(GOLD, supply, discard):
            covertool.cover("domsim.py:878:True")
            pass

    elif coins >= COST[MINE] and all_cards.count(MINE) < n and gain(MINE, supply, discard):
            covertool.cover("domsim.py:879:True")
            pass

    elif coins >= COST[SILVER]:
            covertool.cover("domsim.py:880:True")
            gain(SILVER, supply, discard)



covertool.cover("domsim.py:883")
@wrap_attacks
def mine_silver(deck, discard, hand, turn, supply, n=1):
    # Buy n Mines, prefer upgrading silver
    covertool.cover("domsim.py:886")
    if MINE in hand:
        covertool.cover("domsim.py:887")
        if SILVER in hand:
            covertool.cover("domsim.py:888")
            hand.remove(SILVER)
            covertool.cover("domsim.py:889")
            hand.append(GOLD)
        elif COPPER in hand:
            covertool.cover("domsim.py:891")
            hand.remove(COPPER)
            covertool.cover("domsim.py:892")
            hand.append(SILVER)
    covertool.cover("domsim.py:893")
    all_cards = deck + discard + hand
    covertool.cover("domsim.py:894")
    provinces = all_cards.count(PROVINCE)
    covertool.cover("domsim.py:895")
    coins = count_coins(hand)
    covertool.cover("domsim.py:896")
    if coins >= COST[PROVINCE] and gain(PROVINCE, supply, discard):
            covertool.cover("domsim.py:896:True")
            pass

    elif BUY_DUCHIES and coins >= COST[DUCHY] and provinces > 3 and gain(DUCHY, supply, discard):
            covertool.cover("domsim.py:897:True")
            pass

    elif BUY_ESTATES and coins >= COST[ESTATE] and provinces > 3 and gain(ESTATE, supply, discard):
            covertool.cover("domsim.py:898:True")
            pass

    elif coins >= COST[GOLD] and gain(GOLD, supply, discard):
            covertool.cover("domsim.py:899:True")
            pass

    elif coins >= COST[MINE] and all_cards.count(MINE) < n and gain(MINE, supply, discard):
            covertool.cover("domsim.py:900:True")
            pass

    elif coins >= COST[SILVER]:
            covertool.cover("domsim.py:901:True")
            gain(SILVER, supply, discard)



covertool.cover("domsim.py:904")
@wrap_attacks
def minion(deck, discard, hand, turn, supply):
    covertool.cover("domsim.py:906")
    my_attacks = []
    covertool.cover("domsim.py:907")
    coins = count_coins(hand)
    covertool.cover("domsim.py:908")
    bonus_coins = 0
    covertool.cover("domsim.py:909")
    played = []
    covertool.cover("domsim.py:910")
    while MINION in hand:
        covertool.cover("domsim.py:911")
        move(MINION, hand, played)
        covertool.cover("domsim.py:912")
        if MINION in hand or (coins + bonus_coins + 2) >= COST[PROVINCE]:
            covertool.cover("domsim.py:913")
            bonus_coins += 2
        else:
            covertool.cover("domsim.py:915")
            discard += hand
            covertool.cover("domsim.py:916")
            hand[:] = draw(deck, discard, 4)
            covertool.cover("domsim.py:917")
            coins = count_coins(hand)
            covertool.cover("domsim.py:918")
            my_attacks.append(MINION)
    covertool.cover("domsim.py:919")
    discard += played
    covertool.cover("domsim.py:920")
    coins = coins + bonus_coins
    covertool.cover("domsim.py:921")
    all_cards = deck + discard + hand
    covertool.cover("domsim.py:922")
    provinces = all_cards.count(PROVINCE)
    covertool.cover("domsim.py:923")
    if coins >= COST[PROVINCE] and gain(PROVINCE, supply, discard):
            covertool.cover("domsim.py:923:True")
            pass

    elif BUY_DUCHIES and coins >= COST[DUCHY] and provinces > 3 and gain(DUCHY, supply, discard):
            covertool.cover("domsim.py:924:True")
            pass

    elif BUY_ESTATES and coins >= COST[ESTATE] and provinces > 3 and gain(ESTATE, supply, discard):
            covertool.cover("domsim.py:925:True")
            pass

    elif coins >= COST[GOLD] and gain(GOLD, supply, discard):
            covertool.cover("domsim.py:926:True")
            pass

    elif coins >= COST[MINION] and gain(MINION, supply, discard):
            covertool.cover("domsim.py:927:True")
            pass

    elif coins >= COST[SILVER]:
            covertool.cover("domsim.py:928:True")
            gain(SILVER, supply, discard)

    covertool.cover("domsim.py:929")
    return my_attacks


covertool.cover("domsim.py:932")
@wrap_attacks
def moat(deck, discard, hand, turn, supply, n=1):
    # Buy n Moats
    covertool.cover("domsim.py:935")
    if MOAT in hand:
        covertool.cover("domsim.py:936")
        hand += draw(deck, discard, 2)
    covertool.cover("domsim.py:937")
    coins = count_coins(hand)
    covertool.cover("domsim.py:938")
    all_cards = deck + discard + hand
    covertool.cover("domsim.py:939")
    provinces = all_cards.count(PROVINCE)
    covertool.cover("domsim.py:940")
    if coins >= COST[PROVINCE] and gain(PROVINCE, supply, discard):
            covertool.cover("domsim.py:940:True")
            pass

    elif BUY_DUCHIES and coins >= COST[DUCHY] and provinces > 3 and gain(DUCHY, supply, discard):
            covertool.cover("domsim.py:941:True")
            pass

    elif BUY_ESTATES and coins >= COST[ESTATE] and provinces > 3 and gain(ESTATE, supply, discard):
            covertool.cover("domsim.py:942:True")
            pass

    elif coins >= COST[GOLD] and gain(GOLD, supply, discard):
            covertool.cover("domsim.py:943:True")
            pass

    elif coins >= COST[MOAT] and all_cards.count(MOAT) < n and gain(MOAT, supply, discard):
            covertool.cover("domsim.py:944:True")
            pass

    elif coins >= COST[SILVER]:
            covertool.cover("domsim.py:945:True")
            gain(SILVER, supply, discard)



covertool.cover("domsim.py:948")
@wrap_attacks
def smithy(deck, discard, hand, turn, supply, n=1):
    # Buy n Smithies
    covertool.cover("domsim.py:951")
    if SMITHY in hand:
        covertool.cover("domsim.py:952")
        hand += draw(deck, discard, 3)
    covertool.cover("domsim.py:953")
    coins = count_coins(hand)
    covertool.cover("domsim.py:954")
    all_cards = deck + discard + hand
    covertool.cover("domsim.py:955")
    provinces = all_cards.count(PROVINCE)
    covertool.cover("domsim.py:956")
    smithies = all_cards.count(SMITHY)
    covertool.cover("domsim.py:957")
    if coins >= COST[PROVINCE] and gain(PROVINCE, supply, discard):
            covertool.cover("domsim.py:957:True")
            pass

    elif BUY_DUCHIES and coins >= COST[DUCHY] and provinces > 3 and gain(DUCHY, supply, discard):
            covertool.cover("domsim.py:958:True")
            pass

    elif BUY_ESTATES and coins >= COST[ESTATE] and provinces > 3 and gain(ESTATE, supply, discard):
            covertool.cover("domsim.py:959:True")
            pass

    elif coins >= COST[GOLD] and gain(GOLD, supply, discard):
            covertool.cover("domsim.py:960:True")
            pass

    elif coins >= COST[SMITHY] and all_cards.count(SMITHY) < n and gain(SMITHY, supply, discard):
            covertool.cover("domsim.py:961:True")
            pass

    elif coins >= COST[SILVER]:
            covertool.cover("domsim.py:962:True")
            gain(SILVER, supply, discard)



def wharf(deck, discard, hand, turn, supply, n=1, attacks=None):
    # Buy n Wharfs
    covertool.cover("domsim.py:967")
    buys = 1
    covertool.cover("domsim.py:968")
    durations = []
    covertool.cover("domsim.py:969")
    if "Wharf 1" in hand:
        covertool.cover("domsim.py:970")
        durations.append(WHARF)
        covertool.cover("domsim.py:971")
        hand.remove("Wharf 1")
        covertool.cover("domsim.py:972")
        hand += draw(deck, discard, 3)
        covertool.cover("domsim.py:973")
        buys += 1
    covertool.cover("domsim.py:974")
    if attacks:
        covertool.cover("domsim.py:975")
        handle_attacks(deck, discard, hand, turn, supply, attacks)
    covertool.cover("domsim.py:976")
    if WHARF in hand:
        covertool.cover("domsim.py:977")
        hand.remove(WHARF)
        covertool.cover("domsim.py:978")
        hand += draw(deck, discard, 2)
        covertool.cover("domsim.py:979")
        buys += 1
        covertool.cover("domsim.py:980")
        deck.append("Wharf 1")  # Wharf duration placeholder
    covertool.cover("domsim.py:981")
    coins = count_coins(hand)
    covertool.cover("domsim.py:982")
    all_cards = deck + discard + hand
    covertool.cover("domsim.py:983")
    provinces = all_cards.count(PROVINCE)
    covertool.cover("domsim.py:984")
    wharves = all_cards.count(WHARF)
    covertool.cover("domsim.py:985")
    while buys > 0:
        covertool.cover("domsim.py:986")
        buys -= 1
        covertool.cover("domsim.py:987")
        if coins >= COST[PROVINCE] and gain(PROVINCE, supply, discard):
            covertool.cover("domsim.py:988")
            coins -= COST[PROVINCE]
            covertool.cover("domsim.py:989")
            provinces += 1
        elif BUY_DUCHIES and coins >= COST[DUCHY] and provinces > 3 and gain(DUCHY, supply, discard):
            covertool.cover("domsim.py:991")
            coins -= COST[DUCHY]
        elif BUY_ESTATES and coins >= COST[ESTATE] and provinces > 3 and gain(ESTATE, supply, discard):
            covertool.cover("domsim.py:993")
            coins -= COST[ESTATE]
        elif coins >= COST[GOLD] and gain(GOLD, supply, discard):
            covertool.cover("domsim.py:995")
            coins -= COST[GOLD]
        elif coins >= COST[WHARF] and wharves < n and gain(WHARF, supply, discard):
            covertool.cover("domsim.py:997")
            coins -= COST[WHARF]
            covertool.cover("domsim.py:998")
            wharves += 1
        elif coins >= COST[SILVER] and gain(SILVER, supply, discard):
            covertool.cover("domsim.py:1000")
            coins -= COST[SILVER]
        else:
            covertool.cover("domsim.py:1002")
            break


covertool.cover("domsim.py:1005")
@wrap_attacks
def witch(deck, discard, hand, turn, supply, n=1):
    # Buy n Witches
    covertool.cover("domsim.py:1008")
    my_attacks = []
    covertool.cover("domsim.py:1009")
    if WITCH in hand:
        covertool.cover("domsim.py:1010")
        hand += draw(deck, discard, 2)
        covertool.cover("domsim.py:1011")
        my_attacks.append(WITCH)
    covertool.cover("domsim.py:1012")
    coins = count_coins(hand)
    covertool.cover("domsim.py:1013")
    all_cards = deck + discard + hand
    covertool.cover("domsim.py:1014")
    provinces = all_cards.count(PROVINCE)
    covertool.cover("domsim.py:1015")
    if coins >= COST[PROVINCE] and gain(PROVINCE, supply, discard):
            covertool.cover("domsim.py:1015:True")
            pass

    elif BUY_DUCHIES and coins >= COST[DUCHY] and provinces > 3 and gain(DUCHY, supply, discard):
            covertool.cover("domsim.py:1016:True")
            pass

    elif BUY_ESTATES and coins >= COST[ESTATE] and provinces > 3 and gain(ESTATE, supply, discard):
            covertool.cover("domsim.py:1017:True")
            pass

    elif coins >= COST[GOLD] and gain(GOLD, supply, discard):
            covertool.cover("domsim.py:1018:True")
            pass

    elif coins >= COST[WITCH] and all_cards.count(WITCH) < n and gain(WITCH, supply, discard):
            covertool.cover("domsim.py:1019:True")
            pass

    elif coins >= COST[SILVER]:
            covertool.cover("domsim.py:1020:True")
            gain(SILVER, supply, discard)

    covertool.cover("domsim.py:1021")
    return my_attacks


covertool.cover("domsim.py:1024")
@wrap_attacks
def big_money(deck, discard, hand, turn, supply):
    # Buy no kingdom cards at all
    covertool.cover("domsim.py:1027")
    coins = count_coins(hand)
    covertool.cover("domsim.py:1028")
    all_cards = deck + discard + hand
    covertool.cover("domsim.py:1029")
    provinces = all_cards.count(PROVINCE)
    covertool.cover("domsim.py:1030")
    if coins >= COST[PROVINCE] and gain(PROVINCE, supply, discard):
            covertool.cover("domsim.py:1030:True")
            pass

    elif BUY_DUCHIES and coins >= COST[DUCHY] and provinces > 3 and gain(DUCHY, supply, discard):
            covertool.cover("domsim.py:1031:True")
            pass

    elif BUY_ESTATES and coins >= COST[ESTATE] and provinces > 3 and gain(ESTATE, supply, discard):
            covertool.cover("domsim.py:1032:True")
            pass

    elif coins >= COST[GOLD] and gain(GOLD, supply, discard):
            covertool.cover("domsim.py:1033:True")
            pass

    elif coins >= COST[SILVER]:
            covertool.cover("domsim.py:1034:True")
            gain(SILVER, supply, discard)



covertool.cover("domsim.py:1037")
@wrap_attacks
def early_gold(deck, discard, hand, turn, supply, g=0):
    # Test buying a gold when drawing 8+ coins after buying only g gold.
    covertool.cover("domsim.py:1040")
    if SMITHY in hand:
        covertool.cover("domsim.py:1041")
        hand += draw(deck, discard, 3)
    covertool.cover("domsim.py:1042")
    coins = count_coins(hand)
    covertool.cover("domsim.py:1043")
    all_cards = (deck + discard + hand)
    covertool.cover("domsim.py:1044")
    if coins >= COST[GOLD] and all_cards.count(GOLD) < g and gain(GOLD, supply, discard):
            covertool.cover("domsim.py:1044:True")
            pass

    elif coins >= COST[PROVINCE] and all_cards.count(GOLD) == g and gain(GOLD, supply, discard):
            covertool.cover("domsim.py:1045:True")
            pass

    elif coins >= COST[PROVINCE] and gain(PROVINCE, supply, discard):
            covertool.cover("domsim.py:1046:True")
            pass

    elif coins >= COST[GOLD] and all_cards.count(GOLD) == g:
        covertool.cover("domsim.py:1048")
        raise InvalidGameError
    elif coins >= COST[GOLD] and gain(GOLD, supply, discard):
            covertool.cover("domsim.py:1049:True")
            pass

    elif coins >= COST[SMITHY] and SMITHY not in all_cards and gain(SMITHY, supply, discard):
            covertool.cover("domsim.py:1050:True")
            pass

    elif coins >= COST[SILVER]:
            covertool.cover("domsim.py:1051:True")
            gain(SILVER, supply, discard)



covertool.cover("domsim.py:1054")
@wrap_attacks
def early_province(deck, discard, hand, turn, supply, g=0):
    # Test buying a province when drawing 8+ coins after buying only g gold.
    covertool.cover("domsim.py:1057")
    if SMITHY in hand:
        covertool.cover("domsim.py:1058")
        hand += draw(deck, discard, 3)
    covertool.cover("domsim.py:1059")
    coins = count_coins(hand)
    covertool.cover("domsim.py:1060")
    all_cards = (deck + discard + hand)
    covertool.cover("domsim.py:1061")
    if coins >= COST[GOLD] and all_cards.count(GOLD) < g and gain(GOLD, supply, discard):
            covertool.cover("domsim.py:1061:True")
            pass

    elif coins >= COST[PROVINCE] and gain(PROVINCE, supply, discard):
            covertool.cover("domsim.py:1062:True")
            pass

    elif coins >= COST[GOLD] and PROVINCE not in all_cards:
        covertool.cover("domsim.py:1064")
        raise InvalidGameError
    elif coins >= COST[GOLD] and gain(GOLD, supply, discard):
            covertool.cover("domsim.py:1065:True")
            pass

    elif coins >= COST[SMITHY] and SMITHY not in all_cards and gain(SMITHY, supply, discard):
            covertool.cover("domsim.py:1066:True")
            pass

    elif coins >= COST[SILVER]:
            covertool.cover("domsim.py:1067:True")
            gain(SILVER, supply, discard)



covertool.cover("domsim.py:1070")
@wrap_attacks
def turn3_gold(deck, discard, hand, turn, supply):
    # Test buying a gold when drawing 8+ coins on turn 3.
    covertool.cover("domsim.py:1073")
    coins = count_coins(hand)
    covertool.cover("domsim.py:1074")
    if BARON in hand and ESTATE in hand:
        covertool.cover("domsim.py:1075")
        move(ESTATE, hand, discard)
        covertool.cover("domsim.py:1076")
        coins += 4
    covertool.cover("domsim.py:1077")
    all_cards = (deck + discard + hand)
    covertool.cover("domsim.py:1078")
    if coins >= COST[PROVINCE] and GOLD not in all_cards and gain(GOLD, supply, discard):
            covertool.cover("domsim.py:1078:True")
            pass

    elif coins >= COST[PROVINCE] and gain(PROVINCE, supply, discard):
            covertool.cover("domsim.py:1079:True")
            pass

    elif turn == 3:
        covertool.cover("domsim.py:1081")
        raise InvalidGameError
    elif coins >= COST[GOLD] and gain(GOLD, supply, discard):
            covertool.cover("domsim.py:1082:True")
            pass

    elif coins >= COST[BARON] and BARON not in all_cards and gain(BARON, supply, discard):
            covertool.cover("domsim.py:1083:True")
            pass

    elif coins >= COST[SILVER]:
            covertool.cover("domsim.py:1084:True")
            gain(SILVER, supply, discard)



covertool.cover("domsim.py:1087")
@wrap_attacks
def super_early_province(deck, discard, hand, turn, supply):
    # Test buying a province when drawing 8+ coins on turn 3.
    covertool.cover("domsim.py:1090")
    coins = count_coins(hand)
    covertool.cover("domsim.py:1091")
    if BARON in hand and ESTATE in hand:
        covertool.cover("domsim.py:1092")
        move(ESTATE, hand, discard)
        covertool.cover("domsim.py:1093")
        coins += 4
    covertool.cover("domsim.py:1094")
    all_cards = (deck + discard + hand)
    covertool.cover("domsim.py:1095")
    if coins >= COST[PROVINCE] and gain(PROVINCE, supply, discard):
            covertool.cover("domsim.py:1095:True")
            pass

    elif turn == 3:
        covertool.cover("domsim.py:1097")
        raise InvalidGameError
    elif coins >= COST[GOLD] and gain(GOLD, supply, discard):
            covertool.cover("domsim.py:1098:True")
            pass

    elif coins >= COST[BARON] and BARON not in all_cards and gain(BARON, supply, discard):
            covertool.cover("domsim.py:1099:True")
            pass

    elif coins >= COST[SILVER]:
            covertool.cover("domsim.py:1100:True")
            gain(SILVER, supply, discard)



covertool.cover("domsim.py:1103")
if __name__ == "__main__":
    covertool.cover("domsim.py:1104")
    main()
