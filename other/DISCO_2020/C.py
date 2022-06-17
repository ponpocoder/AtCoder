h, w, k = map(int, input().split())
s = [input() for _ in range(h)]

res = [[0] * w for _ in range(h)]

cnt = 1
for i in range(h):
    for j in range(w):
        if s[i][j] == "#":
            res[i][j] = cnt
            cnt += 1
    for j in range(1, w):
        res[i][j] = max(res[i][j], res[i][j-1])
    for j in range(w-2, -1, -1):
        if res[i][j] == 0:
            res[i][j] = res[i][j+1]

for j in range(w):
    for i in range(1, h):
        res[i][j] = max(res[i][j], res[i-1][j])
    for i in range(h-2, -1, -1):
        if res[i][j] == 0:
            res[i][j] = res[i+1][j]
            
for re in res:
    print(*re)