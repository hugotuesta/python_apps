def reverse_in_parentheses(inputString):
    return eval('"' + inputString.replace('(', '"+("').replace(')', '")[::-1]+"') + '"')

print(reverse_in_parentheses('(bar)'))
print(reverse_in_parentheses('foo(bar)baz'))
print(reverse_in_parentheses('(abc)d(efg)'))
print(reverse_in_parentheses('foo(bar(baz))blim'))
print(reverse_in_parentheses('()'))
print(reverse_in_parentheses(''))
