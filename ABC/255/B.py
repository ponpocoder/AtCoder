n, k = map(int, input().split())
a = list(map(int, input().split()))
s = set(a)
xy = [[0, 0]]

for _ in range(n):
    x, y = map(int, input().split())
    xy.append([x, y])

mx = 0

for i in range(1, n+1):
    if i in s:
        continue
    curr = float("inf")
    for j in range(k):
        dx = abs(xy[i][0] - xy[a[j]][0])
        dy = abs(xy[i][1] - xy[a[j]][1])
        dist = (dx**2 + dy**2) ** 0.5
        curr = min(curr, dist)
    
    mx = max(mx, curr)

print(mx)