
def maxsubAsize(A):
    n = len(A)
    dp = [float('-inf')]*n
    dp[0] = A[0]
    maxi = A[0]


    for i in range(1,len(A)):
        maxi = max(dp[i-1]+A[i], A[i])
        dp[i] = maxi
    return max(dp)



arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
n = len(arr)

print(maxsubAsize(arr))
