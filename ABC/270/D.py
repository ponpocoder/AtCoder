import sys
sys.setrecursionlimit(10**6)
n, k = map(int, input().split())
a = list(map(int, input().split()))

dp = [0] * (n+1)
for i in range(n+1):
    for j in range(k):
        if a[j] > i:
            break
        dp[i] = max(dp[i], i - dp[i-a[j]])

print(dp[n])
