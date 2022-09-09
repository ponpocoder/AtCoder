n = int(input())
cords = []

for _ in range(n):
    x, y = map(int, input().split())
    cords.append((x, y))

res = 0
for i in range(n):
    for j in range(i+1, n):
        x, y = cords[i]
        nx, ny = cords[j]

        dx = abs(x - nx)
        dy = abs(y - ny)
        if -dx <= dy <= dx:
            res += 1

print(res)
