"""
Given a string, are all characters unique?
"""

def unique_characters1(string):
    string = string.replace(' ', '')
    return len(set(string)) == len(string)

def unique_characters2(string):
    string = string.replace(' ', '')
    count = {}

    for letter in string:
        if letter in count:
            return False
        else:
            count[letter] = 1

    return True

print(unique_characters1('qwerty'))
print(unique_characters1('asdfagda'))
print(unique_characters1('abcdce'))
print(unique_characters1('poiuyt'))
print(unique_characters1('a b cde'))
print('')
print(unique_characters2('qwerty'))
print(unique_characters2('asdfagda'))
print(unique_characters2('abcdce'))
print(unique_characters2('poiuyt'))
print(unique_characters2('a b cde'))
