def next_greater_to_left(array):
    stack = []
    result = []
    n = len(array)

    for i in range(0,n):
        if len(stack) == 0:
            result.append(i + 1)
            stack.append(array[i])
        elif stack[-1] > array[i]:
            result.append(i - array.index(stack[-1]))
            stack.append(array[i])
        else:
            while (len(stack) != 0 and stack[-1] <= array[i]):
                stack.pop()
            if len(stack) == 0:
                result.append(i + 1)
            else:
                result.append(i - array.index(stack[-1]))
            stack.append(array[i])
    # alternate way is to first get all the results 
    #   without calcuating final answers 
    #   
    #     print(stack)
    # for i in range(n):        
    #     result[i] = i-result[i]
    return result

array = [1, 3, 2, 4]

print(next_greater_to_left(array))


