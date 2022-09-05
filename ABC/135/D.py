s = input()
n = len(s)
mod = 10**9 + 7

dp = [[0] * 13 for _ in range(n+1)]
dp[0][0] = 1

for i in range(n):
    for j in range(13):
        if s[i] == "?":
            for k in range(10):
                nj = (j*10 + k) % 13
                dp[i+1][nj] += dp[i][j]
                dp[i+1][nj] %= mod
        else:
            nj = (j*10+int(s[i])) % 13
            dp[i+1][nj] += dp[i][j]
            dp[i+1][nj] %= mod

print(dp[-1][5])
