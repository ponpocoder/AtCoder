a, b, c, d, e, f = map(int, input().split())

dp = [[False] * (f+1) for _ in range(f+1)]
dp[0][0] = True

for i in range(f+1):
    for j in range(f+1):
        if not dp[i][j]:
            continue
        if i + 100*a <= f:
            dp[i+100*a][j] = True
        if i + 100*b <= f:
            dp[i+100*b][j] = True
        if i + c <= f and j + c <= f:
            dp[i+c][j+c] = True
        if i + d <= f and j + d <= f:
            dp[i+d][j+d] = True

res = 0
x, y = 100*a, 0
for i in range(1, f+1):
    for j in range(f+1):
        if not dp[i][j] or (100*j > (i-j)*e):
            continue
        curr = 100 * j / i
        if res < curr:
            res = curr
            x = i
            y = j

print(x, y)
