memo = []
def factorial(n):
    memo = []
    
    memo.append(1)
    i = 1
    while(i<=n):
        memo.append(i*memo[i-1])
        i += 1
    
    return memo[n]

print(factorial(10))

print(factorial(30))
    
     