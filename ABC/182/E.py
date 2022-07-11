import sys
sys.setrecursionlimit(10**5)

h, w, n, m = map(int, input().split())

light = [[False] * w for _ in range(h)]
block = [[False] * w for _ in range(h)]


for _ in range(n):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    light[a][b] = True

for _ in range(m):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    block[c][d] = True

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
memo = [[False] * w for _ in range(h)]
res = [[False] * w for _ in range(h)]

def dfs(i, r, c):
    if r < 0 or r >= h or c < 0 or c >= w or block[r][c]:
        return False
    if light[r][c]:
        return True
    if visited[r][c]:
        return memo[r][c]

    memo[r][c] = dfs(i, r+dx[i], c+dy[i])
    visited[r][c] = True
    
    return memo[r][c]

for i in range(4):
    visited = [[False] * w for _ in range(h)]
    for j in range(h):
        for k in range(w):
            if dfs(i, j, k):
                res[j][k] = True

cnt = 0
for i in range(h):
    for j in range(w):
        if res[i][j]:
            cnt += 1

print(cnt)