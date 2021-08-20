def find_profession(level, pos):
    if level == 1:
        return 'Engineer'
        
    if pos % 2 != 0:
        return findProfession(level-1, (pos + 1)//2)
    else:
        if (findProfession(level-1, pos//2)) == 'Doctor':    
            return 'Engineer'
        else:
            return 'Doctor'
