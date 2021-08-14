def areFollowingPatterns(strings, patterns):
    mapping = {}
    for i in range(len(patterns)):
        if patterns[i] not in mapping:
            if strings[i] not in mapping.values():
                mapping[patterns[i]] = strings[i]
            else:
                return False
        else:
            if mapping[patterns[i]] != strings[i]:
                return False
    
    return True

print(areFollowingPatterns(["cat", "dog", "dog"], ["a", "b", "b"]))
print(areFollowingPatterns(["cat", "dog", "doggy"], ["a", "b", "b"]))
