n = int(input())
mod = 998244353 

dp = [[0 for _ in range(n)] for _ in range(9)]
for i in range(9):
    dp[i][0] = 1
for i in range(1, n):
    for j in range(9):
        if j == 0:
            dp[j][i] = (dp[j][i - 1] + dp[j + 1][i - 1]) % mod
        elif j == 8:
            dp[j][i] = (dp[j][i - 1] + dp[j - 1][i - 1]) % mod
        else:
            dp[j][i] = (dp[j][i - 1] + dp[j - 1][i - 1] + dp[j + 1][i - 1]) % mod

res = 0
for i in range(9):
    res = (res + dp[i][-1]) % mod

print(res)
