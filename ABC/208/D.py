n, m = map(int, input().split())
inf = float("inf")
dist = [[inf] * n for _ in range(n)]

for i in range(n):
    dist[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    dist[a][b] = c

res = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            dist[j][k] = min(dist[j][k], dist[j][i] + dist[i][k])
            if dist[j][k] != inf:
                res += dist[j][k]
print(res)