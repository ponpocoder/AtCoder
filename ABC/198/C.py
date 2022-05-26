import math
r, x, y = map(int, input().split())

d = (x**2 + y**2) ** 0.5

res = 0
if r == d:
    res = 1
elif d <= 2*r:
    res = 2
else:
    res = math.ceil(d / r)

print(res)
