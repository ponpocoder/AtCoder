h, w = map(int, input().split())
s = [input() for _ in range(h)]
mod = 10**9+7
dpx = [[0] * w for _ in range(h)]
dpy = [[0] * w for _ in range(h)]
dpd = [[0] * w for _ in range(h)]
dp = [[0] * w for _ in range(h)]

dpx[0][0] = 1
dpy[0][0] = 1
dpd[0][0] = 1
dp[0][0] = 1

for i in range(h):
    for j in range(w):
        if i==0 and j==0:
            continue
        if s[i][j] == "#":
            continue
        if j:
            dpx[i][j] += dpx[i][j-1]
        if i:
            dpy[i][j] += dpy[i-1][j]
        if i and j:
            dpd[i][j] += dpd[i-1][j-1]
        dp[i][j] += dpx[i][j] + dpy[i][j] + dpd[i][j]
        dp[i][j] %= mod
        dpx[i][j] += dp[i][j]
        dpy[i][j] += dp[i][j]
        dpd[i][j] += dp[i][j]

print(dp[-1][-1])