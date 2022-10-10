n, m = map(int, input().split())

INF = 1001001001
dist = [[INF] * n for _ in range(n)]

for _ in range(m):
    a, b, t = map(int, input().split())
    a -= 1
    b -= 1
    dist[a][b] = t
    dist[b][a] = t

for i in range(n):
    dist[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

res = INF
for i in range(n):
    res = min(res, max(dist[i]))

print(res)
