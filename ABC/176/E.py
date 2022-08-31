h, w, m = map(int, input().split())
s = [0] * h
t = [0] * w
u = set()
for _ in range(m):
    x, y = map(int, input().split())
    s[x-1] += 1
    t[y-1] += 1
    u.add((x-1, y-1))

mr = max(s)
mc = max(t)
rows = []
cols = []
for i in range(h):
    if s[i] == mr:
        rows.append(i)
for j in range(w):
    if t[j] == mc:
        cols.append(j)

res = mr + mc

for r in rows:
    for c in cols:
        if (r, c) not in u:
            print(res)
            exit()

print(res-1)
