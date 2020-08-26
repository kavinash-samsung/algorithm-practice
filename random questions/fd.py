def fact(n): 
      
    res = 1
    for i in range(2, n + 1):  
        res = res * i 
    return res 
  
# Applying the formula  
def count_heads(n, r): 
      
    output = fact(n) / (fact(r) * fact(n - r)) 
    output = output / (2**n) 
    return output 
  
# Driver code 
n,r = tuple(map(int,input().split()))

  
# Call count_heads with n and r 
print (count_heads(n, r)) 