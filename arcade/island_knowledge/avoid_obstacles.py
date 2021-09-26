def avoid_obstacles(inputArray):
    ordered = sorted(inputArray)   
    maximum = max(ordered) + 1
    number = maximum
    result = []
    
    while number > 0 and number <= maximum:
        can_be_added = True
        for i in range(0, maximum, number):
            if i in ordered:
                can_be_added = False
                break
        if can_be_added:
            result.append(number)
        number -= 1
        
    return min(result)

print(avoid_obstacles([5, 3, 6, 7, 9])) # 4
print(avoid_obstacles([2, 3])) # 4
print(avoid_obstacles([1000, 999])) # 6
print(avoid_obstacles([19, 32, 11, 23])) # 3
