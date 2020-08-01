def subsetsum(array, sumn, n):
    matrix = [[False]*(sumn+1) for i in range(n+1)]

    for i in range(len(matrix[0])):
        matrix[0][i] = False
    for i in range(len(matrix)):
        matrix[i][0] = True
    
    for i in range(1, n+1):
        for j in range(1, sumn+1):
            if j <= array[i-1]:
                matrix[i][j] = matrix[i-1][j] or matrix[i-1][j-array[i-1]]
            else:
                matrix[i][j] = matrix[i-1][j]
    return matrix[n][sumn]
    


def equalsubset(array, n):
    total = sum(array) 
    if total % 2 != 0:
        return False
    else:
        return subsetsum(array, total//2, n)

array = [1, 5, 11, 7,6]
print(equalsubset(array,len(array)))
