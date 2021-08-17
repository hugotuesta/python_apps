def contains_close_nums(nums, k):
    enum = list(enumerate(nums))
    indices = {}
    
    for item in enum:
        if item[1] in indices:
            indices[item[1]].append(item[0])
            indices_list = indices[item[1]]
            difference = abs(indices_list[len(indices_list)-1] - indices_list[len(indices_list)-2])
            if difference <= k:
                return True
        else:
            indices[item[1]] = [item[0]]
    
    return False

print(contains_close_nums([0, 1, 2, 3, 5, 2], 3))
print(contains_close_nums([0, 1, 2, 3, 5, 2], 2))
