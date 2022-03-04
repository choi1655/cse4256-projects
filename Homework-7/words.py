"""File: words.py
Author: John Choi choi.1655@osu.edu
Version: February 28, 2022

The Ohio State University CSE4256 SP22 Homework 7.
"""

"""Generates the sequence of words in string `s`."""
def words(s):
    word_list = s.split()
    for word in word_list:
	    yield word

def firstlines(filename):
    """TODO Use the generator function words(s) to write a function called firstlines(filename)
    that builds a dictionary of every word that appears in a file mapped to the line number on which it first appears.
    For example, suppose the contents of the file foo.txt are
    this is
    my file
    this is not
    your file

    Then a call to firstlines("foo.txt") should produce the dictionary {'this':0, 'is': 0, 'my', 1, 'file': 1, 'not': 2, 'your': 3).
    """
    map = {}
    # open the file
    with open(filename, 'r') as f:
        counter = 0
        for line in f:
            # split line by spaces and newlines
            # go through the words
            word_gen = words(line)
            for word in word_gen:
                if word not in map:
                    map[word] = counter
            counter += 1
    return map