n = int(input())
cords = []

for _ in range(n):
    x, y = map(int, input().split())
    cords.append((x, y))

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            x1, y1 = cords[i]
            x2, y2 = cords[j]
            x3, y3 = cords[k]
            dx = x2 - x1
            dy = y2 - y1
            dx2 = x3 - x1
            dy2 = y3 - y1
            if dx * dy2 == dx2 * dy:
                print("Yes")
                exit()

print("No")
