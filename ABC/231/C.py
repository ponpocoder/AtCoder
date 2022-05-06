n, q = map(int, input().split())

a = list(map(int, input().split()))
a.sort()


def binarySearch(x):
    l, r = 0, len(a) - 1
    res = 0
    while l <= r:
        m = (l + r) // 2
        if a[m] >= x:
            res = len(a) - m
            r = m - 1
        else:
            l = m + 1
    print(res)

x = []
for _ in range(q):
    curr = int(input())
    x.append(curr)

for y in x:
    binarySearch(y)