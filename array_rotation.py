"""
Given 2 lists (assume duplicates are rotations)
list2 is a rotation of list1
They have the same size and elements but start index is differente
"""

def rotation(list1, list2):
    if len(list1) != len(list2):
        return False

    key = list1[0]
    index = 0

    for i in range(len(list2)):
        if list2[i] == key:
            index = i
            break
    
    for j in range(len(list1)):
        i2 = (index + j) % len(list1)
        if list1[j] != list2[i2]:
            return False

    return True

print(rotation([1,2,3,4,5,6,7], [5,6,7,1,2,3,4]))
print(rotation([1,2,3,4,5], [3,4,5,1,6]))
print(rotation([1,2,3,4,5,6], [1,2,3,4,5,6]))
print(rotation([1,2,3,4,5,6], [3,4,5,6,1]))
print(rotation([1,2,3,4,5,6,7], [3,4,5,6,7,1,2]))
print(rotation([1,2,3], [4,5,6]))
