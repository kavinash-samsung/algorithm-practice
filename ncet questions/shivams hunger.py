def main():
    dp = [False for i in range(101)]
    dp[3] = True
    dp[7] = True
    for i in range(4,101):
        if i%3 == 0:
            dp[i] = dp[i] or dp[i-3]
        if i%7 == 0:
            dp[i] = dp[i] or dp[i-7]
    n = int(input())
    for i in range(n):
        x = int(input())
        if dp[x]:
            print("YES")
        else:
            print('NO')

main()