n = int(input())

dp = []
dp.append([1])

for i in range(1, n):
    s = dp[i - 1] + [i + 1] + dp[i - 1]
    dp.append(s)

print(*dp[-1])