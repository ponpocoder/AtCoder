h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]

res = 0

for i in range(h):
    for j in range(i, h):
        for k in range(w):
            for l in range(k, w):
                if a[i][k] + a[j][l] > a[j][k] + a[i][l]:
                    print("No")
                    exit()

print("Yes")