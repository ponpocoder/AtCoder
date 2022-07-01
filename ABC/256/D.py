n = int(input())
a = []

for _ in range(n):
    l, r = map(int, input().split())
    a.append((l, r))


a.sort()

res = []
cs = a[0][0]
ce = a[0][1]

for i in range(1, n):
    ns, ne = a[i]
    if ns <= ce:
        ce = max(ce, ne)
    else:
        res.append([cs, ce])
        cs = ns
        ce = ne

res.append([cs, ce])
for re in res:
    print(*re)