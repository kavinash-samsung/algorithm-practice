def solve(a,b):
    l1 = len(a)
    l2 = len(b)
    matrix = [[-1]*(l1+1) for i in range(l2+2)]
    for i in range(l2+1):
        matrix[i][0] = i
    for i in range(l2+1):
        matrix[0][i] = i
    
    for i in range(1, l1+1):
        for j in range(1, l2+1):
            if a[i-1] == b[i-1]:
                matrix[i][j] = matrix[i-1][j-1]
            else:
                matrix[i][j] = 1 + min(matrix[i-1][j],matrix[i][j-1],matrix[i-1][j-1])

    return matrix[l1][l2]

