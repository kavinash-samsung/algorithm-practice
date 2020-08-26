class minstack:
    def __init__(self):
        self.__stack = []
        self.__minimum = float('inf')
        self.__n = 0
    
    def top(self):
        if self.__n == 0:
            return "stack is empty"
        if self.__stack[-1]>self.__minimum:
            return self.__stack[-1]
        else:
            return self.__minimum
    
    def sizeofstack(self):
        return self.__n
    
    def push(self,x):
        if self.__n == 0:
            self.__n += 1
            self.__minimum = x
            self.__stack.append(x)
        else:
            self.__n += 1
            if self.__minimum < x:
                self.__stack.append(x)
            else:
                no = 2*x-self.__minimum
                self.__stack.append(no)
                self.__minimum = x
    
    def pop(self):
        if self.__n == 0:
            return 'stack is empty'
        if self.top()>self.__minimum:
            self.__n -= 1
            return self.__stack.pop()
        else:
            self.__n -= 1
            popeditem = self.__minimum
            mini = 2*self.__minimum - self.__stack.pop()
            self.__minimum = mini
            return popeditem

    def minimum(self):
        if self.__n == 0:
            return 'stack is empty'
        return self.__minimum
    
    def print(self):
        print(self.__stack)
    


mini = minstack()

mini.push(20)
mini.push(10)
mini.push(40)
mini.push(9)
mini.push(45)

mini.pop()
mini.pop()

print('minimum element recent in stack', mini.minimum())

print('top of stack is ',mini.top())



