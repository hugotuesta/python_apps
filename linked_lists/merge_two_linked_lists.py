# Singly-linked lists are already defined with this interface:
class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None

def merge_two_linked_lists(l1, l2):
    dummy = ListNode(0)
    tail = dummy
    
    while True:
        if not l1:
            tail.next = l2
            break
        
        if not l2:
            tail.next = l1
            break
            
        if l1.value <= l2.value:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
            
        tail = tail.next
    
    return dummy.next


l1 = ListNode(1)
l1.next = ListNode(1)
l1.next.next = ListNode(2)
l1.next.next.next = ListNode(4)

l2 = ListNode(0)
l2.next = ListNode(3)
l2.next.next = ListNode(5)

l3 = merge_two_linked_lists(l1=l1, l2=l2)
merged_list = []

while l3:
    merged_list.append(l3.value)
    l3 = l3.next

print(merged_list)
