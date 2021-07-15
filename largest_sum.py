# Take an array with positive and negative integers and
# find the maximum continuous sum of that array

def largest_sum(array):
    if len(array) == 0:
        return print('Too small')
    
    max_sum = current_sum = array[0]

    for num in array[1:]:
        current_sum = max(current_sum + num, num)
        max_sum = max(current_sum, max_sum)

    return print(max_sum)

largest_sum([7,1,2,-1,3,4,10,-12,3,21,-19])
largest_sum([1,3,5,-1,4,-7])
