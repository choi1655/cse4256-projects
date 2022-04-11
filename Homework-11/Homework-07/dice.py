"""File: dice.py
Author: John Choi choi.1655@osu.edu
Version: March 4, 2022

The Ohio State University CSE4256 SP22 Homework 7.
"""

import random

def mcg(number=543718):
    """Simple pseudorandom number generator."""
    while True:
        random_number = random.randint(0, number)
        yield random_number

def diceroller(sides=6, samples=10000):
    """Simulates rolling a `sides`-sided die `samples` times, and prints the results.

    Args:
    sides: number of sides on the die to simulate
    samples: number of rolls to simulate
    """
    die = (n % sides + 1 for n in mcg())
    counts = {}
    for _ in range(samples):
        roll = next(die)
        if roll not in counts:
            counts[roll] = 0
        counts[roll] += 1
    return counts

def print_bar_chart(data: dict):
    """Takes an input as a dictionary returned by diceroller() and prints to the console a
    horizontal bar chart made of unicode characters.
    """
    max_length = 80 - 2 # minus 2 for label and space
    for length in data.values():
        max_length = max(length, max_length)
    # if max_length is over 80, normalize
    new_data = dict(data.items())
    if max_length > 80 - 2:
        new_data = {}
        for label, bar_length in data.items():
            # normalize bar_length
            bar_length = bar_length * 78 // max_length
            new_data[label] = bar_length
    bar_char = '\u2588'
    buffer = []
    for key, value in new_data.items():
        bar_chart = bar_char * value
        buffer.append((key, bar_chart))
    # sort buffer
    buffer.sort()
    # print
    for (key, chart) in buffer:
        print(f'{key} {chart}')
