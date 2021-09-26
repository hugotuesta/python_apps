def array_maximal_adjacent_difference(inputArray):
    max_diff = 0
    for i in range(len(inputArray) - 1):
        diff = abs(inputArray[i] - inputArray[i+1])
        max_diff = max(max_diff, diff)
    
    return max_diff

print(array_maximal_adjacent_difference([2, 4, 1, 0])) # 3
print(array_maximal_adjacent_difference([1, 1, 1, 1])) # 0
print(array_maximal_adjacent_difference([-1, 4, 10, 3, -2])) # 7
