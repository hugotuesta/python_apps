import pytest
from add_border import add_border
from alternating_sums import alternating_sums
from are_similar import are_similar

def test_add_border_01():
    expected_result = ['*****', '*abc*', '*ded*', '*****']
    test_result = add_border(["abc", "ded"])

    assert test_result == expected_result

def test_add_border_02():
    expected_result = ['*******', '*abcde*', '*fghij*', '*klmno*', '*pqrst*', '*uvwxy*', '*******']
    test_result = add_border(["abcde", "fghij", "klmno", "pqrst", "uvwxy"])

    assert test_result == expected_result

def test_add_border_03():
    expected_result = ['*******', '*wzy***', '*******']
    test_result = add_border(["wzy**"])

    assert test_result == expected_result

def test_expected_result_01():
    expected_result = alternating_sums([50, 60, 60, 45, 70])
    test_result = [180, 105]
    assert test_result == expected_result

def test_expected_result_02():
    expected_result = alternating_sums([100, 50])
    test_result = [100, 50]
    assert test_result == expected_result

def test_expected_result_03():
    expected_result = alternating_sums([80])
    test_result = [80, 0]
    assert test_result == expected_result

def test_are_similar_01():
    expected_result = are_similar([1, 2, 3], [1, 2, 3])
    assert True == expected_result

def test_are_similar_02():
    expected_result = are_similar([2, 3, 1], [1, 3, 2])
    assert True == expected_result

def test_are_similar_03():
    expected_result = are_similar([4, 6, 3], [3, 4, 6])
    assert False == expected_result

def test_are_similar_04():
    expected_result = are_similar([832, 998, 148, 570, 533, 561, 894, 147, 455, 279], [832, 570, 148, 998, 533, 561, 455, 147, 894, 279])
    assert False == expected_result
