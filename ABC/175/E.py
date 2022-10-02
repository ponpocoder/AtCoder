r, c, n = map(int, input().split())
grid = [[0] * c for _ in range(r)]

for _ in range(n):
    x, y, v = map(int, input().split())
    grid[x-1][y-1] += v

dp = [[0] * 4 for _ in range(c)]

for i in range(r):
    p = dp
    dp = [[0] * 4 for _ in range(c)]
    for j in range(c):
        for k in range(4):
            if i > 0:
                dp[j][k] = max(dp[j][k], p[j][0])
            if j > 0:
                dp[j][k] = max(dp[j][k], dp[j-1][k])
        for k in range(1, 4):
            dp[j][k-1] = max(dp[j][k-1], dp[j][k] + grid[i][j])

res = 0
for i in range(4):
    res = max(res, dp[c-1][i])
print(res)
