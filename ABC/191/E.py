from heapq import heappush, heappop
n, m = map(int, input().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append((b, c))

for i in range(n):
    heap = []
    dist = [float("inf")] * n
    for j, c in graph[i]:
        heappush(heap, (c, j))

    while heap:
        d, curr = heappop(heap)
        if dist[curr] != float("inf"):
            continue
        dist[curr] = d
        for dest, nd in graph[curr]:
            heappush(heap, (d+nd, dest))

    if dist[i] != float("inf"):
        print(dist[i])
    else:
        print(-1)