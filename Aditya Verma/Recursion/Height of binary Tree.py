"""height of binary tree"""
"""


gives height of tree  ----  height(root)
gives height of left sub tree height(root-left)
gives height of right sub tree height(root-right)

induction
    right have height of right subtree
    left have height of left subtree

    then we will return maximumof both
    adding height of current
    so it will return 1 + max(right,left)

    what will be the smallest height it will be null\


"""

class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None



def height(tree):
    if tree == None:
        return 0
    left = height(tree.left)
    right = height(tree.right)

    return 1 + max(left, right)

root = node(10)
r = node(20)
l = node(30)
rr = node(40)
rl = node(50)
ll = node(60)
lr = node(70)
lll = node(80)
root.left = l
root.right = r
r.right = rr
l.left = ll
r.left = rl
l.right = lr
lr.left = lll

print(height(root))
    