def box_blur(image):
    size_row = len(image)
    #print(f'size_row: {size_row}')
    size_col = len(image[0])
    #print(f'size_col: {size_col}')
    new_rows, new_cols = size_row - 2, size_col - 2
    
    result = []
    for i in range(new_rows):
        result_row = []
        for j in range(new_cols):
            row_1 = [image[i][j], image[i][j+1], image[i][j+2]]
            row_2 = [image[i+1][j], image[i+1][j+1], image[i+1][j+2]]
            row_3 = [image[i+2][j], image[i+2][j+1], image[i+2][j+2]]

            #print(f'row_1: {row_1}')
            #print(f'row_2: {row_2}')
            #print(f'row_3: {row_3}')
            
            numerador = sum(row_1) + sum(row_2) + sum(row_3)
            denominador = 9

            #print(f'numerador: {numerador}')
            #print(f'denominador: {denominador}')

            #value = (sum(row_1) + sum(row_2) + sum(row_3))//(size_row * size_col)

            value = numerador // denominador
            
            result_row.append(value)
        
        result.append(result_row)  

    return result

print(box_blur([[1,1,1], [1,7,1], [1,1,1]])) # [[1]]
print(box_blur([[0,18,9], [27,9,0], [81,63,45]])) # [[28]]
print(box_blur([[36,0,18,9], [27,54,9,0], [81,63,72,45]])) # [[40,30]]
print(box_blur([[7,4,0,1], [5,6,2,2], [6,10,7,8], [1,4,2,0]])) # [[5,4], [4,4]]
# print(box_blur([[1,1,1], [1,7,1], [1,1,1]])) # 
