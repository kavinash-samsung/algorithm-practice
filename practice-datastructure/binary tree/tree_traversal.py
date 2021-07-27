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

    def inorder_iterative(self):
        stack = []
        temp = self.root
        result = []
        while(True):
            if temp:
                stack.append(temp)
                temp = temp.left
            elif stack:
                temp = stack.pop()
                result.append(temp.data)
                temp = temp.right
            else:
                break
        for i in result:
            print(i, end=" ")

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
            print(x.data, end=" ")
            if x.left:
                queue.append(x.left)
            if x.right:
                queue.append(x.right)

    def preorder_iterative(self):
        stack = [self.root]
        queu = list()
        while(stack):
            x = stack.pop()
            queu.append(x.data)
            if x.right:
                stack.append(x.right)
            if x.left:
                stack.append(x.left)
        for i in queu:
            print(i,end=" ")
        
    def postorder_iterative(self):
        stack1 = [self.root]
        stack2 = []
        while(stack1):
            x = stack1.pop()
            stack2.append(x.data)
            if x.left:
                stack1.append(x.left)
            if x.right:
                stack1.append(x.right)
        n = len(stack2)
        for i in range(n):
            print(stack2[n-1-i], end=" ")
    
    




        
    

tree = BinaryTree()
tree.insertNode(10)
tree.insertNode(11)
tree.insertNode(12)
tree.insertNode(13)
tree.insertNode(14)
tree.insertNode(15)
print("inorder", end=" ")
tree.inorder_iterative()
print()
print("preorder", end=" ")
tree.preorder_iterative()
print()
print("postorder", end=" ")
tree.postorder_iterative()

print()
print("levelorder", end=" ")
tree.levelOrder()

            