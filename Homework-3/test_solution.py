
import solution
import unittest

class Person:
    def __init__(self, name) -> None:
        self.name = name
            
    def __eq__(self, __o: object) -> bool:
        return self.name == __o.name
    
    def __hash__(self) -> int:
        return hash(self.name)
        
        
class TestSolution(unittest.TestCase):

    def test_all_unique_numbers_unique(self):
        input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        expected_result = solution.all_unique(input_list)

        self.assertTrue(expected_result)
    
    def test_all_unique_numbers_duplicate(self):
        input_list = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9]
        expected_result = solution.all_unique(input_list)

        self.assertFalse(expected_result)

    def test_all_unique_elements_unique(self):
        person1 = Person('A')
        person2 = Person('B')
        person3 = Person('C')
        person4 = Person('D')
        input_list = [person1, person2, person3, person4]
        expected_result = solution.all_unique(input_list)
        self.assertTrue(expected_result)
    
    def test_all_unique_elements_duplicate(self):
        person1 = Person('A')
        person2 = Person('B')
        person3 = Person('A')
        person4 = Person('D')
        input_list = [person1, person2, person3, person4]
        expected_result = solution.all_unique(input_list)
        self.assertFalse(expected_result)

    def test_apply_all(self):
        input_set = {1, 3, 5, 7, 9}
        expected_set = {6, 8, 10, 12, 14}

        solution.apply_all(input_set)
        self.assertEqual(input_set, expected_set)

if __name__ == '__main__':
    unittest.main()