from heapq import heapify, heappush, heappop

n, m = map(int, input().split())
roads = [[] for _ in range(n)]

for i in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    roads[a].append((b, c, i + 1))
    roads[b].append((a, c, i + 1))

dist = [float("inf")] * n
visited = [False] * n
dist[0] = 0

q = [(0, 0, 0)]

res = []

while q:
    d, curr, i = heappop(q)
    if not visited[curr]:
        visited[curr] = True
        dist[curr] = d
        res.append(i)
        for dest, nd, ni in roads[curr]:
            if not visited[dest] and dist[dest] > d + nd:
                heappush(q, (d + nd, dest, ni))

print(*res[1:])

