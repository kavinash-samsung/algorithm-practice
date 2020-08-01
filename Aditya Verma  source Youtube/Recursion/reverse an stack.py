def insert(stack,n):
    if stack ==[]:
        stack.append(n)
        return

    lastItem = stack.pop()
    insert(stack, n)
    stack.append(lastItem)

def reverseStack(stack):
    if len(stack) == 1:
        return 
    item = stack.pop()
    reverseStack(stack)
    insert(stack, item)


stack = [1,2,3,4,5]
reverseStack(stack)
print(stack)