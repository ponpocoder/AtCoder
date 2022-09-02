h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]

mn = 100

for i in range(h):
    for j in range(w):
        mn = min(mn, a[i][j])

cnt = 0
for i in range(h):
    for j in range(w):
        cnt += max(0, a[i][j]-mn)

print(cnt)
