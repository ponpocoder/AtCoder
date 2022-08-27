import sys
sys.setrecursionlimit(10**6)

w, h = map(int, input().split())
mod = 10**9 + 7


def powmod(a, b, mod):
    if b == 0:
        return 1
    curr = powmod(a, b//2, mod)
    curr *= curr
    if b % 2:
        curr *= a
    return curr % mod


def permod(x, mod):
    if x == 0:
        return 1
    return x * permod(x-1, mod) % mod


a = permod(h+w-2, mod)
b = permod(h-1, mod) * permod(w-1, mod)
c = powmod(b, mod-2, mod)
print(a*c % mod)

# import sys
# sys.setrecursionlimit(10**5)

# w, h = map(int, input().split())
# memo = [[-1] * w for _ in range(h)]
# memo[0][0] = 1
# mod = 10**9 + 7


# def dfs(r, c):
#     if r < 0 or c < 0:
#         return 0
#     if memo[r][c] != -1:
#         return memo[r][c]

#     curr = 0
#     if r > 0:
#         curr += dfs(r-1, c)
#         curr %= mod
#     if c > 0:
#         curr += dfs(r, c-1)
#         curr %= mod

#     memo[r][c] = curr
#     return memo[r][c]


# print(dfs(h-1, w-1))
