def isCryptSolution(crypt, solution):
    mapping = {item[0]:item[1] for item in solution}
    first_number = ''.join([mapping[letter] for letter in crypt[0]])
    second_number = ''.join([mapping[letter] for letter in crypt[1]])
    result_number = ''.join([mapping[letter] for letter in crypt[2]])

    if not is_valid(first_number) or not is_valid(second_number) or not is_valid(result_number):
        return False
    else:
        return int(first_number) + int(second_number) == int(result_number)

def is_valid(number):
    return len(number) == 1 or (len(number) > 1 and number[0] != '0')

print(isCryptSolution(["SEND", "MORE", "MONEY"], [['O', '0'],
            ['M', '1'],
            ['Y', '2'],
            ['E', '5'],
            ['N', '6'],
            ['D', '7'],
            ['R', '8'],
            ['S', '9']]))
print(isCryptSolution(["TEN", "TWO", "ONE"], [['O', '1'],
            ['T', '0'],
            ['W', '9'],
            ['E', '5'],
            ['N', '4']]))
print(isCryptSolution(["A", "A", "A"], [["A","0"]]))
