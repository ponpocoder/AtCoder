s = input()
n = len(s)
dp = [[0] * (n+1) for _ in range(9)]
t = "chokudai"
mod = 10**9 + 7

for j in range(n+1):
    dp[0][j] = 1

for i in range(1, 9):
    for j in range(1, n+1):
        dp[i][j] += dp[i][j-1]
        if s[j-1] == t[i-1]:
            dp[i][j] += dp[i-1][j-1]
        dp[i][j] %= mod

print(dp[-1][-1])