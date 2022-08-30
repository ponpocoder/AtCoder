d, g = map(int, input().split())
p = []
c = []

for _ in range(d):
    a, b = map(int, input().split())
    p.append(a)
    c.append(b)

res = float("inf")
for i in range(1 << d):
    curr = 0
    cnt = 0
    for j in range(d):
        if (i >> j) & 1:
            curr += 100 * (j+1) * p[j] + c[j]
            cnt += p[j]

    if curr >= g:
        res = min(res, cnt)
    else:
        for k in range(d-1, -1, -1):
            if (i >> k) & 1:
                continue
            for _ in range(p[k]):
                if curr >= g:
                    break
                curr += 100 * (k + 1)
                cnt += 1
        res = min(res, cnt)

print(res)
