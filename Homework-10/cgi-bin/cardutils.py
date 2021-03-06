"""File: cardutils.py
Author: John Choi choi.1655@osu.edu
Version: April 10, 2022

The Ohio State University CSE4256 SP22 Homework 10.
"""

from collections import deque, namedtuple
from enum import Enum
from random import choice
import csv

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

def deal(deck: deque, n_players: int):
    """Deals the cards n_players ways."""

    hands = [[] for _ in range(n_players)]
    hand_no = 0
    while len(deck) > 0:
        hands[hand_no].append(deck.pop())
        hand_no = (hand_no + 1) % n_players

    return hands

def play_game(deck: deque, n_players: int, outfile: str):
    """Simulates a simple card game being played by the computer, recording the moves in outfile.

    The rules of the game are as follows:
        - Each round, all players play the card at the top of their hand
        - The player who played the card with the highest rank gets a point
            - If there are multiple cards with the same rank, then suits are taken in reverse
              alphabetical order, with SPADES as the highest suit, then HEARTS, then DIAMONDS,
              then CLUBS. The player with the highest suit (among tied-rank cards) gets a point
        - Once any player's hand is empty, the game is over and the player with the most points
          is declared the winner.

    This function should do the following:
        - Shuffle the deck well
        - Deal the deck into n_players hands (the players have ids 0, 1, 2, ..., n_players - 1)
        - Open a csv file called outfile to which the game will be written
        - Play the game, each round doing the following:
            - Print the cards that were played by each player in this round, as well as the current
              scores of all players and which player won the round
            - Append the round to outfile as a series of rows with one row per card played, keeping
              track of the following:
                - The id of the player who played the card
                - The name of the card Rank (one of "ACE", "TWO", "THREE", "FOUR", "FIVE", etc.)
                - The name of the card Suit (one of "CLUBS", "SPADES", "HEARTS", "DIAMONDS")
        - After the game is over, print the following information about the game:
            - The id of the winning player
            - The scores of all players

    The generated csv file should have the following format:
        - The first row should contain the field names, which are:
            - "player"
            - "rank""
            - "suit"
        - Each subsequent row should contain, in order:
            - The id of the player
            - The name of the rank of the card they played
            - The name of the suit of the card they played
    """
    def decks_are_empty(decks) -> bool:
        for deck in decks:
            if deck:
                return False
        return True

    # Implement this function
    # 1. Shuffle the deck well
    mix_deck(deck)
    # 2. Deal the deck into n_players hands
    decks = deal(deck, n_players)
    # 3. Open outfile and point a csv writer to it
    with open(outfile, 'w', newline='') as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(['player', 'rank', 'suit'])
        # 4. While all hands are non-empty, play the game.
        while not decks_are_empty(decks):
            for i in range(n_players):
                # skip if deck is empty
                if not decks[i]:
                    continue
                player = i
                card = decks[i].pop()
                rank_name = card.rank.name
                suit_name = card.suit.name
                csvwriter.writerow([player, rank_name, suit_name])
