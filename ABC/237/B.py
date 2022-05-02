h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]

for i in range(w):
    curr = []
    for j in range(h):
        curr.append(a[j][i])
    print(*curr)
    