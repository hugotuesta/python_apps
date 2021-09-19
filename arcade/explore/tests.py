import pytest
from add_border import add_border
from alternating_sums import alternating_sums

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
