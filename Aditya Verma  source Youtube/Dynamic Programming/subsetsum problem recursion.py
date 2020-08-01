
def subsetsum(seti, sumi, n):
    if sumi == 0 :
        dicti[0] = True
        return True
    elif n == 0:
        return False
    if sumi in dicti:
        return dicti[sumi]
    if sumi>= seti[n-1]:
        dicti[sumi] = subsetsum(seti,sumi-seti[n-1]
        ,n-1) or subsetsum(seti, sumi, n-1)
    else:
        dicti[sumi] = subsetsum(seti, sumi, n-1)
    return dicti[sumi]


def subsetsummatrix(seti,sumi,n):
    matrix = [[False]*(sumi+1) for i in range(len(seti)+1)]
    for i in range(len(matrix[0])):
        matrix[0][i] = False
    for i in range(len(matrix)):
        matrix[i][0] = True
    for i in range(len(seti)+1):
        for j in range(sumi+1):
            if seti[i-1]<= j:
                matrix[i][j] = (matrix[i-1][j-seti[i-1]]) or matrix[i-1][j]
            else:
                matrix[i][j] = matrix[i-1][j]
    return matrix[n][sumi]
    

seti = [2,3,7,8,10]
sumi = 20
n = len(seti)
dicti = {}
print(subsetsummatrix(seti, sumi, n))
print(dicti)


    