"""File: cards.py
Author: John Choi choi.1655@osu.edu
Version: April 3, 2022

The Ohio State University CSE4256 SP22 Homework 9.
"""

from collections import deque, namedtuple
import csv
from enum import Enum, auto
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
    # The strength of ACE is 1 and the strength of KING is 13

    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13

Card = namedtuple("Card", ["rank", "suit"])

def card_str(card: Card):
    """Returns a string representing the rank and suit of a playing card."""

    return f"{card.rank.name}{card.suit.symbol}"

def std_card_deck() -> deque:
    """Returns a deque containing 52 Cards, the standard 52 playing cards."""

    deck = []
    suits = [Suit.CLUBS, Suit.SPADES, Suit.HEARTS, Suit.DIAMONDS]
    ranks = [Rank.ACE, Rank.TWO, Rank.THREE, Rank.FOUR, Rank.FIVE, Rank.SIX, Rank.SEVEN, Rank.EIGHT, Rank.NINE, Rank.TEN, Rank.JACK, Rank.QUEEN, Rank.KING]
    for suit in suits:
        for rank in ranks:
            deck.append(Card(rank, suit))
    return deque(deck)

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
    deck = std_card_deck()
    # 1. Shuffle the deck well
    mix_deck(deck)
    # 2. Deal the deck into n_players hands
    decks = deal(deck, n_players)
    # 3. Open outfile and point a csv writer to it
    with open(outfile, 'w', newline='') as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(['player', 'rank', 'suit'])
        scores = [0 for _ in range(n_players)]
        # 4. While all hands are non-empty, play the game.
        while not decks_are_empty(decks):
            winner = None
            winner_id = None
            for i in range(n_players):
                # skip if deck is empty
                if not decks[i]:
                    continue
                player = i
                card = decks[i].pop()
                rank_name = card.rank.name
                suit_name = card.suit.name
                csvwriter.writerow([player, rank_name, suit_name])

                if winner:
                    winner_score = int(10 * int(winner.suit.value[0]) + int(winner.rank.value))
                    card_score = int(10 * int(card.suit.value[0]) + int(card.rank.value))
                    if card_score > winner_score:
                        winner = card
                        winner_id = i
                else:
                    winner = card
                    winner_id = i
            # 5. Print and record every card played in the round, and determine a round winner
            csvwriter.writerow(['Winner', card_str(winner)])
            scores[winner_id] += 1

        # 6. Print a summary of the game: the winner's id and all players' scores
        csvwriter.writerow(['------------ Game Summary ------------'])
        max_id = 0
        for i in range(1, len(scores)):
            if scores[i] > scores[max_id]:
                max_id = i
        winner_summary = ['Overall Winner ID and Score', max_id, scores[max_id]]
        csvwriter.writerow(winner_summary)
        for i in range(len(scores)):
            csvwriter.writerow(['Player ID and Score', i, scores[i]])
