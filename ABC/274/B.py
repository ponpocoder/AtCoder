h, w = map(int, input().split())
c = [list(input()) for _ in range(h)]
     
res = []

for i in range(w):
    curr = 0
    for j in range(h):
        if c[j][i] == "#":
            curr += 1
    res.append(curr)

print(*res)
