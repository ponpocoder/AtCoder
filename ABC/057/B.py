n, m = map(int, input().split())
curr = [list(map(int, input().split())) for _ in range(n)]
dest = [list(map(int, input().split())) for _ in range(m)]
res = []
for i in range(n):
    x1, y1 = curr[i]
    dist = float("inf")
    nxt = 0
    for j in range(m):
        x2, y2 = dest[j]
        d = abs(x1-x2) + abs(y1-y2)
        if d < dist:
            dist = d
            nxt = j+1
    res.append(nxt)

for r in res:
    print(r)
