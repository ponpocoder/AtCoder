x, y, z = map(int, input().split())
res = -1
if abs(x) <= abs(y):
    res = abs(x)
elif x * y < 0:
    res = abs(x)
else:
    if abs(z) <= abs(y):
        res = abs(z) + abs(z-x)
    else:
        res = -1
print(res)
