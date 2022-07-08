h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]
op = []
for i in range(h):
    for j in range(w):
        if i == h - 1:
            if a[i][j] % 2 and j != w-1:
                a[i][j] -= 1
                a[i][j+1] += 1
                op.append((i+1, j+1, i+1, j+2))
        else:
            if a[i][j] % 2:
                a[i][j] -= 1
                a[i+1][j] += 1
                op.append((i+1, j+1, i+2, j+1))

print(len(op))
for r in op:
    print(*r)