def are_following_patterns(strings, patterns):
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

print(are_following_patterns(["cat", "dog", "dog"], ["a", "b", "b"]))
print(are_following_patterns(["cat", "dog", "doggy"], ["a", "b", "b"]))
