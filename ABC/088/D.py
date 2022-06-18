from collections import deque

h, w = map(int, input().split())
s = [input() for _ in range(h)]

d = [[float("inf")] * w for _ in range(h)]

q = deque()
q.append((0, 0, 0))

while q:
    r, c, dist = q.popleft()
    if r < 0 or r >= h or c < 0 or c >= w or s[r][c] == "#" or d[r][c] != float("inf"):
        continue
    d[r][c] = dist + 1
    if r == h-1 and c == w-1:
        break
    q.append((r+1,c,dist+1))
    q.append((r-1,c,dist+1))
    q.append((r,c+1,dist+1))
    q.append((r,c-1,dist+1))

# print(d)
if d[h-1][w-1] == float("inf"):
    print(-1)
    exit()
else:
    visited = [[False] * w for _ in range(h)]
    cr, cc = h-1, w-1
    visited[0][0] = True
    while cr != 0 or cc != 0:
        visited[cr][cc] = True
        cd = d[cr][cc]
        if cr > 0 and d[cr-1][cc] == cd - 1:
            cr -= 1
        elif cc > 0 and d[cr][cc-1] == cd - 1:
            cc -= 1
        elif cr < h - 1 and d[cr+1][cc] == cd - 1:
            cr += 1
        elif cc < w - 1 and d[cr][cc+1] == cd - 1:
            cc += 1
# print(visited)
cnt = 0
for i in range(h):
    for j in range(w):
        if not visited[i][j] and s[i][j] == ".":
            cnt += 1

print(cnt)