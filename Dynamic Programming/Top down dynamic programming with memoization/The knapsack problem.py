'''

knapsack problem

A thief has broken into a house
the house has many valuable goods but unfortunately, 
the thief only brought a knapsack with a limited capacity. 
Every good in the house has a value in dollars 
and weight in kilograms associated with it. 
The thief wants to maximize the utility of his trip 
and take back the goods that fit his knapsack 
and earn him the highest possible money.




'''




def printMatrix(matrix):
    for rows in matrix:
        print(rows)

def knapsack(weight, price, capacity):
    n = len(weight)
    matrix = [[0 for i in range(capacity+1)]for j in range(n+1)]
    
    
    for i in range(1,n+1):
        for j in range(1,capacity+1):
            if weight[i-1]>j:
                matrix[i][j] = matrix[i-1][j]
            else:
                matrix[i][j] = max(matrix[i-1][j],price[i-1]+matrix[i-1][j-weight[i-1]])
    printMatrix(matrix)
    return matrix[n][capacity]
                                                    # weight = [1, 2, 4, 6]
weight = [1, 2, 4, 6]
price = [4, 2, 4, 7]
capacity =7

print(knapsack(weight, price, capacity))
