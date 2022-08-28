from collections import defaultdict

n = int(input())
s = defaultdict(int)
tmax = 0
for _ in range(n):
    t, x, a = map(int, input().split())
    s[(t, x)] += a
    tmax = max(tmax, t)

tmax += 1

dp = [[-1] * 5 for _ in range(tmax)]
dp[0][0] = 0
for i in range(1, tmax):
    for j in range(5):
        dp[i][j] = dp[i-1][j]
        if j > 0 and dp[i-1][j-1] != -1:
            dp[i][j] = max(dp[i][j], dp[i-1][j-1])
        if j < 4 and dp[i-1][j+1] != -1:
            dp[i][j] = max(dp[i][j], dp[i-1][j+1])
        if (i, j) in s and dp[i][j] != -1:
            dp[i][j] += s[(i, j)]

res = max(dp[-1])
if res == -1:
    print(0)
else:
    print(res)
