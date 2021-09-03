def common_character_count(s1, s2):
    s1, s2 = list(s1), list(s2)
    common = []
    
    for item in s1:
        if item in s2:
            common.append(item)
            s2.remove(item)
            
    return len(common)

print(common_character_count('aabcc', 'adcaa'))
