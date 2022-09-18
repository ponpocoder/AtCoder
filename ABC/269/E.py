n = int(input())

row, column = 0, 0
for i in range(2):
    l, r = 0, n
    while l+1 < r:
        m = (l + r) // 2
        if i == 0:
            print("?", 1, m, 1, n)
        else:
            print("?", m, 1, n, 1)
        x = int(input())
        if x != m:
            r = m
        else:
            l = m
    if t == 0:
        row = r
    else:
        column = r


print("!", r, c)
