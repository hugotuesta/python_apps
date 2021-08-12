# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
import math

def addTwoHugeNumbers_with_lists(a, b):
    size = 4
    text_a = get_text(a)
    text_b = get_text(b)
    
    number_a = int(''.join([str(n).rjust(size,'0') for n in text_a]))
    number_b = int(''.join([str(n).rjust(size,'0') for n in text_b]))
    
    result = number_a + number_b
    result_text = str(result)

    response = []
    limit = math.ceil(len(result_text)/size)
    for i in range(limit):
        response.append(int(result_text[-(i+1)*size:-i*size if i != 0 else None]))
    return response[::-1]
    
    
def get_text(node):
    current = node
    text = []
    while current:
        text.append(current.value)
        current = current.next
    return text
