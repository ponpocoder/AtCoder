n = int(input())
mod = 10**9+7

def powmod(a, b, mod):
    if b == 0:
        return 1
    curr = powmod(a, b//2, mod)
    curr *= curr
    if b % 2:
        curr *= a
    return curr % mod

res = powmod(10, n, mod)
res -= powmod(9, n, mod) * 2
res += powmod(8, n, mod)

print(res%mod)