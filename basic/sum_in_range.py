from itertools import accumulate

def sum_in_range(nums, queries):
    cumulative = list(accumulate(nums))

    partial = []
    for query in queries:
        if query[0] == 0:
            partial.append(cumulative[query[1]])
        else:
            partial.append(cumulative[query[1]] - cumulative[query[0]-1])
    
    return sum(partial) % (10**9 + 7)

print(sum_in_range(nums=[3, 0, -2, 6, -3, 2], queries=[[0,2], [2,5], [0,5]]))
