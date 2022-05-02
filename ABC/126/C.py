n, k = map(int, input().split())

dp = [1/n] * (n + 1)
dp[0] = 0

for i in range(1, n + 1):
    curr = i
    while curr < k:
        dp[i] /= 2
        curr *= 2

print(sum(dp))