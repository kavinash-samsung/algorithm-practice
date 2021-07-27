Index = 0
Index_dict = {}

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def binary_tree_from_inorder_and_postorder(inorder, postorder):

    def create_tree(inorder, postorder, start, last):
        global Index, Index_dict
        if start>last:
            return None
        x = postorder[Index]
        node = Node(x)
        Index -= 1
        if start == last:
            return node
        curr_index = Index_dict[x]

        node.right = create_tree(inorder, postorder, curr_index+1, last)
        node.left = create_tree(inorder, postorder, start, curr_index-1)
        return node


    start = 0
    last = len(inorder)-1
    return create_tree(inorder, postorder, start, last)
    

def postorder_traversal(root):
    if root == None:
        return
    postorder_traversal(root.left)
    postorder_traversal(root.right)
    print(root.data, end=" ")


inorder = [4, 2, 5, 1, 6, 3, 7]
postorder = [4, 5, 2, 6, 7, 3, 1]
n=len(postorder)
Index = n-1
for i in range(n-1, -1, -1):
    Index_dict[inorder[i]] = i


tree = binary_tree_from_inorder_and_postorder(inorder, postorder)

postorder_traversal(tree)
