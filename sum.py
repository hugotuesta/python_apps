def list_sum_regular(input_list):
    return sum(input_list)

def list_sum_recursive(input_list):
    if len(input_list) == 1:
        return input_list[0]
    else:
        head = input_list[0]
        small_list = input_list[1:]
        return head + list_sum_recursive(small_list)

numbers = [1,3,4,6,8]
print(list_sum_regular(numbers))
print(list_sum_recursive(numbers))
