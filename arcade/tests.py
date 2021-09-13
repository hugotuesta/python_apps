import pytest
from adjacent_elements_product import adjacent_elements_product
from all_longest_strings import all_longest_strings
from almost_increasing_sequence import almost_increasing_sequence
from common_character_count import common_character_count
from is_lucky import is_lucky
from make_array_consecutive import make_array_consecutive
from matrix_element_sum import matrix_elements_sum
from reverse_in_parentheses import reverse_in_parentheses
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

def test_is_lucky_four_digit():
    test_result = is_lucky(1230)

    assert test_result == True

def test_is_lucky_six_digit():
    test_result = is_lucky(134008)

    assert test_result == True

def test_is_not_lucky_six_digit():
    test_result = is_lucky(261534)

    assert test_result == False

def test_is_lucky_six_digit_two():
    test_result = is_lucky(261531)

    assert test_result == True

def test_common_character_count():
    test_result = common_character_count('aabcc', 'adcaa')

    assert test_result == 3

def test_adjacent_elements_product_01():
    test_result = adjacent_elements_product([3, 6, -2, -5, 7, 3])

    assert test_result == 21

def test_adjacent_elements_product_02():
    test_result = adjacent_elements_product([-23, 4, -3, 8, -12])

    assert test_result == -12

def test_adjacent_elements_product_03():
    test_result = adjacent_elements_product([5, 1, 2, 3, 1, 4])

    assert test_result == 6

def test_almost_increasing_sequence():
    test_result = almost_increasing_sequence([1, 3, 2])

    assert test_result == True

def test_all_longest_strings_01():
    expected_result = ['aba', 'vcd', 'aba']
    test_result = all_longest_strings(['aba', 'aa', 'ad', 'vcd', 'aba'])

    assert test_result == expected_result

def test_all_longest_strings_02():
    expected_result = ['aokbcwthc']
    test_result = all_longest_strings(['onsfnib', 'aokbcwthc', 'jrfcw'])

    assert test_result == expected_result

def test_make_array_consecutive_01():
    test_result = make_array_consecutive([6, 2, 3, 8])

    assert test_result == 3

def test_make_array_consecutive_02():
    test_result = make_array_consecutive([0, 3])

    assert test_result == 2

def test_make_array_consecutive_03():
    test_result = make_array_consecutive([5, 4, 6])

    assert test_result == 0

def test_make_array_consecutive_04():
    test_result = make_array_consecutive([6, 3])

    assert test_result == 2

def test_make_array_consecutive_05():
    test_result = make_array_consecutive([1])

    assert test_result == 0

def test_reverse_in_parentheses_01():
    expected_result = 'rab'
    test_result = reverse_in_parentheses('(bar)')

    assert test_result == expected_result

def test_reverse_in_parentheses_02():
    expected_result = 'foorabbaz'
    test_result = reverse_in_parentheses('foo(bar)baz')

    assert test_result == expected_result

def test_reverse_in_parentheses_03():
    expected_result = 'cbadgfe'
    test_result = reverse_in_parentheses('(abc)d(efg)')

    assert test_result == expected_result

def test_reverse_in_parentheses_04():
    expected_result = 'foobazrabblim'
    test_result = reverse_in_parentheses('foo(bar(baz))blim')

    assert test_result == expected_result

def test_reverse_in_parentheses_05():
    expected_result = ''
    test_result = reverse_in_parentheses('()')

    assert test_result == expected_result

def test_reverse_in_parentheses_06():
    expected_result = ''
    test_result = reverse_in_parentheses('')

    assert test_result == expected_result
