n = int(input())
cords = []

for _ in range(n):
    x, y = map(int, input().split())
    cords.append((x, y))

a, b, c = [1], [0], [0]
d, e, f = [0], [1], [0]

m = int(input())
for _ in range(m):
    op = list(map(int, input().split()))

    if op[0] == 1:
        a.append(d[-1])
        b.append(e[-1])
        c.append(f[-1])
        d.append(-a[-2])
        e.append(-b[-2])
        f.append(-c[-2])
    elif op[0] == 2:
        a.append(-d[-1])
        b.append(-e[-1])
        c.append(-f[-1])
        d.append(a[-2])
        e.append(b[-2])
        f.append(c[-2])
    elif op[0] == 3:
        p = op[1]
        a.append(-a[-1])
        b.append(-b[-1])
        c.append(2*p-c[-1])
        d.append(d[-1])
        e.append(e[-1])
        f.append(f[-1])
    else:
        p = op[1]
        a.append(a[-1])
        b.append(b[-1])
        c.append(c[-1])
        d.append(-d[-1])
        e.append(-e[-1])
        f.append(2*p-f[-1])

q = int(input())
for _ in range(q):
    s, t = map(int, input().split())
    t -= 1
    x, y = cords[t]
    nx = a[s]*x + b[s]*y + c[s]
    ny = d[s]*x + e[s]*y + f[s]

    print(nx, ny)