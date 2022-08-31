h, w, x, y = map(int, input().split())
s = [input() for _ in range(h)]

x -= 1
y -= 1

cnt = 1
cx = x + 1
while cx < h and s[cx][y] == ".":
    cnt += 1
    cx += 1

cx = x - 1
while cx >= 0 and s[cx][y] == ".":
    cnt += 1
    cx -= 1

cy = y + 1
while cy < w and s[x][cy] == ".":
    cnt += 1
    cy += 1

cy = y - 1
while cy >= 0 and s[x][cy] == ".":
    cnt += 1
    cy -= 1

print(cnt)
