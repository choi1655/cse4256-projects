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
        numerator = self.__num
        denominator = self.__d
        is_negative = (numerator < 0) ^ (denominator < 0)
        if is_negative:
            numerator = abs(numerator)
            denominator = abs(denominator)
        
        # if denominator is 1, meaning it's a whole number, simply print
        if denominator == 1:
            result = ''
            if is_negative:
                result += '-'
            result += f'{numerator}/1'
            return result
        
        # integer refers to the whole number in front of the fraction
        integer = numerator // denominator if numerator > denominator else 0
        # calculate reduced numerator
        new_numerator = numerator - (denominator * integer) if numerator > denominator else numerator
        mixed_number: str = ''
        if is_negative:
            mixed_number += '-'
        if integer != 0:
            mixed_number += f'{integer} '
        mixed_number += f'{new_numerator}/{denominator}'
        return mixed_number

    def __repr__(self):
        """Returns a string that is [numerator]'/'[denominator].

        __repr__ is called by the builtin function repr, or by print if
        there is no definition for __str__.
        """
        return f'{self.__num}/{self.__d}'

    def __str__(self):
        """Returns a string that is [numerator]'/'[denominator].

        __str__ is called by the builtin print function.
        """
        return f'{self.__num}/{self.__d}'

    def __eq__(self, other: 'Fraction') -> bool:
        """Reports whether self is the same number as other.

        __eq__ is called by the equality operator, e.g., frac1 == frac2.
        """
        return self.__d == other.__d and self.__num == other.__num

    def __neg__(self) -> 'Fraction':
        """Returns the negation of self.

        __neg__ is called by the unary minus operator, e.g., -frac.
        """
        return Fraction(-self.__num, self.__d)

    def __invert__(self) -> 'Fraction':
        """Returns the reciprocal of self.

        __invert__ is called by the unary tilde operator, e.g., ~frac.
        """

        return Fraction(self.__d, self.__num)

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
