k, a, b = map(int, input().split())

res = 0
if b - a > 2:
    t = max((k - a + 1) // 2, 0)
    curr = 1 + t * (b - a) + k - t * 2
    res = max(curr, 1 + k)
else:
    res = 1 + k

print(res)