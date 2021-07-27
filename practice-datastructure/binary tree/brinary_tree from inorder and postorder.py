class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def createtree(inorder, postorder):
    if inorder == []:
        return None
    x = postorder[-1]
    node = Node(x)
    if len(inorder) == 1:
        return node
    x_range = 0
    for i in range(len(inorder)):
        if inorder[i] == x:
            x_range = i
            break
    l_inorder = inorder[:x_range]
    r_inorder = inorder[x_range+1:]
    l_postorder = postorder[:x_range]
    r_postorder = postorder[x_range:-1]
    node.left = createtree(l_inorder, l_postorder)
    node.right = createtree(r_inorder, r_postorder)
    return node

def inorder_traversal(root):
    if root == None:
        return
    inorder_traversal(root.left)
    print(root.data, end=" ")
    inorder_traversal(root.right)
    return


inorder = [4, 2, 5, 1, 6, 3]
postorder = [4, 5, 2, 6, 3, 1]

root = createtree(inorder, postorder)

inorder_traversal(root)

