n, w = map(int, input().split())

weights, values = [], []

for _ in range(n):
    weight, value = map(int, input().split())
    weights.append(weight)
    values.append(value)

dp = [[float("inf") for _ in range(100001)] for _ in range(n + 1)]
dp[0][0] = 0

for i in range(1, n + 1):
    for j in range(100001):
        if j >= values[i - 1]:
            dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - values[i - 1]] + weights[i - 1])
        else:
            dp[i][j] = dp[i - 1][j]

res = 0
for i in reversed(range(100001)):
    if dp[-1][i] <= w:
        res = i
        break
print(res)