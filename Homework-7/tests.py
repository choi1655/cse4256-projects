"""File: tests.py
Author: John Choi choi.1655@osu.edu
Version: March 4, 2022

The Ohio State University CSE4256 SP22 Homework 7.
Contains the unittest test cases.
"""

import unittest
import main
import dice
import words
import os
from fraction import Fraction

class WordTest(unittest.TestCase):

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

    def test_str_rep_fraction_1(self):
        input = '5/3'
        expected = Fraction(5, 3)
        actual = Fraction.from_str(input)
        self.assertEqual(actual, expected)

    def test_str_rep_fraction_2(self):
        input = '-18/36'
        expected = Fraction(-18, 36)
        actual = Fraction.from_str(input)
        self.assertEqual(actual, expected)

    def test_str_rep_decimal_1(self):
        input = '47.625'
        expected = Fraction(381, 8)
        actual = Fraction.from_str(input)
        self.assertEqual(actual, expected)

    def test_str_rep_decimal_2(self):
        input = '-8.3333'
        expected = Fraction(-83333, 10000)
        actual = Fraction.from_str(input)
        self.assertEqual(actual, expected)

    def test_str_rep_zero_1(self):
        input = '0 / 10'
        expected = Fraction(0, 1)
        actual = Fraction.from_str(input)
        self.assertEqual(actual, expected)

    def test_str_rep_zero_2(self):
        input = '0.0'
        expected = Fraction(0, 1)
        actual = Fraction.from_str(input)
        self.assertEqual(actual, expected)

    def test_str_rep_invalid_1(self):
        input = '-123.23/34.3232'
        with self.assertRaises(ValueError) as e:
            Fraction.from_str(input)
        self.assertTrue('str_rep can only contain one decimal or one fraction.' in str(e.exception))

    def test_str_rep_invalid_2(self):
        input = '123/32/32/22'
        with self.assertRaises(ValueError) as e:
            Fraction.from_str(input)
        self.assertTrue('str_rep cannot contain more than 1 division operator' in str(e.exception))

    def test_str_rep_invalid_3(self):
        input = '(32) / 21'
        with self.assertRaises(ValueError) as e:
            Fraction.from_str(input)
        self.assertTrue('str_rep can only contain one decimal or one fraction.' in str(e.exception))

    def test_str_rep_invalid_4(self):
        input = '34.34.34.3'
        with self.assertRaises(ValueError):
            Fraction.from_str(input)

    def test_str_rep_init_fraction(self):
        input = '5/3'
        expected = Fraction(5, 3)
        actual = Fraction(input)
        self.assertEqual(actual, expected)

    def test_str_rep_init_decimal(self):
        input = '47.625'
        expected = Fraction(381, 8)
        actual = Fraction(input)
        self.assertEqual(actual, expected)

class GraphTest(unittest.TestCase):

    def test_foo(self):
        print('hi')
        self.assertTrue(True)

if __name__ == '__main__':
    # run test cases in this file
    tests = [WordTest, DiceTest, FractionTest, GraphTest]
    for test in tests:
        suite = unittest.TestLoader().loadTestsFromTestCase(test)
        unittest.TextTestRunner(verbosity=2).run(suite)