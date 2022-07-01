h, w = map(int, input().split())
c = [list(map(int, input().split())) for _ in range(10)]
a = [list(map(int, input().split())) for _ in range(h)]

table = c.copy()
for k in range(10):
    for i in range(10):
        for j in range(10):
            table[i][j] = min(table[i][j], table[i][k] + c[k][j])

cnt = 0
for row in a:
    for v in row:
        if v != -1:
            cnt += table[v][1]

print(cnt)