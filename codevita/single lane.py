from itertools import permutations
from math import factorial
dictx = {}
def noofgroups(n):
  if n in dictx:
    return dictx[n]
  if n == 0:
    return 0
  x = (n)*noofgroups(n-1)+factorial(n-1)  
  dictx[n] = x
  return x

def noofgroup(n):
    ans = 0
    fact = 1
    for i in range(1,n):
        fact = fact*i
        ans = n*ans+fact
    return ans
         

n = int(input())
cars_speed = list(map(int,input().split(" ")))

ans = noofgroup(n)/factorial(n)

print("{0:.6f}".format(ans))