def delete(stack, mid):
    if len(stack) == mid:
        stack.pop()
        return
    x = stack.pop()
    delete(stack, mid)
    stack.append(x)
    return

def delmiddle(stack):
    if stack:
        if stack == []:
            print("stack is empty")
        mid = len(stack)//2+1
        # mid = len(stack) - mid
        delete(stack,mid)
        return
    print("no stack present")

 

stack = [1, 2, 3, 4, 6, 5]

delmiddle(stack)

print(stack)