"""File: tests.py
Author: John Choi choi.1655@osu.edu
Version: March 21, 2022

The Ohio State University CSE4256 SP22 Homework 8.
Contains the unittest test cases.
"""

import unittest
from main import *
import random

class MainTest(unittest.TestCase):

    times_run = 10000

    def test_uniform(self):
        # try calling the uniform function 100 times
        for _ in range(self.times_run):
            a, b = random.randint(0, 1000), random.randint(0, 1000)
            while a == b:
                a, b = random.randint(0, 1000), random.randint(0, 1000)
            if b < a:
                a, b = b, a
            random_num = uniform(a, b)
            self.assertTrue(random_num >= a and random_num < b, f'{random_num=}, {a=}, {b=}')

    def test_randrange(self):
        # try calling the uniform function 100 times
        for _ in range(self.times_run):
            a, b = random.randint(0, 1000), random.randint(0, 1000)
            while a == b:
                a, b = random.randint(0, 1000), random.randint(0, 1000)
            if b < a:
                a, b = b, a
            random_num = uniform(a, b)
            self.assertTrue(random_num >= a and random_num < b, f'{random_num=}, {a=}, {b=}')

    def test_choice(self):
        input = [random.randint(0, 100) for x in range(10)]
        for _ in range(self.times_run):
            random_selected = choice(input)
            self.assertTrue(random_selected in input)

    def test_std_card_deck(self):
        deck = std_card_deck()
        self.assertEqual(len(deck), 13 * 4)

        spades, diamonds, hearts, clubs = 0, 0, 0, 0
        for card in deck:
            if card.suit == 'Spades':
                spades += 1
            elif card.suit == 'Hearts':
                hearts += 1
            elif card.suit == 'Diamonds':
                diamonds += 1
            else:
                clubs += 1
        self.assertTrue(spades == 13 and spades == diamonds and diamonds == hearts and hearts == clubs)


    def test_riffle_shuffle(self):
        original_deck = std_card_deck()
        deck = std_card_deck()

        riffle_shuffle(deck)
        self.assertEqual(len(original_deck), len(deck))
        self.assertNotEqual(original_deck, deck)

    def test_mix_deck(self):
        original_deck = std_card_deck()
        deck = std_card_deck()

        mix_deck(deck)
        self.assertEqual(len(original_deck), len(deck))
        self.assertNotEqual(original_deck, deck)

    def test_deal_5(self):
        deck = std_card_deck()
        cards = deal(deck, 5)
        self.assertTrue(len(cards) == 5)

    def test_deal_1(self):
        deck = std_card_deck()
        cards = deal(deck, 1)
        self.assertTrue(len(cards) == 1 and len(cards[0]) == 52)

if __name__ == '__main__':
    test_suite = unittest.TestLoader().loadTestsFromTestCase(MainTest)
    unittest.TextTestRunner(verbosity=2).run(test_suite)