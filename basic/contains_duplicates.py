def contains_duplicates(a):
    return len(a) != len(list(set(a)))

print(contains_duplicates([1, 2, 3, 1]))
print(contains_duplicates([3, 1]))
