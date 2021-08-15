import unittest
from contains_duplicates import contains_duplicates

class TestContainsDuplicates(unittest.TestCase):

    def test_contains_duplicates(self):
        self.assertEqual(contains_duplicates([1, 2, 3, 1]), True)
    
    def test_does_not_contains_duplicates(self):
        self.assertEqual(contains_duplicates([3, 1]), False)

if __name__ == '__main__':
    unittest.main()
