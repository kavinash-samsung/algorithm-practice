def minsubset(array, sumn, length):
    matrix = [[-1]*(sumn+1) for i in range(length+1)]
    for i in range(sumn+1):
        matrix[0][i] = 0
    for i in range(length+1):
        matrix[i][0] = 1
    for i in range(1,length+1):
        for j in range(1,sumn+1):
            if j>=array[i-1]:
                matrix[i][j] = matrix[i-1][j] + matrix[i-1][j-array[i-1]]
            else:
                matrix[i][j] = matrix[i-1][j]
    # for rows in matrix:
    #     print(rows)
    return matrix[length][sumn]
def countsubsetingivendifference(array,length,difference):
    total = sum(array)
    print((total+difference)//2)
    if (total + difference)%2 != 0:
        return -1
    else:
        return minsubset(array, (total+difference)//2, length)

array = [1,1,2,3]
length = len(array)
difference = 1
print(countsubsetingivendifference(array , length, difference))