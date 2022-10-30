a, b, c, d, e, f = map(int, input().split())
mod = 998244353

x = a * b * c % mod
y = d * e * f % mod
res = x - y
print(res%mod)
