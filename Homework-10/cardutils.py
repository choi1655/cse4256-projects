from collections import deque, namedtuple
from enum import Enum
from random import choice

class Suit(Enum):
    """Enum of the suits of the standard playing cards.

    Each member has two fields: strength and symbol. The strength of a suit defines how it compares
    with other suits; a higher strength will beat a lower strength.
    """

    CLUBS    = (1, '♣')
    DIAMONDS = (2, '♦')
    HEARTS   = (3, '♥')
    SPADES   = (4, '♠')

    def __init__(self, strength, symbol) -> None:
        super().__init__()
        self.strength = strength
        self.symbol = symbol

class Rank(Enum):
    """Enum of the ranks of the standard playing cards.

    Each member has two fields: strength and symbol. The strength of a rank defines how it compares
    to other ranks; a higher strength will beat a lower strength.
    """

    # TODO: Using Suit as a guide, implement an Enum for the card ranks.
    # The strength of ACE is 1 and the strength of KING is 13
    ACE   = (1, 'A')
    TWO   = (2, '2')
    THREE = (3, '3')
    FOUR  = (4, '4')
    FIVE  = (5, '5')
    SIX   = (6, '6')
    SEVEN = (7, '7')
    EIGHT = (8, '8')
    NINE  = (9, '9')
    TEN   = (10, '10')
    JACK  = (11, 'J')
    QUEEN = (12, 'Q')
    KING  = (13, 'K')

    def __init__(self, strength, symbol) -> None:
        super().__init__()
        self.strength = strength
        self.symbol = symbol

Card = namedtuple("Card", ["rank", "suit"])

def card_str(card: Card):
    """Returns a string representing the rank and suit of a playing card."""

    return f"{card.rank.symbol:>2}{card.suit.symbol}"

def std_card_deck() -> deque:
    """Returns a deque containing 52 Cards, the standard 52 playing cards."""

    deck = deque()
    for suit in Suit:
        for rank in Rank:
            deck.append(Card(rank, suit))

    return deck

def riffle_shuffle(deck: deque) -> None:
    """Simulates a 'riffle shuffle' of a deck of cards."""

    deck1, deck2 = deque(), deque()

    while len(deck1) < len(deck):
        deck1.append(deck.popleft())

    while 0 < len(deck):
        deck2.append(deck.popleft())

    while len(deck1) > 0 and len(deck2) > 0:
        semi_deck = choice((deck1, deck2))
        deck.append(semi_deck.popleft())

    deck.extend(deck1)
    deck.extend(deck2)

def mix_deck(deck: deque) -> None:
    """Puts deck in a random order."""

    for _ in range(7):
        riffle_shuffle(deck)

def deal(deck: deque, n_players: int) -> list[list]:
    """Deals the cards n_players ways."""

    hands = [[] for _ in range(n_players)]
    hand_no = 0
    while len(deck) > 0:
        hands[hand_no].append(deck.pop())
        hand_no = (hand_no + 1) % n_players

    return hands
