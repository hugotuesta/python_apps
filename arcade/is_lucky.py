def is_lucky(n):
    string_n = str(n)
    first_half = sum([int(i) for i in string_n[:len(string_n)//2]])
    second_half = sum([int(i) for i in string_n[len(string_n)//2:]])
   
    return first_half == second_half

print(is_lucky(1230))
print(is_lucky(134008))
print(is_lucky(261534))
print(is_lucky(261531))
