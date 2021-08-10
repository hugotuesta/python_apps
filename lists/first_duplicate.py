def firstDuplicate(a):
    list_set = set(a)
    
    if len(a) == len(list_set):
        return -1
    
    quantity = {}
    for letter in a:
        if letter in quantity:
            quantity[letter] += 1
        else:
            quantity[letter] = 1

    minimum_index = 10**5
    for k, v in quantity.items():
        if v > 1:
            current_index = a.index(k, a.index(k) + 1)
            if current_index < minimum_index:
                minimum_index = current_index
    
    return a[minimum_index]

print(firstDuplicate([2, 1, 3, 5, 3, 2]))
print(firstDuplicate([5, 5, 5, 5, 5]))
print(firstDuplicate([8, 4, 6, 2, 6, 4, 7, 9, 5, 8]))
