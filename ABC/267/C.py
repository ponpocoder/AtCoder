n, m = map(int, input().split())
a = list(map(int, input().split()))

curr = 0
s = 0
for i in range(m):
    curr += a[i] * (i+1)
    s += a[i]

res = curr
for i in range(m, n):
    curr = curr - s + m * a[i]
    s = s - a[i-m] + a[i]
    res = max(res, curr)

print(res)
