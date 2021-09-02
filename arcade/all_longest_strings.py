def all_longest_strings(inputArray):
    max_length = max([len(item) for item in inputArray])
    
    return [item for item in inputArray if len(item) == max_length]

print(all_longest_strings(['aba', 'aa', 'ad', 'vcd', 'aba']))
print(all_longest_strings(['onsfnib', 'aokbcwthc', 'jrfcw']))
