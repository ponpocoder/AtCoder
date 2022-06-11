r, c = map(int, input().split())
a = []

for _ in range(r):
    x, y = map(int, input().split())
    a.append([x, y])

print(a[r-1][c-1])