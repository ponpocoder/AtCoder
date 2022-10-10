from collections import deque

n, m = map(int, input().split())

INF = 1001001001
cnt = [[INF] * n for _ in range(n)]

nodes = []
for a in range(400):
    for b in range(400):
        if a**2 + b**2 == m:
            nodes.append((a, b))
            nodes.append((-a, b))
            nodes.append((a, -b))
            nodes.append((-a, -b))


q = deque()
q.append((0, 0, 0))

while q:
    x, y, c = q.popleft()
    cnt[x][y] = c
    for dx, dy in nodes:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if cnt[nx][ny] > c + 1:
            cnt[nx][ny] = c + 1
            q.append((nx, ny, c+1))


for i in range(n):
    for j in range(n):
        if cnt[i][j] == INF:
            cnt[i][j] = -1

for i in range(n):
    print(*cnt[i])
