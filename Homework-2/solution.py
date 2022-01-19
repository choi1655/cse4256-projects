
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

def fiblist(n):
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


def ispartitionable(s):
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

"""
Problem 4.
The list comprehension given on slide #15 of the second lecture to generate the n-row
identity matrix uses a nested list comprehension. Write an alternate comprehension that is
not nested to produce the same result, and store that list in a variable called m. Hint: the
sequence repetition (*) and concatenation (+) operators will come in handy.



"""

"""
Problem 5.
Write a list comprehension that produces a list containing the sums of the rows in a matrix
m, and store that list in a variable named sums. You may assume m is previously defined.


sums = [sum(m[x]) for x in range(len(m))]
"""

def vowelcount(s):
    """
    Problem 6.
    Write a function called vowelcount(s) that, given a string, returns the number of characters in the
    string that are English vowels (i.e., one of the characters 'a', 'e', 'i', 'o', or 'u').
    The function should be case-agnostic meaning that, e.g., the character 'A' counts as a vowel.
    """
    s_lower = s.lower()

    # keep a set for vowels
    vowels = {'a', 'e', 'i', 'o', 'u'}
    counter = 0
    for char in s_lower:
        if char in vowels:
            counter += 1
    return counter


def listfromcsv(s):
    """
    Problem 7.
    Write a function called listfromcsv(s) that, given a string containing several lines of comma-separated
    values (e.g., s may be "5,8,hello,2\n9,14,world,1344"), produces a (2-dimensional) list of those values
    separated by line (e.g., for the example given, the result should be the list
    [['5', '8', 'hello', '2'], ['9', '14', 'world', '1344']]).
    """
    result = []
    splitted = s.split('\n')
    for line in splitted:
        result.append(line.split(','))
    return result
