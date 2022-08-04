n = int(input())
a = list(map(int, input().split()))
mod = 998244353

res = 0

for i in range(1, n+1):
    # dp[j][k][l]: j項からk個選んだ時の余りがl
    dp = [[[0] * i for _ in range(i+1)] for _ in range(n+1)]
    dp[0][0][0] = 1

    for j in range(n):
        for k in range(i+1):
            for l in range(i):
                dp[j+1][k][l] += dp[j][k][l]
                dp[j+1][k][l] %= mod
                if k != i:
                    dp[j+1][k+1][(l+a[j]) % i] += dp[j][k][l]
                    dp[j+1][k+1][(l+a[j]) % i] %= mod

    res += dp[n][i][0]
    res %= mod

print(res)
