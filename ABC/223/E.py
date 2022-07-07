x, y, a, b, c = map(int, input().split())

def ceil(a, b):
    return (a+b-1)//b

def can3(x, y, a, b, c):
    w = ceil(a, y)
    if w >= x:
        return False
    x -= w
    return can2(x, y, b, c) or can2(y, x, b, c)

def can2(x, y, a, b):
    nw = ceil(a, y) + ceil(b, y)
    return nw <= x

for i in range(2):
    for j in range(3):
        if can3(x, y, a, b, c):
            print("Yes")
            exit()
        a, b, c = b, c, a
    x, y = y, x

print("No")
