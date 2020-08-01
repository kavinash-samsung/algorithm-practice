"""

this is the same variant of that question 
array  = [1, 3, 2, 4]

resultant array will [-1, 2, -1, -1]

"""

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

array = [1,3,2,4]

print(next_minimum_to_right(array))