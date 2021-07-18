"""
Common elements in two sorted lists (ascending order)
"""

def common_elements1(list1, list2):
    return [n for n in list1 if n in list2]

def common_elements2(list1, list2):
    i1 = i2 = 0
    common = []

    while i1 < len(list1) and i2 < len(list2):
        if list1[i1] == list2[i2]:
            common.append(list1[i1])
            i1 += 1
            i2 += 1
        elif list1[i1] < list2[i2]:
            i1 += 1
        else:
            i2 += 1
    
    return common


print(common_elements1([1,2,3,4,5], [1,3,5,7,9]))  # [1,3,5]
print(common_elements2([1,2,3,4,5], [1,3,5,7,9]))  # [1,3,5]

print(common_elements1([1,3,4,6,7,9], [1,2,4,5,9,10,12]))  # [1,4,9]
print(common_elements2([1,3,4,6,7,9], [1,2,4,5,9,10,12]))  # [1,4,9]
