from math import factorial
n, m = map(int, input().split())
mod = 10**9 + 7

if abs(n - m) >= 2:
    res = 0
elif n == m:
    res = 2 * factorial(n) * factorial(m) % mod
else:
    res = factorial(n) * factorial(m) % mod

print(res)