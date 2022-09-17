n = int(input())
a = list(map(int, input().split()))
a.sort()


def binarySearch(x):
    l, r = 0, n-1

    while l <= r:
        m = (l + r) // 2
        if x >= a[m]:
            l = m + 1
        else:
            r = m - 1

    return l


q = int(input())
for _ in range(q):
    b = int(input())
    x = binarySearch(b)
    if x == 0:
        res = a[x] - b
    elif x == n:
        res = b - a[x-1]
    else:
        res = min(a[x] - b, b - a[x-1])
    print(res)
