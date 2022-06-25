from math import ceil
n = int(input())
xy = []
p = []

for _ in range(n):
    x, y, z = map(int, input().split())
    xy.append((x, y))
    p.append(z)

curr = 0
dist = [[float("inf")] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        x, y = xy[i]
        nx, ny = xy[j]
        curr = abs(x-nx) + abs(y-ny)
        curr /= p[i]
        dist[i][j] = ceil(curr)
for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], max(dist[i][k], dist[k][j]))

res = float("inf")
for i in range(n):
    curr = 0
    for j in range(n):
        curr = max(curr, dist[i][j])    
    res = min(res, curr)

print(res)