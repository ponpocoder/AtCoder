from heapq import heappop, heappush

h, w, t = map(int, input().split())
INF = 1001001001
l, r = 0, 10**9+1

s = [list(input()) for _ in range(h)]

sr, sc = 0, 0
er, ec = 0, 0
for i in range(h):
    for j in range(w):
        if s[i][j] == "S":
            sr, sc = i, j
        if s[i][j] == "G":
            er, ec = i, j


def solve(x):
    dist = [[INF] * w for _ in range(h)]
    dist[sr][sc] = 0
    q = []
    q.append((sr, sc, 0))

    while q:
        cr, cc, cd = heappop(q)
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = cr+dx, cc+dy
            if 0 <= nr < h and 0 <= nc < w:
                if s[nr][nc] == "#":
                    y = x
                else:
                    y = 1
                if dist[nr][nc] > dist[cr][cc] + y:
                    dist[nr][nc] = dist[cr][cc] + y
                    heappush(q, (nr, nc, cd+y))
    return dist[er][ec] <= t
        

while l + 1 < r:
    m = (l + r) // 2
    if solve(m):
        l = m
    else:
        r = m

print(l)
