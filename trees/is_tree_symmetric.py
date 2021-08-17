#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None

def isTreeSymmetric(t):
    return solve(t, t)
    
def solve(node1, node2):
    if not node1 and not node2:
        return True
    if not node1 or not node2:
        return False
    
    return node1.value == node2.value and solve(node1.left, node2.right) and solve(node1.right, node2.left)
