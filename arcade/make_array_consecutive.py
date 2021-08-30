def make_array_consecutive2(statues):
    maximum = max(statues)
    minimum = min(statues)
    
    complete = set(range(minimum, maximum + 1))
    statuses = set(statues)
    
    return len(complete - statuses)

print(make_array_consecutive2([6, 2, 3, 8]))
