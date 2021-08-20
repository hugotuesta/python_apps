# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None

def kth_smallest_in_BST(t, k):
    def in_order(node):
        if node:
            yield from in_order(node.left)
            yield node.value
            yield from in_order(node.right)
            
    elements = in_order(t)
    
    for _ in range(k):
        element = next(elements)
    
    return element
