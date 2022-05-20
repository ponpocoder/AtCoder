n, x, y = map(int, input().split())
a = list(map(int, input().split()))

def calc(b):
    l, r, cntX, cntY, res = 0, 0, 0, 0, 0

    while l < len(b):
        while r < len(b) and (cntX == 0 or cntY == 0):
            if b[r] == x:
                cntX += 1
            if b[r] == y:
                cntY += 1
            r += 1
        if cntX > 0 and cntY > 0:
            res += len(b) - r + 1
        if b[l] == x:
            cntX -= 1
        if b[l] == y:
            cntY -= 1
        l += 1

    return res
    
l, res = 0, 0
while l < n:
    b = []
    while l < n and y <= a[l] <= x:
        b.append(a[l])
        l += 1
    if len(b) != 0:
        res += calc(b)
    else:
        l += 1

print(res)
