n, m = map(int, input().split())
X, Y = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

c, d = 0, 0
t = 0
cnt = 0


def binarySearch(t):
    l, r = -1, n
    while l + 1 < r:
        m = (l + r) // 2
        if a[m] < t:
            l = m
        else:
            r = m
    return l + 1


def binarySearch2(t):
    l, r = -1, m
    while l + 1 < r:
        k = (l + r) // 2
        if b[k] < t:
            l = k
        else:
            r = k
    return l + 1


while True:
    x = binarySearch(t)
    if x == n:
        break
    t = a[x] + X
    y = binarySearch2(t)
    if y == n:
        break
    t = b[y] + Y
    cnt += 1

print(cnt)
