h, w = map(int, input().split())
a = [list(input()) for _ in range(h)]

rows = set()
cols = set()

for i in range(h):
    for j in range(w):
        if a[i][j] == "#":
            rows.add(i)
            cols.add(j)

res = []

for i in range(h):
    if i not in rows:
        continue
    curr = []
    for j in range(w):
        if j in cols:
            curr.append(a[i][j])
    res.append(curr)

for r in res:
    print("".join(r))