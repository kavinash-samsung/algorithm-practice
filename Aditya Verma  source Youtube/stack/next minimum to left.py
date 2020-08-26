"""

array = [1, 3, 2, 4]

result array = [-1, 1, 1, 2]

This is the O(n) approach 

"""
def next_minimum_to_left(array):
    stack = []
    result = []
    n = len(array)
    for i in range(n):
        if len(stack) == 0:
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
    return result

array = [1,3,5,4]

print(next_minimum_to_left(array))