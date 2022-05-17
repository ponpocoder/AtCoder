n, k = map(int, input().split())
a = list(map(int, input().split()))

l, r = -1, max(a) + 1

while l + 1 < r:
    m = (r + l) // 2
    s = 0
    for v in a:
        s += max(0, v - m)
    if s <= k:
        r = m - 1
    else:
        l = m + 1

res = 0
for v in a:
    if v >= r:
        res += (v + r) * (v - r + 1) // 2
        k -= v - r

res += k * r
print(res)