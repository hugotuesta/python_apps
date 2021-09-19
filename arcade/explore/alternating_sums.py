def alternating_sums(a):
    return [sum(a[::2]), sum(a[1::2])]

print(alternating_sums([50, 60, 60, 45, 70]))
print(alternating_sums([100, 50]))
print(alternating_sums([80]))
