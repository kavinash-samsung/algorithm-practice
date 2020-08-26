

# go to bottom of the code 




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

def max_area_matrix(matrix):
    
    modified_matrix = [[0]*len(matrix[0]) for i in range(len(matrix))]
    modified_matrix[0] = matrix[0]
    for i in range(1,len( matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != 0:
                modified_matrix[i][j] = modified_matrix[i-1][j] + matrix[i][j]
    maxi = float('-inf')
    for i in modified_matrix:
        # print(i)
        x = maxareahistogram(i) 
        # print(x)
        if x>maxi:
            maxi = x
    
    return maxi
    
    



matrix = [  
            [0, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 0, 0]
         ]

print(max_area_matrix(matrix))

