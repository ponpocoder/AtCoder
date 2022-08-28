from collections import deque

h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]
t = []
for r in s:
    t.append(r.copy())


def valid(r, c):
    flag = True
    if r > 0 and s[r-1][c] == ".":
        flag = False
    if r < h-1 and s[r+1][c] == ".":
        flag = False
    if c > 0 and s[r][c-1] == ".":
        flag = False
    if c < w-1 and s[r][c+1] == ".":
        flag = False
    if r > 0 and c > 0 and s[r-1][c-1] == ".":
        flag = False
    if r > 0 and c < w-1 and s[r-1][c+1] == ".":
        flag = False
    if r < h-1 and c > 0 and s[r+1][c-1] == ".":
        flag = False
    if r < h-1 and c < w-1 and s[r+1][c+1] == ".":
        flag = False
    return flag


def change(r, c, x):
    if r > 0:
        s[r-1][c] = x
    if r < h-1:
        s[r+1][c] = x
    if c > 0:
        s[r][c-1] = x
    if c < w-1:
        s[r][c+1] = x
    if r > 0 and c > 0:
        s[r-1][c-1] = x
    if r > 0 and c < w-1:
        s[r-1][c+1] = x
    if r < h-1 and c > 0:
        s[r+1][c-1] = x
    if r < h-1 and c < w-1:
        s[r+1][c+1] = x


q = deque()
for i in range(h):
    for j in range(w):
        if s[i][j] == ".":
            q.append((i, j))

for _ in range(len(q)):
    r, c = q.popleft()
    change(r, c, ".")

u = []
for r in s:
    u.append(r.copy())

for i in range(h):
    for j in range(w):
        if s[i][j] == "#":
            q.append((i, j))

for _ in range(len(q)):
    r, c = q.popleft()
    change(r, c, "#")

# for r in s:
#     print("".join(r))
# for r in t:
#     print("".join(r))

for i in range(h):
    for j in range(w):
        if s[i][j] != t[i][j]:
            print("impossible")
            exit()

print("possible")
for r in u:
    print("".join(r))
