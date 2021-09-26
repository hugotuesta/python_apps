def is_ipv4_address(inputString):
    items = inputString.split('.')
    filtered = [item == '' or (item.lstrip('0') != item and len(item) > 1) or not item.isdigit() or int(item) > 255 for item in items]
   
    return len(items) == 4 and not any(filtered)

print(is_ipv4_address('172.16.254.1')) # True
print(is_ipv4_address('172.316.254.1')) # False
print(is_ipv4_address('1.1.1.1a')) # False
print(is_ipv4_address('.254.255.0')) # False
print(is_ipv4_address('1.23.256..')) # False
print(is_ipv4_address('0.254.255.0')) # True
