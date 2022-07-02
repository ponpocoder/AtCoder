from heapq import heappush, heappop
from math import ceil

n, m, x, y = map(int, input().split())
x -= 1
y -= 1

graph = [[] for _ in range(n)]

for _ in range(m):
    a, b, t, k = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append((b, t, k))
    graph[b].append((a, t, k))

heap = [(0, x)]
time = [float("inf")] * n

while heap:
    t, i = heappop(heap)
    if time[i] != float("inf"):
        continue
    time[i] = t
    for dest, dist, k in graph[i]:
        nt = ceil(t/k) * k
        heappush(heap, (nt + dist, dest))

print(time[y] if time[y] != float("inf") else -1)