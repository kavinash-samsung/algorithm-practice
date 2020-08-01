def no_of_ways(coins, sumn, length):
    matrix = [[0]*(sumn+1) for i in range(length+1)]
    for i in range(sumn+1):
        matrix[0][i] = 0
    for i in range(length+1):
        matrix[i][0] = 1
    for i in range(1, length+1):
        for j in range(1, sumn+1):
            if j>=coins[i-1]:
                matrix[i][j] = matrix[i-1][j] + matrix[i][j-coins[i-1]]
            else:
                matrix[i][j] = matrix[i-1][j]
    return matrix[length][sumn]

coins = [1,2,3]
sumn = 400
length = len(coins)
print(no_of_ways(coins, sumn, length))