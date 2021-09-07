import pytest
from sort_by_height import sort_by_height
from matrix_element_sum import matrix_elements_sum

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

def test_matrix_elements_sum_case_1():
    expected_result = 9
    test_result = matrix_elements_sum([[0,1,1,2], [0,5,0,0], [2,0,3,3]])

    assert test_result == expected_result

def test_matrix_elements_sum_case_2():
    expected_result = 9
    test_result = matrix_elements_sum([[1,1,1,0], [0,5,0,1], [2,1,3,10]])

    assert test_result == expected_result

def test_matrix_elements_sum_case_3():
    expected_result = 6
    test_result = matrix_elements_sum([[1], [5], [0], [2]])

    assert test_result == expected_result

def test_matrix_elements_sum_case_4():
    expected_result = 15
    test_result = matrix_elements_sum([[1,2,3,4,5]])

    assert test_result == expected_result
