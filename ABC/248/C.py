n, m, k = map(int, input().split())
mod = 998244353

dp = [[0 for _ in range(k)] for _ in range(n)]
for i in range(m):
    dp[0][i] = 1

for i in range(n - 1):
    for j in range(k):
        for l in range(1, m + 1):
            if j + l < k:
                dp[i + 1][j + l] += dp[i][j]

res = sum(dp[-1]) % mod
print(res)