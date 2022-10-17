n = int(input())
a = list(map(int, input().split()))
b = list(set(a))
b.sort()

def binarySearch(x):
    l, r = -1, len(b)
    while l + 1 < r:
        m = (l + r) // 2
        if b[m] == x:
            return len(b)-1-m
        elif b[m] < x:
            l = m
        else:
            r = m
    return -1

cnt = [0] * n
for i in range(n):
    curr = binarySearch(a[i])
    cnt[curr] += 1
for k in range(n):
    print(cnt[k])
