n, m, k = map(int, input().split())
mod = 998244353


def powmod(a, b, mod):
    if b == 0:
        return 1
    curr = powmod(a, b//2, mod)
    curr *= curr
    if b % 2:
        curr *= a
    return curr % mod


res = 0
comb = 1
for i in range(k+1):
    res += comb * m * powmod(m-1, n-1-i, mod)
    res %= mod
    comb *= (n-i-1) * powmod(i+1, mod-2, mod)
    comb %= mod

print(res)

# import sys
# sys.setrecursionlimit(10**6)
# n, m, k = map(int, input().split())
# mod = 998244353
# dp = [0] * n


# def dfs(i, x):
#     if i == n:
#         return 1

#     curr = 0
#     if i == 0:
#         curr += m * dfs(i+1, x)
#     else:
#         if x > 0:
#             curr += dfs(i+1, x-1)
#         curr += (m-1) * dfs(i+1, x)
#     curr %= mod
#     dp[i] = curr
#     return dp[i]


# print(dfs(0, k))
