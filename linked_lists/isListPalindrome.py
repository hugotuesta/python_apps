# Singly-linked lists are already defined with this interface:
class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None

def isListPalindrome(l):
    current = l 
    elements = []

    while current:
        elements.append(current.value)
        current = current.next
    
    return elements == elements[::-1]
