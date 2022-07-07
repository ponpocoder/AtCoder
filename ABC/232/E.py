h, w, k = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())
mod = 998244353

dp = [[0] * 2 for _ in range(2)]

if x1 == x2 and y1 == y2:
    dp[1][1] = 1
elif x1 == x2:
    dp[1][0] = 1
elif y1 == y2:
    dp[0][1] = 1
else:
    dp[0][0] = 1

for i in range(k):
    p = dp
    dp = [[0] * 2 for _ in range(2)]
    dp[0][0] = p[0][0] * (h-2+w-2) + p[0][1] * (w-1) + p[1][0] * (h-1)
    dp[0][1] = p[0][0] + p[0][1] * (h-2) + p[1][1] * (h-1)
    dp[1][0] = p[0][0] + p[1][0] * (w-2) + p[1][1] * (w-1)
    dp[1][1] = p[0][1] + p[1][0]
    for i in range(2):
        for j in range(2):
            dp[i][j] %= mod

print(dp[1][1])