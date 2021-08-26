# Singly-linked lists are already defined with this interface:
class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None

def reverse_nodes_in_k_groups(l, k):
    dummy = ListNode(0)
    dummy.next = l
    groupPrev = dummy
    
    while True:
        kth = get_kth(groupPrev, k)
        if not kth:
            break
        groupNext = kth.next
        
        previous, current = kth.next, groupPrev.next
        
        while current != groupNext:
            tmp = current.next
            current.next = previous
            previous = current
            current = tmp
        
        tmp = groupPrev.next
        groupPrev.next = kth
        groupPrev = tmp
        
    return dummy.next
    
def get_kth(current, k):
    while current and k > 0:
        current = current.next
        k -= 1
    
    return current
