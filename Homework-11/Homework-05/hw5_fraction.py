"""Contains a class that represents a Fraction (i.e., a rational number).

Author: John Choi choi.1655@osu.edu
Version: Feb 20, 2022
"""

# Import statements go here
import math
from functools import total_ordering

@total_ordering
class Fraction:
    """A rational number.

    Fraction should have no public instance variables.
    """

    def __init__(self, num: int, d: int):
        """Produces the fraction n/d in reduced form.

        By "reduced form", we mean that in the produced fraction, the numerator
        and denominator are relatively prime.
        """

        gcd = math.gcd(num, d)
        num //= gcd
        d //= gcd
        self.__is_negative = (num < 0) ^ (d < 0)  # double underscores to indicate private
        self.__num = abs(num)  # double underscores to indicate private
        self.__d = abs(d)  # double underscores to indicate private

    def mixed_number(self) -> str:
        """Returns a string representation of self in mixed number form.

        For example, if self is 5/3, mixed_number should return "1 2/3".
        """
        # if denominator is 1 (whole number), simply return
        if self.__d == 1:
            return f'-{self.__num}/{self.__d}' if self.__is_negative else f'{self.__num}/{self.__d}'
        whole_number = self.__num // self.__d
        numerator = self.__num - self.__d * whole_number
        mixed_number = ''
        if self.__is_negative:
            mixed_number += '-'
        if whole_number != 0:
            mixed_number += f'{whole_number} '
        mixed_number += f'{numerator}/{self.__d}'
        return mixed_number

    def __repr__(self):
        """Returns a string that is [numerator]'/'[denominator].

        __repr__ is called by the builtin function repr, or by print if
        there is no definition for __str__.
        """
        return f'{self.__num}/{self.__d}' if not self.__is_negative else f'-{self.__num}/{self.__d}'

    def __str__(self):
        """Returns a string that is [numerator]'/'[denominator].

        __str__ is called by the builtin print function.
        """
        return f'{self.__num}/{self.__d}' if not self.__is_negative else f'-{self.__num}/{self.__d}'

    def __eq__(self, other: 'Fraction') -> bool:
        """Reports whether self is the same number as other.

        __eq__ is called by the equality operator, e.g., frac1 == frac2.
        """
        return self.__is_negative == other.__is_negative and self.__num == other.__num and self.__d == other.__d

    def __neg__(self) -> 'Fraction':
        """Returns the negation of self.

        __neg__ is called by the unary minus operator, e.g., -frac.
        """
        numerator = self.__num if self.__is_negative else -self.__num
        return Fraction(numerator, self.__d)


    def __invert__(self) -> 'Fraction':
        """Returns the reciprocal of self.

        __invert__ is called by the unary tilde operator, e.g., ~frac.
        """
        numerator = -self.__d if self.__is_negative else self.__d
        return Fraction(numerator, self.__num)

    def __add__(self, other: 'Fraction') -> 'Fraction':
        """Returns the sum of self and other.

        __add__ is called by the binary plus operator, e.g., frac1 + frac2.
        """
        this_numerator = self.__num
        if self.__is_negative:
            this_numerator *= -1
        this_denominator = self.__d
        other_numerator = other.__num
        if other.__is_negative:
            other_numerator *= -1
        other_denominator = other.__d

        # if denoms are same, simply add them together and return
        if this_denominator == other_denominator:
            return Fraction(this_numerator + other_numerator, this_denominator)
        
        common_denom = this_denominator * other_denominator
        this_numerator *= other_denominator
        other_numerator *= this_denominator
        numerator = this_numerator + other_numerator
        return Fraction(numerator, common_denom)


    def __mul__(self, other: 'Fraction') -> 'Fraction':
        """Returns the product of self and other.

        __mul__ is called by the binary times operator, e.g., frac1 * frac2.
        """
        this_numerator = -self.__num if self.__is_negative else self.__num
        other_numerator = -other.__num if other.__is_negative else other.__num
        denom = self.__d * other.__d
        return Fraction(this_numerator * other_numerator, denom)

    def __sub__(self, other: 'Fraction') -> 'Fraction':
        """Returns the difference of self and other.

        __sub__ is called by the binary minus operator, e.g., frac1 - frac2.
        """
        return self + -other

    def __truediv__(self, other: 'Fraction') -> 'Fraction':
        """Returns the quotient of self and other.

        __div__ is called by the binary division operator, e.g., frac1 / frac2.
        """
        return self * ~other
    
    def __lt__(self, other):
        """Returns true if self is less than the other
        __lt__ is called by the less than operator <, e.g., frac1 < frac2.
        """
        this_numerator = -self.__num if self.__is_negative else self.__num
        other_numerator = -other.__num if other.__is_negative else other.__num
        this_value = this_numerator / self.__d
        other_value = other_numerator / other.__d
        return this_value < other_value


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

"""More test cases on test_fraction.py"""

"""Tests comparisons"""
# Test case 6
print(f < f1)
