"""File: tests.py
Author: John Choi choi.1655@osu.edu
Version: March 4, 2022

The Ohio State University CSE4256 SP22 Homework 7.
Contains the unittest test cases.
"""

import unittest
import dice
import words
import os

class WordTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        # create a file for testing
        cls.filename1 = 'input1.txt'
        with open(cls.filename1, 'w') as f:
            f.write('this is\n')
            f.write('my file\n')
            f.write('this is not\n')
            f.write('your file\n')
        # create another file for testing
        cls.filename2 = 'input2.txt'
        with open(cls.filename2, 'w') as f:
            f.write('hello\n')
            f.write('world\n')
            f.write('go\n')
            f.write('bucks\n')

    @classmethod
    def tearDownClass(cls) -> None:
        if os.path.exists(cls.filename1):
            os.remove(cls.filename1)
        if os.path.exists(cls.filename2):
            os.remove(cls.filename2)

    def test_file1(self):
        expected = {'this': 0, 'is': 0, 'my': 1, 'file': 1, 'not': 2, 'your': 3}
        actual = words.firstlines(self.filename1)
        self.assertEqual(expected, actual)

    def test_file2(self):
        expected = {'hello': 0, 'world': 1, 'go': 2, 'bucks': 3}
        actual = words.firstlines(self.filename2)
        self.assertEqual(expected, actual)

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

# usage to indicate main.py entrypoint
if __name__ == '__main__':
    print('usage: python3 main.py')