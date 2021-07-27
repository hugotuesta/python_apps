def is_palindrome1(word):
    word = word.lower()
    return word == word[::-1]

def is_palindrome2(word):
    word = word.lower()
    if len(word) <= 1:
        return True
    else:
        return word[0] == word[-1] and is_palindrome2(word[1:-1])

print(is_palindrome1(''))
print(is_palindrome1('r'))
print(is_palindrome1('raceCar'))
print(is_palindrome1('troglodyte'))

print(is_palindrome2(''))
print(is_palindrome2('r'))
print(is_palindrome2('raceCar'))
print(is_palindrome2('troglodyte'))