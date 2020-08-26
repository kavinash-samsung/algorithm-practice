
def next_minimum_to_right(array):
    stack = []
    result = []
    n = len(array)
    for i in range(n-1,-1,-1):
        if len(stack)==0:
            result.append(-1)
            stack.append(array[i])
        elif(stack[-1]<array[i]):
            result.append(stack[-1])
            stack.append(array[i])
        else:
            while(len(stack) != 0 and stack[-1] >= array[i]):
                stack.pop()
                
            if len(stack)== 0:
                result.append(-1)
            else:
                result.append(stack[-1])
            stack.append(array[i])
    return result[::-1]