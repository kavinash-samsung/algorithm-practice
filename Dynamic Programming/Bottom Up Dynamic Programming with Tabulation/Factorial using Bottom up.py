
def factorial(n):
    table = [0]*(n+1)
    table[0] = 1

    for i in range(1,n+1):
        table[i] = table[i-1] * i
    
    return table[n]

print(factorial(5))


