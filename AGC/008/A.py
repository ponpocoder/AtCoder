x, y = map(int, input().split())
res = 10**10

if x <= y:
    res = min(res, y-x)
if x >= -y:
    res = min(res, x+y+1)
if x <= -y:
    res = min(res, -y-x+1)
if x >= y:
    res = min(res, -y+x+2)

print(res)