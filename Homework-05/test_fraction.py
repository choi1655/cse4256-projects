

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
    
    def test_two_negatives(self):
        f = Fraction(-4, -10)
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

    def test_negative_fraction_2(self):
        f = Fraction(2, -3)
        expected = '-2/3'
        self.assertEqual(f.mixed_number(), expected)
    
    def test_negative_simple(self):
        f = Fraction(-5, 3)
        expected = '-1 2/3'
        self.assertEqual(f.mixed_number(), expected)
    
    def test_negative_simple_2(self):
        f = Fraction(5, -3)
        expected = '-1 2/3'
        self.assertEqual(f.mixed_number(), expected)
    
    def test_negative_simplify(self):
        f = Fraction(-4, 10)
        expected = '-2/5'
        self.assertEqual(f.mixed_number(), expected)
    
    def test_negative_simplify_2(self):
        f = Fraction(4, -10)
        expected = '-2/5'
        self.assertEqual(f.mixed_number(), expected)

    def test_negative_mixed_number(self):
        f = Fraction(-8, 3)
        expected = '-2 2/3'
        self.assertEqual(f.mixed_number(), expected)
    
    def test_negative_mixed_number_2(self):
        f = Fraction(8, -3)
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
    
    def test_invert(self):
        f1 = Fraction(2, 3)
        expected = Fraction(3, 2)
        self.assertEqual(~f1, expected)
    
    def test_invert_negative(self):
        f1 = Fraction(-2, 3)
        expected = Fraction(-3, 2)
        self.assertEqual(~f1, expected)
    
    def test_add_1(self):
        f1 = Fraction(5, 2)
        f2 = Fraction(13, 4)
        expected = Fraction(23, 4)
        self.assertEqual(f1 + f2, expected)
    
    def test_add_2(self):
        f1 = Fraction(5, 9)
        f2 = Fraction(1, 3)
        expected = Fraction(8, 9)
        self.assertEqual(f1 + f2, expected)

    def test_add_3(self):
        f1 = Fraction(10, 1)
        f2 = Fraction(4, 1)
        expected = Fraction(14, 1)
        self.assertEqual(f1 + f2, expected)
    
    def test_add_4(self):
        f1 = Fraction(-1, 2)
        f2 = Fraction(3, 2)
        expected = Fraction(1, 1)
        self.assertEqual(f1 + f2, expected)
    
    def test_add_5(self):
        f1 = Fraction(3, 4)
        f2 = Fraction(7, 10)
        f3 = Fraction(2, 5)
        expected = Fraction(37, 20)
        self.assertEqual(f1 + f2 + f3, expected)
    
    def test_subtract_1(self):
        f1 = Fraction(3, 6)
        f2 = Fraction(1, 6)
        expected = Fraction(2, 6)
        self.assertEqual(f1 - f2, expected)
    
    def test_subtract_2(self):
        f1 = Fraction(10, 11)
        f2 = Fraction(7, 11)
        expected = Fraction(3, 11)
        self.assertEqual(f1 - f2, expected)
    
    def test_subtract_3(self):
        f1 = Fraction(1, 3)
        f2 = Fraction(1, 6)
        expected = Fraction(1, 6)
        self.assertEqual(f1 - f2, expected)
    
    def test_subtract_4(self):
        f1 = Fraction(23, 24)
        f2 = Fraction(2, 3)
        expected = Fraction(7, 24)
        self.assertEqual(f1 - f2, expected)
    
    def test_subtract_5(self):
        f1 = Fraction(21, 28)
        f2 = Fraction(3, 4)
        expected = Fraction(0, 1)
        self.assertEqual(f1 - f2, expected)
    
    def test_subtract_6(self):
        f1 = Fraction(11, 8)
        f2 = Fraction(2, 3)
        expected = Fraction(17, 24)
        self.assertEqual(f1 - f2, expected)
    
    def test_multiply_1(self):
        f1 = Fraction(1, 3)
        f2 = Fraction(5, 1)
        expected = Fraction(5, 3)
        self.assertEqual(f1 * f2, expected)
    
    def test_multiply_2(self):
        f1 = Fraction(4, 7)
        f2 = Fraction(5, 6)
        expected = Fraction(20, 42)
        self.assertEqual(f1 * f2, expected)
    
    def test_multiply_3(self):
        f1 = Fraction(5, 4)
        f2 = Fraction(-4, 9)
        expected = Fraction(-5, 9)
        self.assertEqual(f1 * f2, expected)
    
    def test_multiply_4(self):
        f1 = Fraction(-5, 8)
        f2 = Fraction(4, 3)
        f3 = Fraction(8, -7)
        expected = Fraction(20, 21)
        self.assertEqual(f1 * f2 * f3, expected)
    
    def test_divide_1(self):
        f1 = Fraction(2, 3)
        f2 = Fraction(1, 2)
        expected = Fraction(4, 3)
        self.assertEqual(f1 / f2, expected)
    
    def test_divide_2(self):
        f1 = Fraction(2, 9)
        f2 = Fraction(3, 10)
        expected = Fraction(20, 27)
        self.assertEqual(f1 / f2, expected)
    
    def test_divide_3(self):
        f1 = Fraction(13, 9)
        f2 = Fraction(3, 5)
        expected = Fraction(65, 27)
        self.assertEqual(f1 / f2, expected)
    
    def test_divide_4(self):
        f1 = Fraction(1, 7)
        f2 = Fraction(3, 4)
        expected = Fraction(4, 21)
        self.assertEqual(f1 / f2, expected)
    
    def test_less_than(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(3, 2)
        self.assertTrue(f1 < f2)
    
    def test_greater_than(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(3, 2)
        self.assertTrue(f2 > f1)
    
    def test_greater_or_equal(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 2)
        self.assertTrue(f1 <= f2)
    
    def test_less_than_or_equal(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 2)
        self.assertTrue(f1 >= f2)

if __name__ == '__main__':
    unittest.main()
