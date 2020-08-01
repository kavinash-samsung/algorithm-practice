'''

this is the code for matrix chaon multiplication 
to find the minimum cost to multiply matrices with 
each other

Simple solution for this is to place the paranthesis
like

let consider these variables as matrix 

ABCDE

putting paranthesis gives us following case

put paranthesis at every possible place



'''


'''

another way to solve this is overlapping subproblem

same problem is accuring again and again so using recursion to do this

using recursion to solve this

'''
def solve(array,i,j):
    if i == j:
        return 0
    min_cost = float('inf')
    for k in range(i,j):
        cost = solve(array, i, k) + solve(array, k+1, j) + (array[i-1] * array[k] * array[j])
        if min_cost>cost:
            min_cost = cost
    return min_cost


arr = [1, 2, 3, 4, 3]

print(solve(arr, 1, len(arr)-1))

print("######################\n######################")

'''

doing same example with memoization 
Just add some lines of code an here a dp dish is ready

'''
matrix = [[-1]*5 for i in range(5)]
def solve(array,i,j):
    if matrix[i][j] != -1:
        return matrix[i][j]
    if i == j:
        return 0
    
    min_cost = float('inf')
    for k in range(i,j):
        cost = solve(array, i, k) + solve(array, k+1, j) + (array[i-1] * array[k] * array[j])
        if min_cost>cost:
            min_cost = cost
    matrix[i][j] = min_cost
    return min_cost


arr = [1, 2, 3, 4, 3]
print('matrix used for memoisation')
print(solve(arr, 1, len(arr)-1))

for i in matrix:
    print(i)






