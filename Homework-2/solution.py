
# CSE4256 Homework 2.
# Author: John Choi choi.1655@osu.edu
# Version: Jan 18, 2022

"""
Problem 1. s = "PYTHON"
    a) s[-1], s[5]
    b) 'PYTHON'
    c) 'PYT'
    d) 'PTO'
    e) s[:4]
    f) s[3::2]
    g) s[5::-2]
"""

def fiblist(n: int) -> list:
    """
    Problem 2.
    Write a function called fiblist(n) that, given a positive integer n, produces a list containing the first n terms of the Fibonacci Sequence.
    You may assume that n is a positive integer.
    """
    result = []
    # base cases
    if n == 0:
        return result
    result.append(1)
    if n == 1:
        return result
    result.append(1)
    if n == 2:
        return result
    
    for i in range(2, n):
        nextValue = result[i - 2] + result[i - 1]
        result.append(nextValue)
    return result
