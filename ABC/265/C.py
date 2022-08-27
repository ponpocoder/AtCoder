h, w = map(int, input().split())
g = [input() for _ in range(h)]

visited = set()
cr, cc = 0, 0
while True:
    if (cr, cc) in visited:
        print(-1)
        exit()

    visited.add((cr, cc))
    c = g[cr][cc]
    if c == "U":
        if cr == 0:
            break
        cr -= 1
    elif c == "D":
        if cr == h-1:
            break
        cr += 1
    elif c == "L":
        if cc == 0:
            break
        cc -= 1
    else:
        if cc == w - 1:
            break
        cc += 1

print(cr+1, cc+1)
