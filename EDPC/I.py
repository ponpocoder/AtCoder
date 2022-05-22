n = int(input())
p = list(map(float, input().split()))

#dp[i][j] = i枚のコインのうちj枚が表である確率
dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
dp[0][0] = 1

for i in range(1, n + 1):
    for j in range(i+1):
        if j != 0:
            dp[i][j] = dp[i - 1][j - 1] * p[i - 1] + dp[i - 1][j] * (1 - p[i - 1])
        else:
            dp[i][j] = dp[i - 1][j] * (1 - p[i - 1])

res = 0
for i in range(n // 2 + 1, n + 1):
    res += dp[-1][i]

print(res)

∑