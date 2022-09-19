n = int(input())
mod = 10**9 + 7


def powmod(a, b, mod):
    if b == 0:
        return 1
    curr = powmod(a, b//2, mod)
    curr *= curr
    if b % 2:
        curr *= a
    return curr % mod


def comb(n, r):
    return (fact[n] * inv[n-r] * inv[r]) % mod


fact = [1, 1]
inv = [1, 1]
for i in range(2, n+1):
    fact.append(fact[-1] * i % mod)
    inv.append(powmod(fact[-1], mod-2, mod))

for k in range(1, n+1):
    curr = 0
    mx = (n+k-1) // k
    for i in range(1, mx+1):
        curr += comb(n-(k-1)*(i-1), i)
        curr %= mod

    print(curr)
