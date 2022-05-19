from collections import deque

n = int(input())
ax, ay = map(int, input().split())
bx, by = map(int, input().split())
ax -= 1
ay -= 1
bx -= 1
by -= 1
s = [input() for _ in range(n)]
inf = 100100100
dist = [[[inf] * 4 for _ in range(n)] for _ in range(n)]

dx = [1, 1, -1, -1]
dy = [1, -1, 1, -1]

q = deque()
q.append((ax, ay, 1))

while q:
    x, y, d = q.popleft()
    for i in range(4):
        nextX, nextY = x, y
        while True:
            nextX += dx[i]
            nextY += dy[i]
            if nextX < 0 or nextX >= n or nextY < 0 or nextY >= n or \
                dist[nextX][nextY][i] != inf or s[nextX][nextY] == "#":
                break

            dist[nextX][nextY][i] = d
            q.append((nextX, nextY, d + 1))

res = min(dist[bx][by])

if res != inf:
    print(res)
else:
    print(-1)

