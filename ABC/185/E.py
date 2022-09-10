n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

INF = 1001001
dp = [[INF] * (m+1) for _ in range(n+1)]
dp[0][0] = 0

for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = min(dp[i][j], dp[i][j-1] + 1, dp[i-1][j] + 1)
        cost = 0
        if a[i-1] != b[j-1]:
            cost = 1
        dp[i][j] = min(dp[i][j], dp[i-1][j-1] + cost)

print(dp[n][m])
