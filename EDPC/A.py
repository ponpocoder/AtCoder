n = int(input())
h = list(map(int, input().split()))

dp = [0] * len(h)
dp[1] = abs(h[0] - h[1])

for i in range(2, len(h)):
    first = dp[i - 2] + abs(h[i - 2] - h[i])
    second = dp[i - 1]  + abs(h[i - 1] - h[i])
    dp[i] = min(first, second)

print(dp[-1])