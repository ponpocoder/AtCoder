n, k = map(int, input().split())
a = list(map(int, input().split()))
mod = 10 ** 9 + 7

dp = [[0] * (k+1) for _ in range(n)] # i:子供の番号, j:配った飴の数
for j in range(min(k+1, a[0] + 1)):
    dp[0][j] = 1

for i in range(1, n):
    curr = [0] * (k+1)
    curr[0] = dp[i-1][0]
    for j in range(1, k+1):
        curr[j] = curr[j-1] + dp[i-1][j]

    for j in range(k+1):
        if j <= a[i]: #箱iに0個のアメを詰める
            dp[i][j] = curr[j]
        else:
            dp[i][j] = curr[j] - curr[j - a[i] - 1] #箱iにj-a[j]個のアメを詰める
        dp[i][j] %= mod

print(dp[-1][-1])


