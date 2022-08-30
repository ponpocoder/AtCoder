from heapq import heappush, heappop

n, m, t = map(int, input().split())
a = list(map(int, input().split()))

graph = [[] for _ in range(n)]
graph2 = [[] for _ in range(n)]

for _ in range(m):
    b, c, d = map(int, input().split())
    b -= 1
    c -= 1
    graph[b].append((c, d))
    graph2[c].append((b, d))


def djikstra(g):
    dist = [float("inf")] * n
    heap = [(0, 0)]

    while heap:
        cd, curr = heappop(heap)
        if dist[curr] != float("inf"):
            continue
        dist[curr] = cd
        for dest, nd in g[curr]:
            heappush(heap, (cd+nd, dest))

    return dist


res = 0
x = djikstra(graph)
y = djikstra(graph2)

res = 0
for i in range(n):
    curr = t - x[i] - y[i]
    res = max(res, curr*a[i])

print(res)
