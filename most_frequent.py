"""
Given a list, what is the most frequently occurring element
"""

def most_frequent(list1):
    frequency = {}
    max_count = 0
    max_item = None

    for i in list1:
        if i in frequency:
            frequency[i] += 1
        else:
            frequency[i] = 1

        if frequency[i] > max_count:
            max_count = frequency[i]
            max_item = i
    
    return frequency, max_item, max_count

print(most_frequent([1,2,3,1,3,4,5,2,2,1,2,4]))
print(most_frequent([1,2,3,1,3,4,5]))
