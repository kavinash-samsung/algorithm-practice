"""

this is also an popular problem in dp 
this algo is the optimum for finding minimum 
no of coins required to achieve the sum 
in the given coins value

this algo takes time complexity of O(n*m)

where n is total given coins size 
and m is the total value we have to make

"""




def minimum_no_of_coins(coins, sumn, length):
    matrix = [[float('inf')]*(sumn+1) for i in range(length+1)]
    for i in range(length+1):
        matrix[i][0] = 0
    for j in range(sumn+1):
        matrix[0][j] = float('inf')
    for i in range(1,sumn+1):
        if i%coins[0] == 0:
            matrix[1][i] = i//coins[0] 
        else:
            matrix[1][i] = float('inf')
    
    for i in range(1,length+1):
        for j in range(2,sumn+1):
            if j>= coins[i-1]:
                matrix[i][j] = min(1+matrix[i][j-coins[i-1]],matrix[i-1][j])
            else:
                matrix[i][j] = matrix[i-1][j]

    return matrix[length][sumn]

coins = [1, 2, 3]
sumn = 10
length = len(coins)

print(minimum_no_of_coins(coins, sumn, length))