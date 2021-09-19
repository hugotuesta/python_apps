def are_similar(a, b):  
    r = []
    for i in range(len(a)):
        if a[i] != b[i]:
            r.append(a[i])
            r.append(b[i])
    
    return len(r) < 5 and len(set(r)) < 3

print(are_similar([1, 2, 3], [1, 2, 3]))
print(are_similar([2, 3, 1], [1, 3, 2]))
print(are_similar([4, 6, 3], [3, 4, 6]))
print(are_similar([832, 998, 148, 570, 533, 561, 894, 147, 455, 279], [832, 570, 148, 998, 533, 561, 455, 147, 894, 279]))
