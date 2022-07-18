n, x, y = map(int, input().split())

dp = [[0] * 2 for _ in range(n)]
dp[n-1][0] = 1

for i in range(n-2, -1, -1):
    dp[i][0] += dp[i+1][0] 
    dp[i+1][1] += dp[i+1][0] * x
    dp[i][0] += dp[i+1][1]
    dp[i][1] += dp[i+1][1] * y

print(dp[0][1]) 
