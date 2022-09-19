n, b, k = map(int, input().split())
c = list(map(int, input().split()))
mod = 10 ** 9 + 7

dp = [[0] * (b+1) for _ in range(n+1)]
dp[0][0] = 1

for i in range(1, n+1):
    for j in range(b+1):
        for l in range(k):
            dp[i][j] += dp[i-1][(10*j+c[l]) % b]
            dp[i][j] %= mod

print(dp[n][0])
