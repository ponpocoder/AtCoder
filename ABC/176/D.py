from collections import deque

h, w = map(int, input().split())
cx, cy = map(int, input().split())
dx, dy = map(int, input().split())
cx -= 1
cy -= 1
dx -= 1
dy -= 1

s = [input() for _ in range(h)]

cnt = [[float("inf")] * w for _ in range(h)]

cnt[cx][cy] = 0

q = deque()
q.append((cx, cy))

while q:
    r, c = q.popleft()
    dist = cnt[r][c]
    nodes = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
    for i, j in nodes:
        if i < 0 or i >= h or j < 0 or j >= w or cnt[i][j] <= dist or s[i][j] == "#":
            continue
        cnt[i][j] = dist
        q.appendleft((i, j))
    for i in range(-2, 3):
        for j in range(-2, 3):
            ni, nj = r+i, c+j
            if ni < 0 or ni >= h or nj < 0 or nj >= w or cnt[ni][nj] <= dist + 1 or s[ni][nj] == "#":
                continue
            cnt[ni][nj] = dist + 1
            q.append((ni, nj))

print(cnt[dx][dy] if cnt[dx][dy] != float("inf") else -1)
