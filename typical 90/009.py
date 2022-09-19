from math import degrees, atan2

n = int(input())
cords = []

for _ in range(n):
    a, b = map(int, input().split())
    cords.append((a, b))


def binarySearch(a, x):
    l, r = -1, n - 1
    while l + 1 < r:
        m = (l + r) // 2
        if a[m] <= x:
            l = m
        else:
            r = m

    return l


res = 0
for i in range(n):
    cx, cy = cords[i]
    curr = []
    for j in range(n):
        if i == j:
            continue
        nx, ny = cords[j]
        angle = degrees(atan2(nx - cx, ny - cy)) % 360
        curr.append(angle)

    curr.sort()
    for angle in curr:
        j = binarySearch(curr, (angle + 180) % 360)
        if j == 0:
            z = 180 - abs(180 - (angle - curr[0]))
            res = max(res, z)
        elif j == len(curr):
            z = 180 - abs(180 - (angle - curr[-1]))
            res = max(res, z)
        else:
            z1 = 180 - abs(180 - (angle - curr[j - 1]))
            z2 = 180 - abs(180 - (angle - curr[j]))
            res = max(res, z1, z2)
print(res)
