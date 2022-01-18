
import unittest
import solution

class TestSolution(unittest.TestCase):

    def test_fiblist_5(self):
        expected_list = [1, 1, 2, 3, 5]
        actual_list = solution.fiblist(5)
        self.assertEqual(expected_list, actual_list)
    
    def test_fiblist_10(self):
        expected_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
        actual_list = solution.fiblist(10)
        self.assertEqual(expected_list, actual_list)

    def test_fiblist_0(self):
        actual_list = solution.fiblist(0)
        self.assertTrue(len(actual_list) == 0)

    def test_fiblist_1(self):
        expected_list = [1]
        actual_list = solution.fiblist(1)
        self.assertEqual(expected_list, actual_list)

    def test_fiblist_2(self):
        expected_list = [1, 1]
        actual_list = solution.fiblist(2)
        self.assertEqual(expected_list, actual_list)


if __name__ == "__main__":
    unittest.main()