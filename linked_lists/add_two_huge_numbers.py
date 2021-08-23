# Singly-linked lists are already defined with this interface:
class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None

import math

def add_two_huge_numbers_with_lists(a, b):
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

def add_two_huge_numbers_with_linked_lists(a, b):
    list_a = reverse(a)
    list_b = reverse(b)
    
    carry = 0
    result = None
    
    while list_a or list_b or carry > 0:
        partial_sum = ((list_a.value if list_a else 0) + 
                      (list_b.value if list_b else 0) + 
                      carry)
                
        node = ListNode(partial_sum % 10000)
        node.next = result
        
        result = node
        carry = partial_sum // 10000
        
        if list_a:
            list_a = list_a.next
        if list_b:
            list_b = list_b.next
            
    return result
    
def reverse(linked_list):
    current = linked_list
    previous = None
    
    while current is not None:
        previous, current.next, current = current, previous, current.next
        
    return previous
