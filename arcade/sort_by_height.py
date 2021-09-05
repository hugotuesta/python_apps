def sort_by_height(a):
    heights = sorted([item for item in a if item != -1])
       
    new = []
    counter = 0
    for i in range(len(a)):
        if a[i] == -1:
            new.append(a[i])
        else:
            new.append(heights[counter])
            counter += 1
    
    return new

print(sort_by_height([-1, 150, 190, 170, -1, -1, 160, 180]))
print(sort_by_height([-1, -1, -1, -1, -1]))
print(sort_by_height([-1]))
print(sort_by_height([4, 2, 9, 11, 2, 16]))
