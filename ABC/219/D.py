n = int(input())
x, y = map(int, input().split())

dp = [[[float("inf")] * (y+1) for _ in range(x+1)] for _ in range(n+1)]

dp[0][0][0] = 0

for i in range(1, n+1):
    a, b = map(int, input().split())
    for j in range(x+1):
        for k in range(y+1):
            dp[i][min(a+j, x)][min(b+k, y)] = min(dp[i][min(a+j,x)][min(b+k,y)], dp[i-1][j][k]+1)
            dp[i][j][k] = min(dp[i][j][k], dp[i-1][j][k])

res = dp[n][x][y]

if res == float("inf"):
    print(-1)
else:
    print(res)