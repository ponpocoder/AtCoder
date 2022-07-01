x, y = map(int, input().split())
mod = 10**9+7

def power(a, n):
    if n == 0:
        return 1
    b = power(a, n//2)
    b *= b
    if n % 2 == 1:
        b *= a
    return b % mod

def choose(a, b):
    deno = 1
    for i in range(1, b+1):
        deno *= i
        deno %= mod
    nume = 1
    for i in range(a-b+1, a+1):
        nume *= i
        nume %= mod
    inv = power(deno, mod-2)
    return nume * inv % mod


n = (x+y) // 3

if (x+y) % 3 != 0:
    print(0)
else:
    x -= n
    y -= n
    if x < 0 or y < 0:
        print(0)
    else:
        print(choose(x+y, x))
