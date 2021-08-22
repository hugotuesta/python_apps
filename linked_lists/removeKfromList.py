# Singly-linked lists are already defined with this interface:
class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None

def removeKFromList(l, k):  
    previous = None
    current = l
    
    if current is None:
        return l
        
    while current is not None:
        if current.value == k and previous is None:
            l = current.next
            current = l
        elif current.value == k and previous is not None:
            next_item = current.next
            previous.next = next_item
            current = next_item
        else:
            previous = current
            current = current.next  

    return l

def remove_k_from_list(l, k):  
    dummy = ListNode(0)
    tail = dummy
    
    while True:
        if not l:
            tail.next = None
            break
            
        if l.value != k:
            tail.next = l
            tail = tail.next
        
        l = l.next
    
    return dummy.next
