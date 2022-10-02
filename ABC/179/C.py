n = int(input())


def check(i):
    l, r = 0, n
    while l < r - 1:
        m = (l + r) // 2
        if i * m >= n:
            r = m
        else:
            l = m
    return l


res = 0
for i in range(1, n):
    j = check(i)
    res += j

print(res)
# n = int(input())
# mod = 10**9+7

# def powmod(a, b, mod):
#     if b == 0:
#         return 1
#     curr = powmod(a, b//2, mod)
#     curr *= curr
#     if b % 2:
#         curr *= a
#     return curr % mod

# res = powmod(10, n, mod)
# res -= powmod(9, n, mod) * 2
# res += powmod(8, n, mod)

# print(res%mod)
