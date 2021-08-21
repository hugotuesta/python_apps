import unittest
from contains_duplicates import contains_duplicates
from sum_of_two import sum_of_two
from sum_in_range import sum_in_range

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

class TestSumInRange(unittest.TestCase):

    def test_positives_and_negatives(self):
        test_result = sum_in_range(nums=[3, 0, -2, 6, -3, 2], queries=[[0,2], [2,5], [0,5]])
        self.assertEqual(10, test_result)
    
    def test_all_positives(self):
        test_result = sum_in_range(nums=[34, 19, 21, 5, 1, 10, 26, 46, 33, 10], queries=[[3,7], [3,4], [3,7], [4,5], [0,5]])
        self.assertEqual(283, test_result)

    def test_all_negatives(self):
        test_result = sum_in_range(nums=[-4, -18, -22, -14, -33, -47, -29, -35, -50, -19], queries=[[2,9], [5,6], [1,2], [2,2], [4,5]])
        self.assertEqual(999999540, test_result)

if __name__ == '__main__':
    unittest.main()
