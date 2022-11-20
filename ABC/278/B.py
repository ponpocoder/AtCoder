h, m = list(map(int, input().split()))

for i in range(24):
    nh = str((h+i) % 24)
    if len(nh) < 2:
        nh = "0" + nh
    a, b = int(nh[0]), int(nh[1])
    for j in range(60):
        if i == 0:
            if m+j >= 60:
                break
            nm = str((m+j) % 60)
        else:
            nm = str(j)
        if len(nm) < 2:
            nm = "0" + nm
        c, d = int(nm[0]), int(nm[1])
        # print(a, b, c, d)
        x = a*10+c
        y = 10*b+d
        if x < 24 and (y < 60):
            print(10*a+b, 10*c+d)
            exit()
