
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

    def test_ispartitionable_1(self):
        list = [1, 2, 3, 2, 4]
        self.assertTrue(solution.ispartitionable(list))
    
    def test_ispartitionable_2(self):
        list = [1, 2, 3, 4, 5]
        self.assertFalse(solution.ispartitionable(list))

    def test_ispartitionable_3(self):
        list = [1, 2, 3, 4, 10]
        self.assertTrue(solution.ispartitionable(list))

    def test_ispartitionable_4(self):
        list = [10, 2, 8]
        self.assertTrue(solution.ispartitionable(list))
    
    def test_vowelcount(self):
        value = 'aeiouDFGHAEghI'
        expected = 8
        self.assertEqual(solution.vowelcount(value), expected)
    
    def test_listfromcsv(self):
        inputVal = "5,8,hello,2\n9,14,world,1344"
        expected_list = [['5', '8', 'hello', '2'], ['9', '14', 'world', '1344']]
        self.assertEqual(solution.listfromcsv(inputVal), expected_list)



if __name__ == "__main__":
    unittest.main()