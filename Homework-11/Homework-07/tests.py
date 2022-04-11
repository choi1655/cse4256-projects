"""File: tests.py
Author: John Choi choi.1655@osu.edu
Version: March 14, 2022

The Ohio State University CSE4256 SP22 Homework 7.
Contains the unittest test cases.
"""

import unittest
from graph import EdgelistGraph, MatrixGraph, DictGraph
import dice
import words
import os
from fraction import Fraction

class WordTest(unittest.TestCase):
    """Unit test suite for the functions in word.py"""

    @classmethod
    def setUpClass(cls) -> None:
        # create a file for testing
        cls.filename1 = 'input1.txt'
        with open(cls.filename1, 'w', encoding='utf-8') as file:
            file.write('this is\n')
            file.write('my file\n')
            file.write('this is not\n')
            file.write('your file\n')
        # create another file for testing
        cls.filename2 = 'input2.txt'
        with open(cls.filename2, 'w', encoding='utf-8') as file:
            file.write('hello\n')
            file.write('world\n')
            file.write('go\n')
            file.write('bucks\n')

    @classmethod
    def tearDownClass(cls) -> None:
        if os.path.exists(cls.filename1):
            os.remove(cls.filename1)
        if os.path.exists(cls.filename2):
            os.remove(cls.filename2)

    def test_file1(self):
        """Tests the function using the first input file"""
        expected = {'this': 0, 'is': 0, 'my': 1, 'file': 1, 'not': 2, 'your': 3}
        actual = words.firstlines(self.filename1)
        self.assertEqual(expected, actual)

    def test_file2(self):
        """Tests the function using the second input file"""
        expected = {'hello': 0, 'world': 1, 'go': 2, 'bucks': 3}
        actual = words.firstlines(self.filename2)
        self.assertEqual(expected, actual)

class DiceTest(unittest.TestCase):
    """Unit test suite for the functions in dice.py"""

    def test_dice_bar_chart_100_samples(self):
        """Test using 100 samples"""
        print('sample = 100')
        dice_result = dice.diceroller(samples=100)
        dice.print_bar_chart(dice_result)

    def test_dice_bar_chart_500_samples(self):
        """Test using 500 samples"""
        print('sample = 500')
        dice_result = dice.diceroller(samples=500)
        dice.print_bar_chart(dice_result)

    def test_dice_bar_chart_default_samples(self):
        """Test using default number (10000) of samples"""
        print('sample = default')
        dice_result = dice.diceroller()
        dice.print_bar_chart(dice_result)

class FractionTest(unittest.TestCase):
    """Unit test suite for the functions in fraction.py"""

    def test_str_rep_fraction_1(self):
        """Tests the string to fraction functionality"""
        input_num = '5/3'
        expected = Fraction(5, 3)
        actual = Fraction.from_str(input_num)
        self.assertEqual(actual, expected)

    def test_str_rep_fraction_2(self):
        """Tests negative number"""
        input_num = '-18/36'
        expected = Fraction(-18, 36)
        actual = Fraction.from_str(input_num)
        self.assertEqual(actual, expected)

    def test_str_rep_decimal_1(self):
        """Tests floating number"""
        input_num = '47.625'
        expected = Fraction(381, 8)
        actual = Fraction.from_str(input_num)
        self.assertEqual(actual, expected)

    def test_str_rep_decimal_2(self):
        """Tests negative floating number"""
        input_num = '-8.3333'
        expected = Fraction(-83333, 10000)
        actual = Fraction.from_str(input_num)
        self.assertEqual(actual, expected)

    def test_str_rep_zero_1(self):
        """Tests zero"""
        input_num = '0 / 10'
        expected = Fraction(0, 1)
        actual = Fraction.from_str(input_num)
        self.assertEqual(actual, expected)

    def test_str_rep_zero_2(self):
        """Tests zero in floating number"""
        input_num = '0.0'
        expected = Fraction(0, 1)
        actual = Fraction.from_str(input_num)
        self.assertEqual(actual, expected)

    def test_str_rep_invalid_1(self):
        """Tests invalid with decimal and slashes"""
        input_num = '-123.23/34.3232'
        with self.assertRaises(ValueError) as e:
            Fraction.from_str(input_num)
        self.assertTrue('str_rep can only contain one decimal or one fraction.' in str(e.exception))

    def test_str_rep_invalid_2(self):
        """Tests multiple slashes"""
        input_num = '123/32/32/22'
        with self.assertRaises(ValueError) as e:
            Fraction.from_str(input_num)
        self.assertTrue('str_rep cannot contain more than 1 division operator' in str(e.exception))

    def test_str_rep_invalid_3(self):
        """Tests invalid fraction with invalid characters"""
        input_num = '(32) / 21'
        with self.assertRaises(ValueError) as e:
            Fraction.from_str(input_num)
        self.assertTrue('str_rep can only contain one decimal or one fraction.' in str(e.exception))

    def test_str_rep_invalid_4(self):
        """Tests multiple decimal points"""
        input_num = '34.34.34.3'
        with self.assertRaises(ValueError):
            Fraction.from_str(input_num)

    def test_str_rep_init_fraction(self):
        """Tests string fraction to fraction"""
        input_num = '5/3'
        expected = Fraction(5, 3)
        actual = Fraction(input_num)
        self.assertEqual(actual, expected)

    def test_str_rep_init_decimal(self):
        """Tests string decimal to fraction"""
        input_num = '47.625'
        expected = Fraction(381, 8)
        actual = Fraction(input_num)
        self.assertEqual(actual, expected)

