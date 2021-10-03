import pytest
from array_maximal_adjacent_difference import array_maximal_adjacent_difference
from avoid_obstacles import avoid_obstacles
from is_ipv4_address import is_ipv4_address

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

def test_array_maximal_adjacent_difference_04():
    expected_result = array_maximal_adjacent_difference([-5, 3, 6, 13, -2])
    test_result = 15

    assert test_result == expected_result

def test_avoid_obstacles_01():
    expected_result = avoid_obstacles([5, 3, 6, 7, 9])
    test_result = 4

    assert test_result == expected_result

def test_avoid_obstacles_02():
    expected_result = avoid_obstacles([2, 3])
    test_result = 4

    assert test_result == expected_result

def test_avoid_obstacles_03():
    expected_result = avoid_obstacles([1000, 999])
    test_result = 6

    assert test_result == expected_result

def test_avoid_obstacles_04():
    expected_result = avoid_obstacles([19, 32, 11, 23])
    test_result = 3

    assert test_result == expected_result

def test_is_ipv4_address_01():
    expected_result = is_ipv4_address('172.16.254.1')
    test_result = True

    assert test_result == expected_result

def test_is_ipv4_address_02():
    expected_result = is_ipv4_address('172.316.254.1')
    test_result = False

    assert test_result == expected_result

def test_is_ipv4_address_03():
    expected_result = is_ipv4_address('1.1.1.1a')
    test_result = False

    assert test_result == expected_result

def test_is_ipv4_address_04():
    expected_result = is_ipv4_address('.254.255.0')
    test_result = False

    assert test_result == expected_result

def test_is_ipv4_address_05():
    expected_result = is_ipv4_address('1.23.256..')
    test_result = False

    assert test_result == expected_result

def test_is_ipv4_address_06():
    expected_result = is_ipv4_address('0.254.255.0')
    test_result = True

    assert test_result == expected_result

def test_is_ipv4_address_07():
    expected_result = is_ipv4_address('1.255.55.00')
    test_result = False

    assert test_result == expected_result
