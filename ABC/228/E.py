n, k, m = map(int, input().split())
mod = 998244353

def powmod(x, y, m):
    if y == 0:
        return 1
    curr = powmod(x, y//2, m)
    curr *= curr
    if y % 2:
        curr *= x
    return curr % m

r = powmod(k, n, mod-1)
res = powmod(m, r, mod)

if m % mod == 0:
    print(0)
else:
    print(res)