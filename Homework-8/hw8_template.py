from collections import namedtuple, deque, Counter
from random import random
from typing import Any, Sequence

def uniform(a: float, b: float) -> float:
    """Returns a uniformly-distributed real number in the interval [a, b)."""

    # TODO: Implement this method

def randrange(start: int, stop: int) -> int:
    """Returns a uniformly distributed integer in the interval [start, stop)."""

    # TODO: Implement this method

def choice(seq: Sequence) -> Any:
    """Returns a randomly-chosen element of `seq`."""

    # TODO: Implement this method

# TODO: Define the type Card as a named tuple.
Card = None

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
