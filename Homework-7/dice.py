"""File: dice.py
Author: John Choi choi.1655@osu.edu
Version: February 28, 2022

The Ohio State University CSE4256 SP22 Homework 7.
"""

"""Simple pseudorandom number generator."""
def mcg(s=543718):
    import random

    while True:
        x = random.randint(0, s)
        yield x

"""Simulates rolling a `sides`-sided die `samples` times, and prints the results.

Args:
  sides: number of sides on the die to simulate
  samples: number of rolls to simulate
"""
def diceroller(sides=6, samples=10000):
    raise NotImplementedError()
    die = (n % sides + 1 for n in mcg())
    counts = dict()
    for i in range(samples):
        roll = next(die)
        if roll not in counts:
            counts[roll] = 0
        counts[roll] += 1

    # TODO Modify the output of this function so that it displays a "pretty" horizontal bar chart.
    #   Hint: use the Unicode character FULL BLOCK (U+2588) (in Python: u"\u2588").
    for value in range(1, sides + 1):
        print(f"{value}: {counts[value]}")

