k = int(input())
a = []

for i in range(1, 10):
    a.append(i)

while True:
    if k <= len(a):
        print(a[k-1])
        exit()

    k -= len(a)
    na = []
    for v in a:
        for i in [-1, 0, 1]:
            d = v % 10 + i
            if d < 0 or d > 9:
                continue
            nx = v*10 + d
            na.append(nx)
    a = na
