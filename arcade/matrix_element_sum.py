def matrix_elements_sum(matrix):
    total_matrix = 0
    items = zip(*matrix)
    
    for row in items:
        for cell in row:
            if cell == 0:
                break
            total_matrix += cell
    
    return total_matrix

print(matrix_elements_sum([[0,1,1,2], [0,5,0,0], [2,0,3,3]]))
print(matrix_elements_sum([[1,1,1,0], [0,5,0,1], [2,1,3,10]]))
print(matrix_elements_sum([[1], [5], [0], [2]]))
print(matrix_elements_sum([[1,2,3,4,5]]))
