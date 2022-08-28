x = int(input())

l, r = 1, 10**9

while l <= r:
    m = (l+r)//2
    if m**4 == x:
        print(m)
        exit()
    elif m**4 > x:
        r = m - 1
    else:
        l = m + 1
