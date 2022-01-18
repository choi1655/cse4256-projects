
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


def ispartitionable(s: list) -> bool:
    """
    Problem 3.
    Write a function called ispartitionable(s) that, given a list of integers, return True if the
    list can be partitioned into two contiguous slices such that the sum of the elements of
    one slice is equal to the sum of the elements of the other slice, False otherwise. You may
    assume the list s contains only integers. Formally, the function should return True if the
    following holds, and False otherwise.
    """
    # 1, 2, 3, 2, 4
    # 1, 2, 3       2, 4

    left = s[0]
    right = sum(s[1:])
    if left == right:
        return True
    
    for i in range(1, len(s)):
        left += s[i]
        right -= s[i]
        if left == right:
            return True
    return False