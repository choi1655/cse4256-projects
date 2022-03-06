"""File: dice.py
Author: John Choi choi.1655@osu.edu
Version: March 4, 2022

The Ohio State University CSE4256 SP22 Homework 7.
"""

import random

"""Simple pseudorandom number generator."""
def mcg(s=543718):
    while True:
        x = random.randint(0, s)
        yield x

"""Simulates rolling a `sides`-sided die `samples` times, and prints the results.

Args:
  sides: number of sides on the die to simulate
  samples: number of rolls to simulate
"""
def diceroller(sides=6, samples=10000):
    die = (n % sides + 1 for n in mcg())
    counts = dict()
    for i in range(samples):
        roll = next(die)
        if roll not in counts:
            counts[roll] = 0
        counts[roll] += 1
    return counts

"""Takes an input as a dictionary returned by diceroller() and prints to the console a horizontal
bar chart made of unicode characters.
TODO: normalize the bar charts so that it doesn't go over 80 characters
"""
def print_bar_chart(data: dict):
    bar_char = '\u2588'
    buffer = []
    for key, value in data.items():
        bar_chart = bar_char * value
        buffer.append((key, bar_chart))
    # sort buffer
    buffer.sort()
    # print
    for (key, chart) in buffer:
        print(f'{key} {chart}')
