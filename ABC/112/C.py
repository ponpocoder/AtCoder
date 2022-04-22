n = int(input())
cords = []

for _ in range(n):
    x, y, h = map(int, input().split())
    cords.append((x, y, h))

def getHeight(x, y, cx, cy, H):
    tempH = H - abs(x - cx) - abs(y - cy)
    return max(tempH, 0)

for cx in range(101):
    for cy in range(101):
        H = 0
        for x, y, h in cords:
            if h == 0:
                continue
            H = abs(x - cx) + abs(y - cy) + h
        for i in range(n):
            if getHeight(cords[i][0], cords[i][1], cx, cy, H) != cords[i][2]:
                break
            if i == n - 1:
                print(cx, cy, H)
