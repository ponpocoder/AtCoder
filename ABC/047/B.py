w, h, n = map(int, input().split())
minX, minY, maxX, maxY = 0, 0, w, h

for _ in range(n):
    x, y, a = map(int, input().split())
    if a == 1:
        minX = max(minX, x)
    elif a == 2:
        maxX = min(maxX, x)
    elif a == 3:
        minY = max(minY, y)
    else:
        maxY = min(maxY, y)

res = max(maxX-minX, 0)*max(maxY-minY, 0)

print(res)
