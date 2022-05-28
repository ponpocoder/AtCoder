n = int(input())
xy = []

for _ in range(n):
    xy.append(list(map(int, input().split())))

res = 0

for i in range(n):
    x1, y1 = xy[i]
    for j in range(i+1, n):
        x2, y2 = xy[j]
        for k in range(j+1, n):
            x3, y3 = xy[k]
            ox1, oy1 = x1 - x3, y1 - y3
            ox2, oy2 = x2 - x3, y2 - y3
            area = ox1*oy2 - ox2*oy1
            if area != 0:
                res += 1

print(res)