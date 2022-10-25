n, x, y = map(int, input().split())
a = list(map(int, input().split()))
sx = set()
sx.add(a[0])
sy = set()
sy.add(0)

for i in range(1, n):
    t = set()
    if i % 2:
        for cy in sy:
            t.add(cy+a[i])
            t.add(cy-a[i])
            sy = t
    else:
        for cx in sx:
            t.add(cx+a[i])
            t.add(cx-a[i])
            sx = t

print("Yes" if x in sx and y in sy else "No")
