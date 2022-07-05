n = int(input())
x = [[float("inf"), -float("inf")] for _ in range(n+1)]

for _ in range(n):
    a, c = map(int, input().split())
    x[c][0] = min(x[c][0], a)
    x[c][1] = max(x[c][1], a)
x[0][0] = 0
x[0][1] = 0
x.append([0, 0])

y = []
for l, r in x:
    if l != float("inf"):
        y.append([l, r])

dp = [0] * 2

for i in range(1, len(y)):
    p = dp
    dp = [float("inf")] * 2
    l, r = y[i]
    for j in range(2):
        s = y[i-1][1] if j else y[i-1][0]
        dp[0] = min(dp[0], p[j] + abs(s-r) + abs(r-l))
        dp[1] = min(dp[1], p[j] + abs(s-l) + abs(r-l))

print(dp[0])