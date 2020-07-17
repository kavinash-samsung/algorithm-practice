steptrack = {}
def staircase(n,m):
    if n == 1:
        return 1
    if n in steptrack:
        return steptrack[n]
    if n <= m:
        steptrack[n] = 1
        for i in range(1,n):
            steptrack[n] += staircase(n-i,m) 
        return steptrack[n]
    if n>m:
        steptrack[n] = 0
        for i in range(1,m+1):
            steptrack[n] += staircase(n-i,m)
        return steptrack[n]
         



n = 100
m = 6
print(staircase(n,m))
# print(steptrack[n])
print(steptrack)