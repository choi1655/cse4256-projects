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

    # TODO: Implement this method

def riffle_shuffle(deck: deque) -> None:
    """Simulates a 'riffle shuffle' of a deck of cards."""

    # TODO: Implement this method

def mix_deck(deck: deque) -> None:
    """Puts deck in a random order."""

    # TODO: Implement this method

def deal(deck: deque, n_players: int) -> list:
    """Deals the cards n_players ways."""

    # TODO: Implement this method

def letter_freq(s: str) -> Counter:
    """Counts the number of times each letter appears in `s`."""

    # TODO: Implement this method

def popular_letter(s: str) -> str:
    """Returns the letter in `s` that appears most often."""

    # TODO: Implement this method
