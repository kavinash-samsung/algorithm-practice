def insert(stack, x):
    if stack == [] or stack[-1] <= x:
        stack.append(x)
        return
    last = stack.pop()
    insert(stack, x)
    stack.append(last)
    return
    

def sortstack(stack):
    if len(stack) == 1:
        return
    last = stack.pop()
    sortstack(stack)
    insert(stack, last)
    return 

stack = [10,30,50,70,60,40,20]
print("stack before sort",stack)

sortstack(stack)

print("sorted stack",stack)
    