"""

In this we find next greater element in this array

given array = [1, 3, 2, 4]

answer will be [3, 4, 4, -1]

next greater element

"""



def next_greater_to_right(arr):
    n = len(arr)
    result = []
    stack = []
    for i in range(n-1,-1,-1):
        if len(stack)==0:
            result.append(-1)
            stack.append(arr[i])
        elif(stack[-1]>arr[i]):
            result.append(stack[-1])
            stack.append(arr[i])
        else:
            while(stack[-1] <= arr[i] and len(stack) != 0):
                stack.pop()
                
            if len(stack)== 0:
                result.append(-1)
            else:
                result.append(stack[-1])
            stack.append(arr[i])
    return result[::-1]




array = [1,3,2,4]

print(next_greater_to_right(array))
