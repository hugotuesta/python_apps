def add_border(picture):
    row = len(picture)
    col = len(picture[0])
    
    border = '*' * (col + 2)
    
    rectangle = []
    rectangle.append(border)
    
    for item in picture:
        rectangle.append('*' + item + '*')
    rectangle.append(border)
    
    return rectangle

print(add_border(["abc", "ded"]))
print(add_border(["abcde", "fghij", "klmno", "pqrst", "uvwxy"]))
print(add_border(["wzy**"]))
