n, l, r = map(int, input().split())
a = list(map(int, input().split()))

res = r * n
suma = 0
sumb = 0
maxb = 0

for i in range(n):
    suma += a[i]
    sumb += a[i] - l
    maxb = max(maxb, sumb)
    curr = suma + r * (n-i-1) - maxb
    res = min(res, curr)

print(res)
