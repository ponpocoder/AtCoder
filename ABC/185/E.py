n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

INF = 1001001001
dp = [[INF] * (m+1) for _ in range(n+1)]
dp[0][0] = 0

for i in range(n + 1):
    for j in range(m + 1):
        if i > 0:
            dp[i][j] = min(dp[i][j], dp[i-1][j] + 1)
        if j > 0:
            dp[i][j] = min(dp[i][j], dp[i][j-1] + 1)
        if i > 0 and j > 0:
            cost = 0
            if a[i-1] != b[j-1]:
                cost = 1
            dp[i][j] = min(dp[i][j], dp[i-1][j-1] + cost)

print(dp[n][m])
