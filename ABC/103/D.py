n, m = map(int, input().split())
edges = []

for _ in range(m):
    a, b = map(int, input().split())
    edges.append((a, b))

edges.sort(key=lambda x: x[1])

cnt = 1
cr = edges[0][1]

for i in range(1, m):
    nl, nr = edges[i]
    if nl >= cr:
        cr = nr
        cnt += 1

print(cnt)
