"""File: tests.py
Author: John Choi choi.1655@osu.edu
Version: February 28, 2022

The Ohio State University CSE4256 SP22 Homework 7.
Contains the unittest test cases.
"""

import unittest
import dice

class WordTests(unittest.TestCase):

    def test_foo(self):
        print('hello')
        self.assertTrue(True)

class DiceTest(unittest.TestCase):

    def test_dice_bar_chart_100_samples(self):
        dice_result = dice.diceroller(samples=100)
        dice.print_bar_chart(dice_result)

class FractionTest(unittest.TestCase):

    def test_foo(self):
        print('hi')
        self.assertTrue(True)

class GraphTest(unittest.TestCase):

    def test_foo(self):
        print('hi')
        self.assertTrue(True)