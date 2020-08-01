"""

In this we have to find the next greater element
on the left side 

given array = [1, 3, 2, 4]

resultant array will be [-1, -1, 3, -1]

we have two approach to do this 
we can have a brute force approach

with the brute force we will use two for loop 

this will take the time complexity of O(n)

complexity for this is O(n)

"""

def next_greater_to_left(array):
    stack = []
    result = []
    n = len(array)

    for i in range(0,n):
        if len(stack) == 0:
            result.append(-1)
            stack.append(array[i])
        elif stack[-1] > array[i]:
            result.append(stack[-1])
            stack.append(array[i])
        else:
            while (len(stack) != 0 and stack[-1] <= array[i]):
                stack.pop()
            if len(stack) == 0:
                result.append(-1)
            else:
                result.append(stack[-1])
            stack.append(array[-1])
    return result

array = [1, 3, 2, 4]

print(next_greater_to_left(array))

