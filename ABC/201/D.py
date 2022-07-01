h, w = map(int, input().split())
a = [input() for _ in range(h)]

dp = [[-10**7] * w for _ in range(h)]
dp[-1][-1] = 0

for i in range(h-1, -1, -1):
    for j in range(w-1, -1, -1):
        if i == h-1 and j == w-1:
            continue
        if i < h - 1:
            if a[i+1][j] == "+":
                dp[i][j] = max(dp[i][j], 1 - dp[i+1][j])
            else:
                dp[i][j] = max(dp[i][j], -1 - dp[i+1][j])
        if j < w - 1:
            if a[i][j+1] == "+":
                dp[i][j] = max(dp[i][j], 1 - dp[i][j+1])
            else:
                dp[i][j] = max(dp[i][j], -1 - dp[i][j+1])

res = dp[0][0]
if res == 0:
    print("Draw")
elif res > 0:
    print("Takahashi")
else:
    print("Aoki")