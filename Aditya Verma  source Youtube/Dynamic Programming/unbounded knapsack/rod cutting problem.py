"""

this is the dynamic programming approach of doing this problem
time complexity for this is O(n^2)

this gives optimum result in less time

"""
def kanpsack(length_array, value_array, n,cur_length):
    matrix = [[-1]*(n+1) for i in range(len(length_array)+1)]
    for i in range(len(matrix)):
        matrix[i][0] = 0
    for i in range(len(matrix[0])):
        matrix[0][i] = 0
    
    for i in range(1, len(value_array)+1):
        for j in range(1,len(length_array)+1):
            if j >= length_array[i-1]:
                matrix[i][j] = max(value_array[i-1]+matrix[i][j-length_array[i-1]],matrix[i-1][j])
            else:
                matrix[i][j] = matrix[i-1][j]
    return matrix[len(length_array)][n]



length_array = [1,2,3,4,5,6,7,8]
value_array = [9,7,6,5,71,3,2,1]

n = 8

print(kanpsack(length_array, value_array,n,0))

