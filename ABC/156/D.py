n, a, b = map(int, input().split())
mod = 10**9+7

def power(a, b):
    if b == 0:
        return 1
    c = power(a, b//2)
    c *= c  
    if b & 1:
        c *= a
    return c % mod

def choose(a, b):
    deno = 1
    for i in range(1,b+1):
        deno *= i
        deno %= mod
    nume = 1
    for i in range(a-b+1, a+1):
        nume *= i
        nume %= mod
    inv = power(deno, mod-2)
    return nume * inv % mod

res = power(2, n) - choose(n, a) - choose(n, b) - 1
print(res%mod)
