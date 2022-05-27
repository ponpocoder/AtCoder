n = int(input())
a = list(map(int, input().split()))

res = 2 << 31

for i in range(1 << n - 1):
    o = 0
    xor = 0
    for j in range(n):
        o |= a[j]
        if (i >> j) & 1:
            xor ^= o
            o = 0
    xor ^= o
    res = min(res, xor)

print(res)