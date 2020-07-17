def subsetsumm(array, sumn, n):
    matrix = [[False]*(sumn+1) for i in range(len(array)+1)]

    for i in range(len(matrix[0])):
        matrix[0][i] = 0
    for i in range(len(matrix)):
        matrix[i][0] = 1
    
    for i in range(1, len(array)+1):
        for j in range(1, sumn+1):
            if j >= array[i-1]:
                matrix[i][j] = matrix[i-1][j] + matrix[i-1][j-array[i-1]]
            else:
                matrix[i][j] = matrix[i-1][j]
    for rows in matrix:
        print(rows)
    return matrix[n][sumn]
