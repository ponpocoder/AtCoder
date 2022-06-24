h, w = map(int, input().split())
s = [input() for _ in range(h)]

cnt = [[0] * w for _ in range(h)]

for i in range(h):
    visited = [False] * w
    for j in range(w):
        if s[i][j] == "#" or visited[j]:
            continue
        l = 0
        while j + l < w:
            if s[i][j+l] == "#":
                break
            l += 1
        for k in range(l):
            cnt[i][j+k] += l
            visited[j+k] = True

for i in range(w):
    visited = [False] * h
    for j in range(h):
        if s[j][i] == "#" or visited[j]:
            continue
        l = 0
        while j + l < h:
            if s[j+l][i] == "#":
                break
            l += 1
        for k in range(l):
            cnt[j+k][i] += l
            visited[j+k] = True

res = 0
for i in range(h):
    for j in range(w):
        res = max(res, cnt[i][j] - 1)

print(res)