'''

this is the finding steps problem solution 
this solution is provided in educative.io
as example 

time complexity of this code is O(n)

from recursion to memoisation complexity
complexity changes from exponential to linear

'''


step = {}
def staircase(n,m):
    if n == 0 :
        return 1
    if n in step:
        return step[n]
    ways = 0
    for i in range(1,m+1):
        if i <= n:
            ways += staircase(n-i,m)
    step[n] = ways
    return step[n]

print(staircase(4,2))

