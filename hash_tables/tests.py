import unittest
from are_following_patterns import are_following_patterns
from grouping_dishes import grouping_dishes
from contains_close_nums import contains_close_nums

class TestAreFollowingPattern(unittest.TestCase):

    def test_match_pattern(self):
        self.assertEqual(are_following_patterns(["cat", "dog", "dog"], ["a", "b", "b"]), True)

    def test_does_not_match_pattern(self):
        self.assertEqual(are_following_patterns(["cat", "dog", "doggy"], ["a", "b", "b"]), False)

class TestGroupingDishes(unittest.TestCase):

    def test_first_group(self):
        expected_result = [['Cheese', 'Quesadilla', 'Sandwich'], 
                           ['Salad', 'Salad', 'Sandwich'], 
                           ['Sauce', 'Pizza', 'Quesadilla', 'Salad'], 
                           ['Tomato', 'Pizza', 'Salad', 'Sandwich']]

        test_result = grouping_dishes([["Salad", "Tomato", "Cucumber", "Salad", "Sauce"],
                                       ["Pizza", "Tomato", "Sausage", "Sauce", "Dough"],
                                       ["Quesadilla", "Chicken", "Cheese", "Sauce"],
                                       ["Sandwich", "Salad", "Bread", "Tomato", "Cheese"]])

        self.assertEqual(test_result, expected_result)

    def test_second_group(self):
        expected_result = [['Cheese', 'Quesadilla', 'Sandwich'], 
                           ['Chicken', 'Chicken Curry', 'Quesadilla'], 
                           ['Nuts', 'Fried Rice', 'Salad'], 
                           ['Onions', 'Fried Rice', 'Pasta']]

        test_result = grouping_dishes([["Pasta", "Tomato Sauce", "Onions", "Garlic"],
                                       ["Chicken Curry", "Chicken", "Curry Sauce"],
                                       ["Fried Rice", "Rice", "Onions", "Nuts"],
                                       ["Salad", "Spinach", "Nuts"],
                                       ["Sandwich", "Cheese", "Bread"],
                                       ["Quesadilla", "Chicken", "Cheese"]])

        self.assertEqual(test_result, expected_result)

class TestContainsCloseNums(unittest.TestCase):

    def test_first_case(self):
        self.assertEqual(contains_close_nums([0, 1, 2, 3, 5, 2], 3), True)

    def test_second_case(self):
        self.assertEqual(contains_close_nums([0, 1, 2, 3, 5, 2], 2), False)

if __name__ == '__main__':
    unittest.main()

# python -m unittest -v tests
