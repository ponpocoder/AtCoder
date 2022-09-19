n = int(input())
jobs = []

for _ in range(n):
    d, c, s = map(int, input().split())
    jobs.append((d, c, s))

jobs.sort()

dp = [[0] * 5001 for _ in range(n+1)]

for i in range(1, n+1):
    d, c, s = jobs[i-1]
    for j in range(1, 5001):
        if c <= j and j <= d:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-c] + s)
        else:
            dp[i][j] = dp[i-1][j]

res = 0
for j in range(1, 5001):
    res = max(res, dp[n][j])

print(res)
