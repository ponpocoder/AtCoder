n, q = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
s = []
curr = 0
s.append(0)
for i in range(n):
    curr += a[i]
    s.append(curr)

def binarySearch(i):
    l, r = 0, n - 1

    while l <= r:
        m = (l + r) // 2
        if i >= a[m]:
            l = m + 1
        else:
            r = m - 1
    return l

for _ in range(q):
    x = int(input())
    idx = binarySearch(x)
    one = abs(x * idx - s[idx])
    two = abs(s[n]-s[idx] - x * (n - idx))
    print(one+two)