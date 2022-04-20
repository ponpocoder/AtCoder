n = int(input())
happiness = []

for _ in range(n):
    happiness.append(list(map(int, input().split())))

dp = [[0 for _ in range(3)] for _ in range(n + 1)]

for i in range(n):
    dp[i + 1][0] = max(dp[i][1], dp[i][2]) + happiness[i][0]
    dp[i + 1][1] = max(dp[i][0], dp[i][2]) + happiness[i][1]
    dp[i + 1][2] = max(dp[i][0], dp[i][1]) + happiness[i][2]

print(max(dp[-1]))
