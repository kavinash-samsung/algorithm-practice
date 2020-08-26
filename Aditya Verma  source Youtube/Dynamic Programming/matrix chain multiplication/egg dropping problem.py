def solve(e, f):
    if f==0 or f == 1:
        return f
    if e == 1:
        return f
    mn = float('inf')

    for i in range(1,f+1):
        temp = 1+max(solve(e-1,i-1),solve(e,f-i))
    
        mn = min(mn, temp)
    
    return mn


print(solve(3,20))