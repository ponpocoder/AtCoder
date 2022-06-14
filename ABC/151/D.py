from collections import deque

h, w = map(int, input().split())
s = [input() for _ in range(h)]

def bfs(i, j):
    visited = [[False] * w for _ in range(h)]
    q = deque()
    q.append((i, j, 0))
    curr = 0
    while q:
        r, c, d = q.popleft()
        if r < 0 or r >= h or c < 0 or c >= w or visited[r][c] or s[r][c] == "#":
            continue
        visited[r][c] = True
        curr = max(curr, d)
        q.append((r+1, c, d+1))
        q.append((r-1, c, d+1))
        q.append((r, c+1, d+1))
        q.append((r, c-1, d+1))

    return curr

res = 0
for i in range(h):
    for j in range(w):
        res = max(res, bfs(i, j))

print(res)