import pytest
from sort_by_height import sort_by_height

def test_sort_by_height_standard_forest():
    expected_result = [-1, 150, 160, 170, -1, -1, 180, 190]
    test_result = sort_by_height([-1, 150, 190, 170, -1, -1, 160, 180])

    assert test_result == expected_result

def test_sort_by_height_only_trees():
    expected_result = [-1, -1, -1, -1, -1]
    test_result = sort_by_height([-1, -1, -1, -1, -1])

    assert test_result == expected_result

def test_sort_by_height_one_tree():
    expected_result = [-1]
    test_result = sort_by_height([-1])

    assert test_result == expected_result

def test_sort_by_height_only_people():
    expected_result = [2, 2, 4, 9, 11, 16]
    test_result = sort_by_height([4, 2, 9, 11, 2, 16])

    assert test_result == expected_result
