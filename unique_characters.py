"""
Given a string, are all characters unique?
"""

def unique_characters1(string):
    string = string.replace(' ', '')
    return len(set(string)) == len(string)

def unique_characters2(string):
    string = string.replace(' ', '')
    characters = set()

    for letter in string:
        if letter in characters:
            return False
        else:
            characters.add(letter)

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
