import pytest
from array_maximal_adjacent_difference import array_maximal_adjacent_difference

def test_array_maximal_adjacent_difference_01():
    expected_result = array_maximal_adjacent_difference([2, 4, 1, 0])
    test_result = 3

    assert test_result == expected_result

def test_array_maximal_adjacent_difference_02():
    expected_result = array_maximal_adjacent_difference([1, 1, 1, 1])
    test_result = 0

    assert test_result == expected_result

def test_array_maximal_adjacent_difference_03():
    expected_result = array_maximal_adjacent_difference([-1, 4, 10, 3, -2])
    test_result = 7

    assert test_result == expected_result
