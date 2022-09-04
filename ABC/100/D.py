n, m = map(int, input().split())
s = []

for _ in range(n):
    x, y, z = map(int, input().split())
    s.append((x, y, z))

dp = [[[0] * 3 for _ in range(m+1)] for _ in range(n+1)]

res = 0
curr = [0] * n
for a in [-1, 1]:
    for b in [-1, 1]:
        for c in [-1, 1]:
            for i in range(n):
                x, y, z = s[i]
                curr[i] = a * x + b * y + c * z

            dp = [[-float("inf")] * (m+1) for _ in range(n+1)]
            dp[0][0] = 0
            for i in range(1, n + 1):
                dp[i][0] = 0
                for j in range(1, m + 1):
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] + curr[i-1])

            res = max(res, dp[-1][-1])
print(res)
