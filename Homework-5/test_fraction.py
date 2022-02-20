
from ast import expr_context
import hw5_fraction as fraction
import unittest

class TestFraction(unittest.TestCase):

    def test_mixed_number_simple(self):
        f = fraction.Fraction(5, 3)
        expected = '1 2/3'
        self.assertEqual(f.mixed_number(), expected)
    
    def test_mixed_number_no_leftover(self):
        f = fraction.Fraction(2, 3)
        expected = '2/3'
        self.assertEqual(f.mixed_number(), expected)
    
    def test_mixed_number_simplify(self):
        f = fraction.Fraction(4, 10)
        expected = '2/5'
        self.assertEqual(f.mixed_number(), expected)
    
    def test_mixed_number_multiple_leftover(self):
        f = fraction.Fraction(8, 3)
        expected = '2 2/3'
        self.assertEqual(f.mixed_number(), expected)
    
    def test_whole_number(self):
        f = fraction.Fraction(10, 1)
        expected = '10/1'
        self.assertEqual(f.mixed_number(), expected)
    
    def test_zero(self):
        f = fraction.Fraction(0, 1)
        expected = '0/1'
        self.assertEqual(f.mixed_number(), expected)

        f = fraction.Fraction(0, 10)
        expected = '0/1'
        self.assertEqual(f.mixed_number(), expected)
    
    def test_repr(self):
        fractions = [
            (fraction.Fraction(5, 3), '5/3'), 
            (fraction.Fraction(2, 3), '2/3'),
            (fraction.Fraction(4, 10), '2/5'),
            (fraction.Fraction(8, 3), '8/3'),
            (fraction.Fraction(10, 1), '10/1'),
            (fraction.Fraction(0, 1), '0/1'),
            (fraction.Fraction(0, 10), '0/1')
        ]

        for key, value in fractions:
            self.assertEqual(repr(key), value)
    
    def test_str(self):
        fractions = [
            (fraction.Fraction(5, 3), '5/3'), 
            (fraction.Fraction(2, 3), '2/3'),
            (fraction.Fraction(4, 10), '2/5'),
            (fraction.Fraction(8, 3), '8/3'),
            (fraction.Fraction(10, 1), '10/1'),
            (fraction.Fraction(0, 1), '0/1'),
            (fraction.Fraction(0, 10), '0/1')
        ]

        for key, value in fractions:
            self.assertEqual(str(key), value)

if __name__ == '__main__':
    unittest.main()
