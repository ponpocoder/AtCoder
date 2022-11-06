# TLE
from collections import deque
import sys
sys.setrecursionlimit(10**9)

h, w = map(int, input().split())
g = [list(input()) for _ in range(h)]
s = [[0] * w for _ in range(h)]
sr, sc = -1, -1

for i in range(h):
    for j in range(w):
        if g[i][j] == "S":
            sr, sc = i, j

x = [0, 0, 1, -1]
y = [1, -1, 0, 0]
visited = [[False] * w for _ in range(h)]


def dfs(r, c, d):
    if r < 0 or r >= h or c < 0 or c >= w or g[r][c] == "#":
        return False
    if r == sr and c == sc and d >= 4:
        return True
    if visited[r][c]:
        return False
    s[r][c] = d
    visited[r][c] = True
    res = False
    for dx, dy in zip(x, y):
        nr, nc = r+dx, c+dy
        if nr < 0 or nr >= h or nc < 0 or nc >= w or g[nr][nc] == "#":
            continue
        res |= dfs(nr, nc, d+1)
    return res


if dfs(sr, sc, 0):
    print("Yes")
else:
    print("No")
