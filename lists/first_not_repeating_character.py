def firstNotRepeatingCharacter(s):
    quantity = {}
    
    for letter in s:
        if letter in quantity:
            quantity[letter] += 1
        else:
            quantity[letter] = 1
    
    for letter in s:
        if quantity[letter] == 1:
            return letter
    
    return '_'

print(firstNotRepeatingCharacter('abacabad'))
print(firstNotRepeatingCharacter('bcb'))
print(firstNotRepeatingCharacter('ngrhhqbhnsipkcoqjyviikvxbxyphsnjpdxkhtadltsuxbfbrkof'))
