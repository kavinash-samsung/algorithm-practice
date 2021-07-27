
#        1
#     2       3
# 4      5  6    7

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

Index = 0
Index_dict = {}
def binary_tree_from_inorder_and_preorder(inorder,preorder):
    def create_tree(inorder,preorder,left,right):
        global Index, Index_dict
        if left>right:
            return None
        x = preorder[Index]
        node = Node(x)
        Index += 1
        if left == right:
            return node
        curr_index = Index_dict[x]

        node.left = create_tree(inorder, preorder, left, curr_index-1)
        node.right = create_tree(inorder,preorder, curr_index+1, right)
        return node
    left = 0
    right = len(preorder)-1
    
    return create_tree(inorder,preorder,left, right)

    
        
        


def preorder_traversal(root):
    if root == None:
        return 
    print(root.data, end=" ")
    preorder_traversal(root.left)
    preorder_traversal(root.right)


inorder = [4,2,5,1,6,3,7]
preorder =[1,2,4,5,3,6,7]
Index = 0

for i in range(len(inorder)):
    Index_dict[inorder[i]] = i



tree = binary_tree_from_inorder_and_preorder(inorder,preorder)
preorder_traversal(tree)