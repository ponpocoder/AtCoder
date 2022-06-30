n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
mod = 998244353

k = 3001
dp = [0] * k
dp[0] = 1
for i in range(n):
    p = dp
    dp = [0] * k
    s = [0] * (k+1)
    for j in range(k-1):
        p[j+1] += p[j]
        p[j+1] %= mod

    for j in range(a[i], b[i] + 1):
        dp[j] += p[j]

print(sum(dp)%mod)
