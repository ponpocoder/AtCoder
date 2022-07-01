n = int(input())
a = list(map(int, input().split()))
mod = 10**9+7

digit = 60
res = 0
for i in range(digit):
    x = 0
    for j in range(n):
        if a[j] >> i & 1:
            x += 1
    res += x * (n - x) * 2**i
    res %= mod

print(res)