"""
Non repeat element
Take a string and return character that never repeats 
if multiple uniques then return only the first unique
"""

def non_repeat_element(string):
    string = string.replace(' ', '')
    count = {}

    for letter in string:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    for letter in string:
        if count[letter] == 1:
            return letter
    
    return None

print(non_repeat_element('I Apple Ape Peels'))
