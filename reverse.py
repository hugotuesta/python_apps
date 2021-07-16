def reverse1(s):
    return ' '.join(s.split()[::-1])

def reverse2(s):
    length = len(s)
    words = []
    i = 0

    while i < length:
        if s[i] != ' ':
            word_start = i

            while i < length and s[i] != ' ':
                i += 1

            words.append(s[word_start:i])
        
        i += 1

    return ' '.join(reversed(words))

print(reverse1('This is the best'))
print(reverse2('This is the best'))
