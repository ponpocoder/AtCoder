n = int(input())
a = list(map(int, input().split()))

INF = 1001001001
res = -INF
for i in range(n):
    ca = -INF
    ct = -INF
    for j in range(n):
        if i == j:
            continue
        if j > i:
            b = a[i:j+1]
        else:
            b = a[j:i+1]
        tt, ta = 0, 0
        for k in range(len(b)):
            if k % 2:
                ta += b[k]
            else:
                tt += b[k]
        if ta > ca:
            ca = ta
            ct = tt
    res = max(res, ct)

print(res)
