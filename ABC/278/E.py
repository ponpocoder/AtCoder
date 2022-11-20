from collections import defaultdict

H, W, N, h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(H)]

x = defaultdict(int)
for i in range(H):
    for j in range(W):
        x[a[i][j]] += 1

res = []
for i in range(H-h+1):
    dic = x.copy()
    y = []
    for r in range(h):
        for c in range(w):
            dic[a[i+r][c]] -= 1
            if dic[a[i+r][c]] == 0:
                dic.pop(a[i+r][c])
    for j in range(W-w+1):
        # print(dic)
        y.append(len(dic))
        if j == W-w:
            break
        for k in range(h):
            dic[a[i+k][j]] += 1
        for k in range(h):
            dic[a[i+k][j+w]] -= 1
            if dic[a[i+k][j+w]] == 0:
                dic.pop(a[i+k][j+w])
    res.append(y)

for re in res:
    print(*re)
