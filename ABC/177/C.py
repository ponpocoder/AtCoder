n = int(input())
a = list(map(int, input().split()))
mod = 10**9 + 7

s = sum(a) % mod
res = 0

for v in a:
    s -= v
    res += v * s
    res %= mod

print(res)
