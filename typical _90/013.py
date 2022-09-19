from heapq import heappush, heappop

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


def djikstra(s):
    q = [(0, s)]
    dist = [-1] * (n+1)
    while q:
        cc, cd = heappop(q)
        if dist[cd] != -1:
            continue
        dist[cd] = cc
        for dest, nc in graph[cd]:
            if dist[dest] != -1:
                continue
            heappush(q, (cc+nc, dest))

    return dist


going = djikstra(1)
coming = djikstra(n)

for i in range(1, n+1):
    res = going[i] + coming[i]
    print(res)
