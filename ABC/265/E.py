n, m = map(int, input().split())
a, b, c, d, e, f = map(int, input().split())

s = set()
mod = 998244353

for _ in range(m):
    x, y = map(int, input().split())
    s.add((x, y))

dp = [[[0] * (n+1) for _ in range(n+1)] for _ in range(n+1)]
dp[0][0][0] = 1

for i in range(n+1):
    for j in range(i+1):
        for k in range(i+1):
            if j + k > i:
                break
            l = i - j - k
            cx = a*j + c*k + e*l
            cy = b*j + d*k + f*l
            if (cx, cy) in s:
                continue
            if j > 0:
                dp[j][k][l] += dp[j-1][k][l]
            if k > 0:
                dp[j][k][l] += dp[j][k-1][l]
            if l > 0:
                dp[j][k][l] += dp[j][k][l-1]
            dp[j][k][l] %= mod


res = 0
for i in range(n+1):
    for j in range(n+1):
        if i + j > n:
            break
        res += dp[i][j][n - i - j]
        res %= mod

print(res)
