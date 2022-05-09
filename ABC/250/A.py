h, w = map(int, input().split())
r, c = map(int, input().split())

res = 0

if r > 1:
    res += 1
if r < h:
    res += 1
if c > 1:
    res += 1
if c < w:
    res += 1

print(res)