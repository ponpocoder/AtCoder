from heapq import heappop, heappush

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
INF = 1 << 60

for i in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append((b, c, i))
    graph[b].append((a, c, i))


def djikstra(i):
    dist = [INF] * n
    dist[i] = 0
    visited = [False] * n
    heap = [(0, i, -1)]
    while heap:
        cd, curr, ci = heappop(heap)
        if visited[curr]:
            continue
        visited[curr] = True
        if ci != -1:
            used.add(ci)
        for dest, nd, ni in graph[curr]:
            if not visited[dest] and dist[curr] + nd < dist[dest]:
                dist[dest] = dist[curr] + nd
                heappush(heap, (dist[dest], dest, ni))


used = set()
for i in range(n):
    djikstra(i)

print(m - len(used))
