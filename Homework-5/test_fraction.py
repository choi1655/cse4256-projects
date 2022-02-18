
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
    
    def test_mixed_number_simplify_and_leftover(self):
        f = fraction.Fraction(8, 3)
        expected = '2 2/3'
        self.assertEqual(f.mixed_number(), expected)

if __name__ == '__main__':
    unittest.main()
