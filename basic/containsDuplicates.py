def containsDuplicates(a):
    return len(a) != len(list(set(a)))

print(containsDuplicates([1, 2, 3, 1]))
print(containsDuplicates([3, 1]))
