from collections import deque

h, w = map(int, input().split())
s = [input() for _ in range(h)]

INF = 1001001001
dist = [[INF] * w for _ in range(h)]
dist[0][0] = 0
visited = [[False] * w for _ in range(h)]

q = deque()
q.append((0, 0))
x = [0, 0, 1, -1]
y = [1, -1, 0, 0]

while q:
    r, c = q.popleft()
    if visited[r][c]:
        continue
    visited[r][c] = True
    cd = dist[r][c]
    for dx, dy in zip(x, y):
        nc = c + dx
        nr = r + dy
        if nr < 0 or nr >= h or nc < 0 or nc >= w or s[nr][nc] == "#" or dist[nr][nc] <= cd:
            continue
        dist[nr][nc] = cd
        q.appendleft((nr, nc))

    for i in range(-2, 3):
        for j in range(-2, 3):
            if abs(i) + abs(j) > 3:
                continue
            nr = r + i
            nc = c + j
            if nr < 0 or nr >= h or nc < 0 or nc >= w or dist[nr][nc] <= cd+1:
                continue
            dist[nr][nc] = cd + 1
            q.append((nr, nc))

print(dist[-1][-1])
