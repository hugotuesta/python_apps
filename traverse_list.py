def count_leaf_items_recursively(item_list):
    count = 0
    for item in item_list:
        if isinstance(item, list):
            count += count_leaf_items_recursively(item)
        else:
            count += 1
    
    return count

def count_leaf_items_non_recursively(item_list):
    count = 0
    stack = []
    current_list = item_list
    i = 0
    
    while True:
        if i == len(current_list):
            if current_list == item_list:
                return count
            else:
                current_list, i = stack.pop()
                i += 1
                continue

        if isinstance(current_list[i], list):
            stack.append([current_list, i])
            current_list = current_list[i]
            i = 0
        else:
            count += 1
            i += 1

names = ['Adam', ['Bob', ['Chet', 'Cat'], 'Barb', 'Bert'], 'Alex', ['Bea', 'Bill'], 'Ann']

print(count_leaf_items_recursively([1, 2, 3, 4]))
print(count_leaf_items_recursively([1, [2.1, 2.2], 3]))
print(count_leaf_items_recursively([]))
print(count_leaf_items_recursively(names))

print(count_leaf_items_non_recursively([1, 2, 3, 4]))
print(count_leaf_items_non_recursively([1, [2.1, 2.2], 3]))
print(count_leaf_items_non_recursively([]))
print(count_leaf_items_non_recursively(names))
