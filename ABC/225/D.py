n, q = map(int, input().split())

front = [None] * n
back = [None] * n

for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 3:
        x = query[1]
        x -= 1
        while front[x] is not None:
            x = front[x]
        res = []    
        while x is not None:
            res.append(x+1)
            x = back[x]

        print(len(res), *res)

    else:
        q = query[0]
        x, y = query[1], query[2]
        x -= 1
        y -= 1

        if q == 1:
            front[y] = x
            back[x] = y
        else:
            front[y] = None
            back[x] = None
