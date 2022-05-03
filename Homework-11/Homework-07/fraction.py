"""Contains a class that represents a Fraction (i.e., a rational number).

Author: John Choi choi.1655@osu.edu
Version: March 6, 2022

The Ohio State University CSE4256 SP22 Homework 7.
"""

# Import statements go here
import math
from functools import total_ordering

@total_ordering
class Fraction:
    """A rational number.

    Fraction should have no public instance variables.
    """

    def __init__(self, *args):
        """Produces the fraction n/d in reduced form.

        By "reduced form", we mean that in the produced fraction, the numerator
        and denominator are relatively prime.
        """
        if len(args) == 2:
            num = args[0]
            denominator = args[1]
            gcd = math.gcd(num, denominator)
            num //= gcd
            denominator //= gcd
            # double underscores to indicate private
            self.__is_negative = (num < 0) ^ (denominator < 0)
            self.__num = abs(num)  # double underscores to indicate private
            self.__d = abs(denominator)  # double underscores to indicate private
        elif len(args) == 1:
            str_rep = str(args[0])
            result = Fraction.from_str(str_rep)
            self.__is_negative = result.__is_negative
            self.__num = result.__num
            self.__d = result.__d
        else:
            raise ValueError(f'Invalid arguments {args}')

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
        return self.__is_negative == other.__is_negative and \
            self.__num == other.__num and \
                self.__d == other.__d

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

    @classmethod
    def from_str(cls, str_rep: str) -> 'Fraction':
        """Produces a fraction from string str_rep.
        Requires str_rep is in one of two forms.
        Either str_rep is the string representation of a fraction(e.g., `5/3` or `-18/36`),
        or str_rep is the string representation of a decimal number(e.g., `47.625` or `-8.3333`).
        The returned fraction should be in reduced form and have the
        value one would "expect" from the input string.
        """
        # check for invalid str rep
        if ('/' in str_rep and '.' in str_rep) or '(' in str_rep or ')' in str_rep:
            raise ValueError('str_rep can only contain one decimal or one fraction.')
        is_decimal = '.' in str_rep
        if is_decimal:
            denom = 1
            decimal_points = len(str_rep) - str_rep.index('.') - 1
            for _ in range(decimal_points):
                denom *= 10

            numerator = int(float(str_rep) * denom)
            return Fraction(numerator, denom)
        numbers = str_rep.split('/')
        if len(numbers) != 2:
            raise ValueError('str_rep cannot contain more than 1 division operator')
        return Fraction(int(numbers[0]), int(numbers[1]))
