"""Main driver.

Author: John Choi choi.1655@osu.edu
Version: Feb 20, 2022
"""

# Number 2 in homework 5. Two import statments.
# Importing the entire module hw5_fraction into main.py.
import hw5_fraction
# Importing only the class Fraction into main.py
from hw5_fraction import Fraction
# Giving the imported entity a shorter name
import hw5_fraction as fraction

# Test case 1
"""Initialization and printing of a fraction with value 0. Hint: Such a fraction should
have denominator 1 in reduced form.
"""
f = Fraction(0, 1)
print(f.mixed_number())

# Test case 2
"""Initialization and printing of a fraction with numerator and denominator that are
relatively prime.
"""
f = Fraction(3, 7)
print(f.mixed_number())

# Test case 3
"""Initialization and printing of a fraction with nonzero numerator and denominator that
are not relatively prime.
"""
f = Fraction(4, 10)
print(f.mixed_number())

# Test case 4
"""The sum of two fractions with the same denominator.
"""
f = Fraction(4, 10)
f1 = Fraction(6, 10)
sum = f + f1
print(sum.mixed_number())

# Test case 5
"""The sum of two fractions with different denominators.
"""
f = Fraction(2, 3)
f1 = Fraction(5, 6)
sum = f + f1
print(sum.mixed_number())
