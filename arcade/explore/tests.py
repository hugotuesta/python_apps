import pytest
from add_border import add_border

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
