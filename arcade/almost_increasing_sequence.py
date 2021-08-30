def almost_increasing_sequence(sequence):
    removed_one = False
    prev_maxval = None
    maxval = None
    for s in sequence:
        if not maxval or s > maxval:
            prev_maxval = maxval
            maxval = s
        elif not prev_maxval or s > prev_maxval:
            if removed_one:
                return False
            removed_one = True
            maxval = s
        else:
            if removed_one:
                return False
            removed_one = True
    return True

print(almost_increasing_sequence([1, 3, 2]))
