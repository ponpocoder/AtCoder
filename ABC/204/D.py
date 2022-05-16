n = int(input())
t = [0] + list(map(int, input().split()))

s = sum(t)

dp = [[False for _ in range(s + 1)] for _ in range(n+1)]

dp[0][0] = True

for i in range(1, n+1):
    for j in range(s+1):
        if dp[i-1][j]:
            dp[i][j] = True
        if j - t[i] >= 0 and dp[i-1][j-t[i]]:
            dp[i][j] = True

res = float("inf")

for j in range(s+1):
    if dp[n][j]:
        res = min(res, max(j, s - j))

print(res)