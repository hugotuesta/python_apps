# Binary trees are already defined with this interface:
class Tree(object):
  def __init__(self, x):
    self.value = x
    self.left = None
    self.right = None

def hasPathWithGivenSum(t, s):
    result = False

    if t is None:
       return False
       
    sub_sum = s - t.value
    if sub_sum == 0 and not t.left and  not t.right:
        return True
    
    if t.right:
        result = result or hasPathWithGivenSum(t.right, sub_sum)
    if t.left:
        result = result or hasPathWithGivenSum(t.left, sub_sum)

    return result

s = 21
root = Tree(10)
root.left = Tree(8)
root.right = Tree(2)
root.left.right = Tree(5)
root.left.left = Tree(3)
root.right.left = Tree(2)

print(hasPathWithGivenSum(root, s))
