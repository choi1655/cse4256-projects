"""File: main.py
Author: John Choi choi.1655@osu.edu
Version: February 28, 2022

The Ohio State University CSE4256 SP22 Homework 7.
"""
import unittest

# Problem 1
def triangles(n) -> list:
    """Write a function called triangles(n) that, given a positive integer n, produces
    a list of the first n triangle numbers. You may assume that n is a positive integer.
    """
    numbers = []
    number = 0
    for i in range(1, n + 1):
        numbers.append(number + i)
        number += i
    return numbers

def ctriangles(n):
    """Write a function called ctriangles(n) that produces a list identical to triangles(n), but does so using a
    single-line list comprehension. Hint: the built-in function sum(s) is probably useful here.
    """
    # 1, 3, 6, 10, 15
    # 1, 2, 3, 4, 5
    return [sum([j for j in range(i + 1)]) for i in range(1, n + 1)]

def pascal(r):
    """Write a function called pascal(r) that, given a positive integer r, produces a list containing
    the first r rows of Pascal's Triangle (more precisely, the function should only generate
    all non-zero entries in the triangle). You may assume that r is a positive integer. You should not
    import any modules to complete this task, including the math module.
    """
    pass

class TestTriangles(unittest.TestCase):

    def test_triangles(self):
        input = 5
        expected = [1, 3, 6, 10, 15]
        self.assertEqual(triangles(input), expected)

    def test_triangles_0(self):
        input = 0
        expected = []
        self.assertEqual(triangles(input), expected)

    def test_triangles_1(self):
        input = 1
        expected = [1]
        self.assertEqual(ctriangles(input), expected)

    def test_ctriangles(self):
        input = 5
        expected = [1, 3, 6, 10, 15]
        self.assertEqual(ctriangles(input), expected)

    def test_ctriangles_0(self):
        input = 0
        expected = []
        self.assertEqual(ctriangles(input), expected)

    def test_ctriangles_1(self):
        input = 1
        expected = [1]
        self.assertEqual(ctriangles(input), expected)

# run the test cases
if __name__ == '__main__':
    unittest.main()
