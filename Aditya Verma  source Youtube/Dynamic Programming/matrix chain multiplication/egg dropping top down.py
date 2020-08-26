def solve(e,f):
    matrix = [[-1]*(f+1) for i in range(e+1)]

    for k in range(f+1):
        for i in range(e+1):
            if matrix[i][k] != -1:
                
            for j in range(k+1):
                
                matrix[i][j] = 1+max()