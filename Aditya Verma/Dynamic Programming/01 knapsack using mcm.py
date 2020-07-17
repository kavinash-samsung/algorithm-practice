def knapsack(n, price , weight, capacity):
    matrix = [[-1]*(capacity+1) for i in range(n+1)]

    for i in range(n+1):
        matrix[i][0] = 0
    for i in range(capacity+1):
        matrix[0][i] = 0

    for i in range(1,n+1):
        for j in range(1,capacity+1):
            if weight[i-1] <= j:
                matrix[i][j] = max(matrix[i-1][j],price[i-1]+matrix[i-1][j-weight[i-1]])
            else:
                matrix[i][j] = matrix[i-1][j]
    return matrix[n][capacity]

price = [60, 100, 120,300]
weight = [10,20,30,40]
capacity = 0
n = len(price)

print(knapsack(n, price, weight, capacity))