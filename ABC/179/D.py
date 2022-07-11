n, k = map(int, input().split())
mod = 998244353

lr = []
for _ in range(k):
    l, r = map(int, input().split())
    lr.append((l, r))

dp = [0] * (n+1)
dpsum = [0] * (n+1)
dp[1] = 1
dpsum[1] = 1

for i in range(2, n+1):
    for l, r in lr:
        left = max(i-r, 1)
        right = i-l
        if right <= 0:
            continue
        dp[i] += dpsum[right] - dpsum[left-1]
        dp[i] %= mod

    dpsum[i] = dp[i] + dpsum[i-1]

print(dp[-1])