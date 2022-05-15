n, k = map(int, input().split())
h = list(map(int, input().split()))

dp = [float("inf")] * len(h)
dp[0] = 0

for i in range(len(h)):
    for j in range(i, min(len(h), i + k + 1)):
        dp[j] = min(dp[j], dp[i] + abs(h[i] - h[j]))
print(dp[-1])