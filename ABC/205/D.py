n, q = map(int, input().split())
a = list(map(int, input().split()))
c = [v-(i+1) for i, v in enumerate(a)] #c[i] :a[i]以下の使える整数の個数

def binarySearch(k):
    l, r = 0, len(a) - 1
    while l <= r:
        m = (l + r) // 2
        if c[m] < k:
            l = m + 1
        else:
            r = m - 1
    return l - 1

for _ in range(q):
    k = int(input())
    i = binarySearch(k)
    if i == -1:
        print(k)
    else:
        print(a[i] + k - c[i])
