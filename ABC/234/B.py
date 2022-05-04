n = int(input())
cords = []

for _ in range(n):
    x, y = map(int, input().split())
    cords.append((x, y))

res = 0
for i in range(n - 1):
    x1, y1 = cords[i]
    for j in range(i+1, n):
        x2, y2 = cords[j]
        dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        res = max(res, dist)

print(res)