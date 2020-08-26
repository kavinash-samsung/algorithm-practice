def next_minimum_to_left(array):
    stack = []
    result = []
    pseudoindex = -1
    n = len(array)
    for i in range(n):
        if len(stack) == 0:
            result.append(pseudoindex)
            stack.append((array[i],i))
        elif(stack[-1][0]<array[i]):
            result.append(stack[-1][1])
            stack.append((array[i],i))
        else:
            while(len(stack) != 0 and stack[-1][0] >= array[i]):
                stack.pop()
                
            if len(stack)== 0:
                result.append(pseudoindex)
            else:
                result.append(stack[-1][1])
            stack.append((array[i],i))
    return result


def next_minimum_to_right(array):
    stack = []
    result = []
    pseudoindex = len(array)
    n = len(array)
    for i in range(n-1,-1,-1):
        if len(stack) == 0:
            result.append(pseudoindex)
            stack.append((array[i],i))
        elif(stack[-1][0]<array[i]):
            result.append(stack[-1][1])
            stack.append((array[i],i))
        else:
            while(len(stack) != 0 and stack[-1][0] >= array[i]):
                stack.pop()
                
            if len(stack)== 0:
                result.append(pseudoindex)
            else:
                result.append(stack[-1][1])
            stack.append((array[i],i))
    return result[::-1]

def maxareahistogram(array):
    left = next_minimum_to_left(array)

    right =next_minimum_to_right(array)

    result = 0
    
    for i in range(len(array)):
        result = max(result,(right[i]-left[i]-1)*array[i])
    
    return(result)