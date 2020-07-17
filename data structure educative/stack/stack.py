class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        return self.items.append(item)
    
    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]
    
    def get_stack(self):
        return self.items
    
    def is_empty(self):
        return self.item == []
    
    

myStack = Stack()
myStack.push("A")
myStack.push("B")
print(myStack.get_stack())
myStack.push("C")
print(myStack.get_stack())
myStack.pop()
print(myStack.get_stack())

print(myStack.peek())