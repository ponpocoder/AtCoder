from collections import deque

h, w = map(int, input().split())
a = [list(input()) for _ in range(h)]

cnt = h*w
res = 0
q = deque()

for i in range(h):
    for j in range(w):
        if a[i][j] == "#":
            a[i][j] = "."
            q.append((i, j))

while q and cnt > 0:
    res += 1
    for i in range(len(q)):
        r, c = q.popleft()
        if r < 0 or r >= h or c < 0 or c >= w or a[r][c] == "#":
            continue
        a[r][c] = "#"
        cnt -= 1
        
        q.append((r+1, c))
        q.append((r-1, c))
        q.append((r, c+1))
        q.append((r, c-1))

print(res - 1 if res > 0 else 0)