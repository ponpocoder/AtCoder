from heapq import heapify, heappush, heappop

n, m = map(int, input().split())
h = list(map(int, input().split()))

graph = [[] for _ in range(n)]

for i in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append(v)
    graph[v].append(u)

dist = [float("inf")] * n
visited = [False] * n
dist[0] = 0
heap = [(0, 0)]

while heap:
    d, curr = heappop(heap)
    visited[curr] = True
    for dest in graph[curr]:
        cost = max(0, h[dest] - h[curr])
        if dist[dest] > d + cost:
            dist[dest] = d + cost
            heappush(heap, (dist[dest], dest))
        
res = 0
for i in range(n):
    curr = h[0] - h[i] - dist[i]
    res = max(res, curr)

print(res)