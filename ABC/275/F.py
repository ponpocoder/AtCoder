n, m = map(int, input().split())
a = list(map(int, input().split()))

INF = 1001001001

# i番目まで見て合計jで最後が◯か×のときの必要な操作回数の最小値
dp = [[INF] * 2 for _ in range(m+1)]
dp[0][0] = 0


for i in range(n):
    p = dp[:]
    dp = [[INF] * 2 for _ in range(m+1)]
    for j in range(m+1):
        for k in range(2):
            curr = p[j][k]
            if j+a[i] <= m:
                dp[j+a[i]][0] = min(dp[j+a[i]][0], curr)
            cost = 1 if k == 0 else 0
            dp[j][1] = min(dp[j][1], curr+cost)

for i in range(1, m+1):
    res = min(dp[i])
    if res == INF:
        res = -1
    print(res)