class GraphTest(unittest.TestCase):
    """Unit test for the functions in graph.py"""

    def setUp(self) -> None:
        self.edgelist_graph = EdgelistGraph([(0, 1), (0, 2), (2, 1), (2, 3)])
        self.matrix_graph = MatrixGraph([
                                    [False, True, True, False],
                                    [True, False, True, False],
                                    [True, True, False, True],
                                    [False, False, True, False]
                                ])
        self.dict_graph = DictGraph({0: [1, 2], 1: [0, 2], 2: [0, 1, 3], 3: [2]})

    def test_dfs_edgelist(self):
        """Tests DFS algorithm for edgelist"""
        dfs_list = []
        for vertex in self.edgelist_graph.depth_first_search(start=1):
            dfs_list.append(vertex)
        expected = [1, 2, 3, 0]
        self.assertEqual(dfs_list, expected)

    def test_dfs_matrix(self):
        """Tests DFS algorithm for matrix"""
        dfs_list = []
        for vertex in self.matrix_graph.depth_first_search(start=1):
            dfs_list.append(vertex)
        expected = [1, 2, 3, 0]
        self.assertEqual(dfs_list, expected)

    def test_dfs_dict(self):
        """Tests DFS algorithm for dict"""
        dfs_list = []
        for vertex in self.dict_graph.depth_first_search(start=1):
            dfs_list.append(vertex)
        expected = [1, 2, 3, 0]
        self.assertEqual(dfs_list, expected)

    def test_bfs_edgelist(self):
        """Tests BFS algorithm for edgelist"""
        bfs_list = []
        for vertex in self.edgelist_graph.breadth_first_search(start=1):
            bfs_list.append(vertex)
        expected = [1, 0, 2, 3]
        self.assertEqual(bfs_list, expected)

    def test_bfs_matrix(self):
        """Tests BFS algorithm for matrix"""
        bfs_list = []
        for vertex in self.matrix_graph.breadth_first_search(start=1):
            bfs_list.append(vertex)
        expected = [1, 0, 2, 3]
        self.assertEqual(bfs_list, expected)

    def test_bfs_dict(self):
        """Tests BFS algorithm for dict"""
        bfs_list = []
        for vertex in self.dict_graph.breadth_first_search(start=1):
            bfs_list.append(vertex)
        expected = [1, 0, 2, 3]
        self.assertEqual(bfs_list, expected)

if __name__ == '__main__':
    # run test cases in this file
    tests = [WordTest, DiceTest, FractionTest, GraphTest]
    for test in tests:
        suite = unittest.TestLoader().loadTestsFromTestCase(test)
        v = 2 if test is not DiceTest else 0
        unittest.TextTestRunner(verbosity=v).run(suite)
