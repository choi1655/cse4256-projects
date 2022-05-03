
import unittest
from hw5_fraction import Fraction

class TestFraction(unittest.TestCase):
    """Unit tests for the Fraction class"""

    def test_mixed_number_simple(self):
        """Tests with the mixed number"""
        fraction = Fraction(5, 3)
        expected = '1 2/3'
        self.assertEqual(fraction.mixed_number(), expected)

    def test_mixed_number_no_leftover(self):
        """Tests with regular fraction"""
        fraction = Fraction(2, 3)
        expected = '2/3'
        self.assertEqual(fraction.mixed_number(), expected)

    def test_mixed_number_simplify(self):
        """Tests with the regular fraction that needs simplifying"""
        fraction = Fraction(4, 10)
        expected = '2/5'
        self.assertEqual(fraction.mixed_number(), expected)

    def test_two_negatives(self):
        """Tests negative fraction"""
        fraction = Fraction(-4, -10)
        expected = '2/5'
        self.assertEqual(fraction.mixed_number(), expected)

    def test_mixed_number_multiple_leftover(self):
        """Tests fraction that needs conversion to
        mixed fraction
        """
        fraction = Fraction(8, 3)
        expected = '2 2/3'
        self.assertEqual(fraction.mixed_number(), expected)

    def test_whole_number(self):
        """Tests whole number"""
        fraction = Fraction(10, 1)
        expected = '10/1'
        self.assertEqual(fraction.mixed_number(), expected)

    def test_zero(self):
        """Tests zeros"""
        fraction = Fraction(0, 1)
        expected = '0/1'
        self.assertEqual(fraction.mixed_number(), expected)

        fraction = Fraction(0, 10)
        expected = '0/1'
        self.assertEqual(fraction.mixed_number(), expected)

    def test_negative_fraction(self):
        """Tests negative fraction"""
        fraction = Fraction(-2, 3)
        expected = '-2/3'
        self.assertEqual(fraction.mixed_number(), expected)

    def test_negative_fraction_2(self):
        """Tests negative fraction with negative denom"""
        fraction = Fraction(2, -3)
        expected = '-2/3'
        self.assertEqual(fraction.mixed_number(), expected)

    def test_negative_simple(self):
        """Tests negative regular fraction that needs
        conversion to mixed number
        """
        fraction = Fraction(-5, 3)
        expected = '-1 2/3'
        self.assertEqual(fraction.mixed_number(), expected)

    def test_negative_simple_2(self):
        """Tests negative regular fraction with negative
        denominator that needs conversion
        to mixed number
        """
        fraction = Fraction(5, -3)
        expected = '-1 2/3'
        self.assertEqual(fraction.mixed_number(), expected)

    def test_negative_simplify(self):
        """Tests negative fraction that needs simplifying"""
        fraction = Fraction(-4, 10)
        expected = '-2/5'
        self.assertEqual(fraction.mixed_number(), expected)

    def test_negative_simplify_2(self):
        """Testse negative fraction with negative
        denominator that needs simplifying
        """
        fraction = Fraction(4, -10)
        expected = '-2/5'
        self.assertEqual(fraction.mixed_number(), expected)

    def test_negative_mixed_number(self):
        """Tests negative fraction that needs conversion
        to mixed number
        """
        fraction = Fraction(-8, 3)
        expected = '-2 2/3'
        self.assertEqual(fraction.mixed_number(), expected)

    def test_negative_mixed_number_2(self):
        """Tests negative fraction with negative denominator
        that needs conversion to mixed number
        """
        fraction = Fraction(8, -3)
        expected = '-2 2/3'
        self.assertEqual(fraction.mixed_number(), expected)

    def test_repr(self):
        """Tests __repr__ function"""
        fractions = [
            (Fraction(5, 3), '5/3'),
            (Fraction(2, 3), '2/3'),
            (Fraction(4, 10), '2/5'),
            (Fraction(8, 3), '8/3'),
            (Fraction(10, 1), '10/1'),
            (Fraction(0, 1), '0/1'),
            (Fraction(0, 10), '0/1')
        ]

        for key, value in fractions:
            self.assertEqual(repr(key), value)

    def test_str(self):
        """Tests __str__ function"""
        fractions = [
            (Fraction(5, 3), '5/3'),
            (Fraction(2, 3), '2/3'),
            (Fraction(4, 10), '2/5'),
            (Fraction(8, 3), '8/3'),
            (Fraction(10, 1), '10/1'),
            (Fraction(0, 1), '0/1'),
            (Fraction(0, 10), '0/1')
        ]

        for key, value in fractions:
            self.assertEqual(str(key), value)

    def test_equals(self):
        """Tests __eq__ function"""
        fraction1 = Fraction(2, 3)
        fraction2 = Fraction(2, 3)
        self.assertEqual(fraction1, fraction2)

    def test_equals_different_but_same(self):
        """Tests __eq__ function with two fractions
        that are equal but looks different
        """
        fraction1 = Fraction(2, 3)
        fraction2 = Fraction(4, 6)
        self.assertEqual(fraction1, fraction2)

    def test_inequal(self):
        """Tests inequal fractions"""
        fraction1 = Fraction(2, 3)
        fraction2 = Fraction(5, 6)
        self.assertNotEqual(fraction1, fraction2)

    def test_neg(self):
        """Tests __negate__ function"""
        fraction1 = Fraction(2, 3)
        expected = Fraction(-2, 3)
        self.assertEqual(-fraction1, expected)

    def test_invert(self):
        """Tests __invert__ function"""
        fraction1 = Fraction(2, 3)
        expected = Fraction(3, 2)
        self.assertEqual(~fraction1, expected)

    def test_invert_negative(self):
        """Tests __invert__ function with
        negative numbers
        """
        fraction1 = Fraction(-2, 3)
        expected = Fraction(-3, 2)
        self.assertEqual(~fraction1, expected)

    def test_add_1(self):
        """Tests addition"""
        fraction1 = Fraction(5, 2)
        fraction2 = Fraction(13, 4)
        expected = Fraction(23, 4)
        self.assertEqual(fraction1 + fraction2, expected)

    def test_add_2(self):
        """Tests addition"""
        fraction1 = Fraction(5, 9)
        fraction2 = Fraction(1, 3)
        expected = Fraction(8, 9)
        self.assertEqual(fraction1 + fraction2, expected)

    def test_add_3(self):
        """Tests addition"""
        fraction1 = Fraction(10, 1)
        fraction2 = Fraction(4, 1)
        expected = Fraction(14, 1)
        self.assertEqual(fraction1 + fraction2, expected)

    def test_add_4(self):
        """Tests addition"""
        fraction1 = Fraction(-1, 2)
        fraction2 = Fraction(3, 2)
        expected = Fraction(1, 1)
        self.assertEqual(fraction1 + fraction2, expected)

    def test_add_5(self):
        """Tests addition"""
        fraction1 = Fraction(3, 4)
        fraction2 = Fraction(7, 10)
        fraction3 = Fraction(2, 5)
        expected = Fraction(37, 20)
        self.assertEqual(fraction1 + fraction2 + fraction3, expected)

    def test_subtract_1(self):
        """Tests subtraction"""
        fraction1 = Fraction(3, 6)
        fraction2 = Fraction(1, 6)
        expected = Fraction(2, 6)
        self.assertEqual(fraction1 - fraction2, expected)

    def test_subtract_2(self):
        """Tests subtraction"""
        fraction1 = Fraction(10, 11)
        fraction2 = Fraction(7, 11)
        expected = Fraction(3, 11)
        self.assertEqual(fraction1 - fraction2, expected)

    def test_subtract_3(self):
        """Tests subtraction"""
        fraction1 = Fraction(1, 3)
        fraction2 = Fraction(1, 6)
        expected = Fraction(1, 6)
        self.assertEqual(fraction1 - fraction2, expected)

    def test_subtract_4(self):
        """Tests subtraction"""
        fraction1 = Fraction(23, 24)
        fraction2 = Fraction(2, 3)
        expected = Fraction(7, 24)
        self.assertEqual(fraction1 - fraction2, expected)

    def test_subtract_5(self):
        """Tests subtraction"""
        fraction1 = Fraction(21, 28)
        fraction2 = Fraction(3, 4)
        expected = Fraction(0, 1)
        self.assertEqual(fraction1 - fraction2, expected)

    def test_subtract_6(self):
        """Tests subtraction"""
        fraction1 = Fraction(11, 8)
        fraction2 = Fraction(2, 3)
        expected = Fraction(17, 24)
        self.assertEqual(fraction1 - fraction2, expected)

    def test_multiply_1(self):
        """Tests multiplication"""
        fraction1 = Fraction(1, 3)
        fraction2 = Fraction(5, 1)
        expected = Fraction(5, 3)
        self.assertEqual(fraction1 * fraction2, expected)

    def test_multiply_2(self):
        """Tests multiplication"""
        fraction1 = Fraction(4, 7)
        fraction2 = Fraction(5, 6)
        expected = Fraction(20, 42)
        self.assertEqual(fraction1 * fraction2, expected)

    def test_multiply_3(self):
        """Tests multiplication"""
        fraction1 = Fraction(5, 4)
        fraction2 = Fraction(-4, 9)
        expected = Fraction(-5, 9)
        self.assertEqual(fraction1 * fraction2, expected)

    def test_multiply_4(self):
        """Tests multiplication"""
        fraction1 = Fraction(-5, 8)
        fraction2 = Fraction(4, 3)
        fraction3 = Fraction(8, -7)
        expected = Fraction(20, 21)
        self.assertEqual(fraction1 * fraction2 * fraction3, expected)

    def test_divide_1(self):
        """Tests division"""
        fraction1 = Fraction(2, 3)
        fraction2 = Fraction(1, 2)
        expected = Fraction(4, 3)
        self.assertEqual(fraction1 / fraction2, expected)

    def test_divide_2(self):
        """Tests division"""
        fraction1 = Fraction(2, 9)
        fraction2 = Fraction(3, 10)
        expected = Fraction(20, 27)
        self.assertEqual(fraction1 / fraction2, expected)

    def test_divide_3(self):
        """Tests division"""
        fraction1 = Fraction(13, 9)
        fraction2 = Fraction(3, 5)
        expected = Fraction(65, 27)
        self.assertEqual(fraction1 / fraction2, expected)

    def test_divide_4(self):
        """Tests division"""
        fraction1 = Fraction(1, 7)
        fraction2 = Fraction(3, 4)
        expected = Fraction(4, 21)
        self.assertEqual(fraction1 / fraction2, expected)

    def test_less_than(self):
        """Tests less than function"""
        fraction1 = Fraction(1, 2)
        fraction2 = Fraction(3, 2)
        self.assertTrue(fraction1 < fraction2)

    def test_greater_than(self):
        """Tests greater than function"""
        fraction1 = Fraction(1, 2)
        fraction2 = Fraction(3, 2)
        self.assertTrue(fraction2 > fraction1)

    def test_greater_or_equal(self):
        """Tests greater or equal to function"""
        fraction1 = Fraction(1, 2)
        fraction2 = Fraction(1, 2)
        self.assertTrue(fraction1 <= fraction2)

    def test_less_than_or_equal(self):
        """Tests less than or equal to function"""
        fraction1 = Fraction(1, 2)
        fraction2 = Fraction(1, 2)
        self.assertTrue(fraction1 >= fraction2)

if __name__ == '__main__':
    unittest.main()
