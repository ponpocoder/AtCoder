n = int(input())
mod = 998244353
length = len(str(n))
K = n - 10 ** (length - 1) + 1
res = K * (K + 1) // 2

for i in range(length - 1):
    K = 9*10**i
    res += K * (K + 1) // 2

print(res % mod)