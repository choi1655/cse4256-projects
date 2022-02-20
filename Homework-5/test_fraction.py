

from hw5_fraction import Fraction
import unittest

class TestFraction(unittest.TestCase):

    def test_mixed_number_simple(self):
        f = Fraction(5, 3)
        expected = '1 2/3'
        self.assertEqual(f.mixed_number(), expected)
    
    def test_mixed_number_no_leftover(self):
        f = Fraction(2, 3)
        expected = '2/3'
        self.assertEqual(f.mixed_number(), expected)
    
    def test_mixed_number_simplify(self):
        f = Fraction(4, 10)
        expected = '2/5'
        self.assertEqual(f.mixed_number(), expected)
    
    def test_mixed_number_multiple_leftover(self):
        f = Fraction(8, 3)
        expected = '2 2/3'
        self.assertEqual(f.mixed_number(), expected)
    
    def test_whole_number(self):
        f = Fraction(10, 1)
        expected = '10/1'
        self.assertEqual(f.mixed_number(), expected)
    
    def test_zero(self):
        f = Fraction(0, 1)
        expected = '0/1'
        self.assertEqual(f.mixed_number(), expected)

        f = Fraction(0, 10)
        expected = '0/1'
        self.assertEqual(f.mixed_number(), expected)

    def test_negative_fraction(self):
        f = Fraction(-2, 3)
        expected = '-2/3'
        self.assertEqual(f.mixed_number(), expected)
    
    def test_negative_simple(self):
        f = Fraction(-5, 3)
        expected = '-1 2/3'
        self.assertEqual(f.mixed_number(), expected)
    
    def test_negative_simplify(self):
        f = Fraction(-4, 10)
        expected = '-2/5'
        self.assertEqual(f.mixed_number(), expected)

    def test_negative_mixed_number(self):
        f = Fraction(-8, 3)
        expected = '-2 2/3'
        self.assertEqual(f.mixed_number(), expected)
    
    def test_repr(self):
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
        f1 = Fraction(2, 3)
        f2 = Fraction(2, 3)
        self.assertEqual(f1, f2)
    
    def test_equals_different_but_same(self):
        f1 = Fraction(2, 3)
        f2 = Fraction(4, 6)
        self.assertEqual(f1, f2)
    
    def test_inequal(self):
        f1 = Fraction(2, 3)
        f2 = Fraction(5, 6)
        self.assertNotEqual(f1, f2)

    def test_neg(self):
        f1 = Fraction(2, 3)
        expected = Fraction(-2, 3)
        self.assertEqual(-f1, expected)

if __name__ == '__main__':
    unittest.main()
