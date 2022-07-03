n = int(input())
a = list(map(int, input().split()))
a.sort()

res = 0
s = 0
for i in range(1, n):
    s += a[i-1]
    res += a[i] * i- s

print(res)