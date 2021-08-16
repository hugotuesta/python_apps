def sum_of_two(a, b, v):
    a = set([v - i for i in a])
    b = set(b)
        
    return len(a & b) > 0

print(sum_of_two([1, 2, 3], [10, 20, 30, 40], 42))
print(sum_of_two([], [1, 2, 3, 4], 4))
