n, m, k = map(int, input().split())

edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a-1, b-1, c))

INF = 10 ** 18
dist = [INF] * n
dist[0] = 0

e = list(map(int, input().split()))

for i in range(k):
    x = e[i]
    x -= 1
    a, b, c = edges[x]
    dist[b] = min(dist[b], dist[a] + c)

res = dist[n-1]
if res == INF:
    res = -1

print(res)
