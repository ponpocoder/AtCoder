n, m, k = map(int, input().split())
mod = 998244353

if k == 0:
    res = 1
    for _ in range(n):
        res *= m
        res %= mod
    print(res)
    exit()

dp = [1] * (m)

def getCount(l, r, s):
    if l > r:
        return 0
    return s[r+1] - s[l]
    
for i in range(1, n):
    p = dp
    s = [0] * (m+1)
    for j in range(m):
        s[j+1] = s[j] + p[j]

    for j in range(m):
        p[j] = getCount(0, j-k, s) + getCount(j+k, m-1, s)
        p[j] %= mod
    dp = p

res = 0
for i in range(m):
    res += dp[i]
    res %= mod
print(res)