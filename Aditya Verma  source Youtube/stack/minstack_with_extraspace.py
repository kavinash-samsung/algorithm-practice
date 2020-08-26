arr = [5,3,6,2,8,6,9]


class minstack:
    def __init__(self):
        self.stack = []
        self.minstack = []

    def sizeofstack(self):
        return len(self.stack)

    def minimum(self):
        if self.minstack == []:
            return('stack is empty')
        return self.minstack[-1]

    def push(self,x):
        if self.stack == []:
            self.stack.append(x)
            self.minstack.append(x)
        else:
            self.stack.append(x)
            if self.minstack[-1]> x :
                self.minstack.append(x)
    
    def pop(self):
        x = self.stack.pop()
        if x == self.minstack[-1]:
            self.minstack.pop()
        return x    
    
    def print(self):
        if self.stack == []:
            print("stack is empty")
            return 
        print(self.stack)
        return
    
    def top(self):
        if self.stack == []:
            return("stack is empty")
        return self.stack[-1]

mini = minstack()

mini.push(20)
mini.push(10)
mini.push(40)
mini.push(9)
mini.push(45)

mini.pop()

print('minimum element resent in stack', mini.minimum())

print('top of stack is ',mini.top())

print('this is stack',mini.stack)
