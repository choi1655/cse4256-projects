"""File: main.py
Author: John Choi choi.1655@osu.edu
Version: March 21, 2022

The Ohio State University CSE4256 SP22 Homework 8.
"""

from collections import namedtuple, deque, Counter
from random import random
from typing import Any, Sequence

def uniform(a: float, b: float) -> float:
    """Returns a uniformly-distributed real number in the interval [a, b)."""

    return a + ((b - a) * random())

def randrange(start: int, stop: int) -> int:
    """Returns a uniformly distributed integer in the interval [start, stop)."""

    return int(uniform(start, stop))

def choice(seq: Sequence) -> Any:
    """Returns a randomly-chosen element of `seq`."""

    return seq[randrange(0, len(seq))]

# Define the type Card as a named tuple.
Card = namedtuple('Card', ['suit', 'rank'])

def std_card_deck() -> deque:
    """Returns a deque containing 52 Cards, the standard 52 playing cards."""

    deck = []
    suits = ['Clubs', 'Spades', 'Hearts', 'Diamonds']
    for suit in suits:
        for i in range(1, 14):
            deck.append(Card(suit, i))
    return deque(deck)

def riffle_shuffle(deck: deque) -> None:
    """Simulates a 'riffle shuffle' of a deck of cards."""

    d1 = deque()
    d2 = deque()
    # split the deck into d1 and d2, of nearly equal lengths, leaving deck empty
    while len(deck) != 0:
        d1.append(deck.popleft())
        if len(deck) != 0:
            d2.append(deck.pop())
    assert(len(deck) == 0)

    # as long as there are cards in both decks,
    # choose the bottom card from either d1 or d2, at random,
    # and place it at the top of deck
    while len(d1) > 0 or len(d2) > 0:
        rand_num = randrange(0, 2)
        card = None
        if rand_num == 0:
            # choose from d1 only if d1 has something. else, choose from d2
            card = d1.popleft() if len(d1) > 0 else d2.popleft()
        else:
            # choose from d2 only if d2 has something. else, choose from d1
            card = d2.popleft() if len(d2) > 0 else d1.popleft()
        deck.append(card)


def mix_deck(deck: deque) -> None:
    """Puts deck in a random order."""

    temp_deck = deque()
    # move everything from deck to temp_deck
    for _ in range(len(deck)):
        temp_deck.appendleft(deck.pop())
    assert(len(deck) == 0) # make sure deck is empty
    for _ in range(len(temp_deck)):
        random_num = randrange(0, 100)
        if random_num < 50:
            deck.append(temp_deck.pop())
        else:
            deck.appendleft(temp_deck.pop())
    assert(len(deck) != 0 and len(temp_deck) == 0)


def deal(deck: deque, n_players: int) -> list:
    """Deals the cards n_players ways."""

    # TODO: Implement this method

def letter_freq(s: str) -> Counter:
    """Counts the number of times each letter appears in `s`."""

    # TODO: Implement this method

def popular_letter(s: str) -> str:
    """Returns the letter in `s` that appears most often."""

    # TODO: Implement this method
