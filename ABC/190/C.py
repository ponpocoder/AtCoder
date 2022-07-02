n, m = map(int, input().split())
a = []
b = []
c = []
d = []
for _ in range(m):
    e, f = map(int, input().split())
    a.append(e)
    b.append(f)

k = int(input())
for _ in range(k):
    g, h = map(int, input().split())
    c.append(g)
    d.append(h)

res = 0

for i in range(1<<k):
    dish = [0] * (n+1)
    for j in range(k):
        if i>>j&1:
            dish[c[j]] += 1
        else:
            dish[d[j]] += 1
    
    cnt = 0
    for j in range(m):
        if dish[a[j]] and dish[b[j]]:
            cnt += 1
    
    res = max(res, cnt)

print(res)