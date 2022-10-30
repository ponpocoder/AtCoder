n, m, k = map(int, input().split())
mod = 998244353

# i回ルーレットを回した時にマスjいる時の確率
dp = [[0] * (n+1) for _ in range(k+1)]

dp[0][0] = 1

def powmod(a, b, mod):
    if b == 0:
        return 1
    curr = powmod(a, b//2, mod)
    curr *= curr
    if b % 2:
        curr *= a
    return curr % mod

y = powmod(m, mod-2, mod)
for i in range(1, k+1):
    for j in range(n):
        for x in range(1, m+1):                                   
            nxt = j+x
            if nxt > n:
                diff = nxt-n
                nxt = n-diff
            dp[i][nxt] += dp[i-1][j] * y
            dp[i][nxt] %= mod
        
res = 0
for i in range(k+1):
    res += dp[i][n]
    res %= mod
print(res)
