import pytest
from add_border import add_border
from alternating_sums import alternating_sums
from are_similar import are_similar
from array_change import array_change
from palindrome_rearranging import palindrome_rearranging

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

def test_array_change_01():
    expected_result = 3
    test_result = array_change([1, 1, 1])
    assert test_result == expected_result

def test_array_change_02():
    expected_result = 5
    test_result = array_change([-1000, 0, -2, 0])
    assert test_result == expected_result

def test_array_change_02():
    expected_result = 25559
    test_result = array_change([3122, -645, 2616, 13213, -8069])
    assert test_result == expected_result

def test_array_change_04():
    expected_result = 737073
    test_result = array_change([9796, 1283, -2825, 3870, -6727, -8616, -10191, -7727, 7074, 1580, -4583, 162, 2980, -3861, 9452, 8145, 1222, -1125, 5142, -5657, -974, -986, -9627, 5244, 8866, 3336, -9946, -5271, 10582, 3013, 8030, 4471, -3420, 9496, -3533, -8030, 10007, 2549, -8195, 7119, 302, -5322, -3537, 209, -8134, -9176, 6336, -1771, 9851, 3644, 9629, -2603, 3988, 10579, 2221, 1101, 1465, 5002, -6203, -8864, 596, 6005, 4554, 8526, 2178, -5447, -232, -9734, 7402, -3984, -7161, -2139, -3181, 10445, 4535, 6926, 7156])
    assert test_result == expected_result

def test_palindrome_rearranging_01():
    test_result = palindrome_rearranging('aabb')
    assert test_result == True

def test_palindrome_rearranging_02():
    test_result = palindrome_rearranging('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaabc')
    assert test_result == False

def test_palindrome_rearranging_03():
    test_result = palindrome_rearranging('abbcabb')
    assert test_result == True

def test_palindrome_rearranging_04():
    test_result = palindrome_rearranging('abdhuierf')
    assert test_result == False
