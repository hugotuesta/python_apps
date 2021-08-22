# Singly-linked lists are already defined with this interface:
class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None

def show_list(linked_list):
    elements = []
    current = linked_list
    
    while current:
        elements.append(current.value)
        current = current.next

    return elements

def removeKFromList(l, k):  
    current = l

    while current:
        if current.next and current.next.value == k:
            current.next = current.next.next
        else:
            current = current.next

    return l.next if l and l.value == k else l

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

l1 = ListNode(3)
l1.next = ListNode(1)
l1.next.next = ListNode(2)
l1.next.next.next = ListNode(3)
l1.next.next.next.next = ListNode(4)
l1.next.next.next.next.next = ListNode(5)

ll1 = removeKFromList(l1, 3)
print(show_list(ll1))

l2 = ListNode(2)
l2.next = ListNode(3)
l2.next.next = ListNode(4)
l2.next.next.next = ListNode(5)
l2.next.next.next.next = ListNode(6)
l2.next.next.next.next.next = ListNode(7)

ll2 = removeKFromList(l2, 10)
print(show_list(ll2))
