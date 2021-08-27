def adjacent_elements_product(inputArray):
    maxProduct = None
    for i in range(len(inputArray) - 1):          
        currentProduct = inputArray[i] * inputArray[i+1]
        if i == 0:
            maxProduct = currentProduct
        if currentProduct > maxProduct:
            maxProduct = currentProduct
    
    return maxProduct

print(adjacent_elements_product([3, 6, -2, -5, 7, 3])) # 21
print(adjacent_elements_product([-23, 4, -3, 8, -12])) # -12
print(adjacent_elements_product([5, 1, 2, 3, 1, 4])) # 6