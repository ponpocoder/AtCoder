import math

n = int(input())

pairs = []
for _ in range(n):
    x, y = map(int, input().split())
    pairs.append((x, y))

magic = set()
for i in range(n):
    x1, y1 = pairs[i]
    for j in range(n):
        if i == j:
            continue
        x2, y2 = pairs[j]
        xDiff = x2 - x1
        yDiff = y2 - y1
        gcd = math.gcd(xDiff, yDiff)
        magic.add((xDiff//gcd, yDiff//gcd))

print(len(magic))