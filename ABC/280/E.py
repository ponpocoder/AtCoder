import sys
sys.setrecursionlimit(10**6)
n, p = map(int, input().split())
mod = 998244353


def powmod(a, b, mod):
    if b == 0:
        return 1
    curr = powmod(a, b//2, mod)
    curr *= curr
    if b % 2:
        curr *= a
    return curr % mod


x = p*powmod(100, mod-2, mod) % mod
y = (1 - x) % mod

dp = [-1] * (n+1)
dp[0] = 0


def dfs(i):
    if i == -1:
        return 0
    if dp[i] != -1:
        return dp[i]
    dp[i] = (1 + x * dfs(i-2) + y * dfs(i-1)) % mod
    return dp[i]


print(dfs(n))
