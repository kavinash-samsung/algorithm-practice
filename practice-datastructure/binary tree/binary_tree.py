class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None
    

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insertNode(self,data):
        if self.root == None:
            self.root = Node(data)
            return 
        queue = [self.root]
        while(queue):
            x = queue.pop(0)
            if x.left:
                queue.append(x.left)
            else:
                x.left = Node(data)
                return
            if x.right:
                queue.append(x.right)
            else:
                x.right = Node(data)
                return

    def preorder(self):
        temp = self.root
        def preorder(root):
            if root == None:
                return 
            preorder(root.left)
            print(root.data, end=" - ")
            preorder(root.right)
        preorder(temp)
    
    def levelOrder(self):

        queue = [self.root]
        while(queue):
            x = queue.pop(0)
            print(x.data, end=" - ")
            if x.left:
                queue.append(x.left)
            if x.right:
                queue.append(x.right)

    def __deleteDepthNode(self,d_node):
        
        queue = [self.root]
        while(queue):
            x = queue.pop(0)
            if x.right == d_node:
                x.right = None
                return
            else:
                if x.right != None:
                    queue.append(x.right)
            if x.left == d_node:
                x.left = None
                return
            else:
                if x.left != None:
                    queue.append(x.left)


    def deleteNode(self,data):
        if self.root == None:
            return
        if self.root.left ==None and self.root.right == None:
            if self.root.data == data:
                self.root = None
                return
            else:
                return
        key_node = None
        queue = [self.root]
        d_node = None
        while(queue):
            d_node = queue.pop(0)
            if d_node.data == data:
                key_node = d_node
            if d_node.left:
                queue.append(d_node.left)
            if d_node.right:
                queue.append(d_node.right)
        
        key_node.data = d_node.data
        self.__deleteDepthNode(d_node)
        return


tree = BinaryTree()
tree.insertNode(10)
tree.insertNode(11)
tree.insertNode(12)
tree.insertNode(13)
tree.insertNode(14)
tree.insertNode(15)
print("before deletion")
tree.levelOrder()
tree.deleteNode(10)
print()
print("after deletion")
tree.levelOrder()

            