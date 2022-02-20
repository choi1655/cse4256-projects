"""Contains a class that represents a Fraction (i.e., a rational number).

Author: John Choi choi.1655@osu.edu
Version: Feb 20, 2022
"""

# Import statements go here
import math

# TODO: Implement the class Fraction
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
        self.__num = num  # double underscores to indicate private
        self.__d = d  # double underscores to indicate private

    def mixed_number(self) -> str:
        """Returns a string representation of self in mixed number form.

        For example, if self is 5/3, mixed_number should return "1 2/3".
        """
        # if denominator is 1, meaning it's a whole number, simply print
        if self.__d == 1:
            return f'{self.__num}/1'
        integer = self.__num // self.__d if self.__num > self.__d else 0
        new_numerator = self.__num - self.__d if self.__num > self.__d else self.__num
        mixed_number: str = ''
        if integer != 0:
            mixed_number += f'{integer} '
        mixed_number += f'{new_numerator}/{self.__d}'
        return mixed_number

    def __repr__(self):
        """Returns a string that is [numerator]'/'[denominator].

        __repr__ is called by the builtin function repr, or by print if
        there is no definition for __str__.
        """

        # TODO: Implement this method.
        pass

    def __str__(self):
        """Returns a string that is [numerator]'/'[denominator].

        __str__ is called by the builtin print function.
        """

        # TODO: Implement this method.
        pass

    def __eq__(self, other: 'Fraction') -> bool:
        """Reports whether self is the same number as other.

        __eq__ is called by the equality operator, e.g., frac1 == frac2.
        """

        # TODO: Implement this method.
        pass

    def __neg__(self) -> 'Fraction':
        """Returns the negation of self.

        __neg__ is called by the unary minus operator, e.g., -frac.
        """

        # TODO: Implement this method.
        pass

    def __invert__(self) -> 'Fraction':
        """Returns the reciprocal of self.

        __invert__ is called by the unary tilde operator, e.g., ~frac.
        """

        # TODO: Implement this method.
        pass

    def __add__(self, other: 'Fraction') -> 'Fraction':
        """Returns the sum of self and other.

        __add__ is called by the binary plus operator, e.g., frac1 + frac2.
        """

        # TODO: Implement this method.
        pass

    def __mul__(self, other: 'Fraction') -> 'Fraction':
        """Returns the product of self and other.

        __mul__ is called by the binary times operator, e.g., frac1 * frac2.
        """

        # TODO: Implement this method.
        pass

    def __sub__(self, other: 'Fraction') -> 'Fraction':
        """Returns the difference of self and other.

        __sub__ is called by the binary minus operator, e.g., frac1 - frac2.
        """

        # TODO: Implement this method without calling the Fraction constructor directly.
        pass

    def __truediv__(self, other: 'Fraction') -> 'Fraction':
        """Returns the quotient of self and other.

        __div__ is called by the binary division operator, e.g., frac1 / frac2.
        """

        # TODO: Implement this method without calling the Fraction constructor directly.
        pass
