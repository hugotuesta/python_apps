import unittest
from contains_duplicates import contains_duplicates
from sum_of_two import sum_of_two

class TestContainsDuplicates(unittest.TestCase):

    def test_contains_duplicates(self):
        self.assertEqual(contains_duplicates([1, 2, 3, 1]), True)
    
    def test_does_not_contains_duplicates(self):
        self.assertEqual(contains_duplicates([3, 1]), False)

class TestSumOfTwo(unittest.TestCase):

    def test_true_case(self):
        test_result = sum_of_two([1, 2, 3], [10, 20, 30, 40], 42)
        self.assertEqual(True, test_result)

    def test_false_case(self):
        test_result = sum_of_two([], [1, 2, 3, 4], 4)
        self.assertEqual(False, test_result)

if __name__ == '__main__':
    unittest.main()
