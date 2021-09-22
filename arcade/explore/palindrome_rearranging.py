def palindrome_rearranging(inputString):
    count = len(inputString)
    elements = {}
    for item in inputString:
        if item in elements:
            elements[item] += 1
        else:
            elements[item] = 1
            
    odd = 0
    for item in elements:
        if count % 2 == 0:
            if elements[item] % 2 != 0:
                return False
        else:
            if elements[item] % 2 != 0:
                odd += 1
            if odd > 1:
                return False
            
    return True

print(palindrome_rearranging('aabb')) # True
print(palindrome_rearranging('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaabc')) # False
print(palindrome_rearranging('abbcabb')) # True
print(palindrome_rearranging('abdhuierf')) # False
