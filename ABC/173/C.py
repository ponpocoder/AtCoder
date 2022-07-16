h, w, k = map(int, input().split())
c = [input() for _ in range(h)]

res = 0
for i in range(1<<h):
    for j in range(1<<w):
        cnt = 0
        for ni in range(h):
            for nj in range(w):
                if i>>ni & 1 or j>>nj & 1:
                    continue
                if c[ni][nj] == "#":
                    cnt += 1
        if cnt == k:
            res += 1

print(res)