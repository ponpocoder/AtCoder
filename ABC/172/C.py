n, m, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

t = [0] * (m+1)

for i in range(1, m+1):
    t[i] = t[i-1] + b[i-1]

def binarySearch(target):
    l, r = 0, m
    while l <= r:
        mi = (l+r) // 2
        if t[mi] == target:
            return mi
        elif t[mi] < target:
            l = mi + 1
        else:
            r = mi - 1
    
    return l-1

res = 0
curr = 0
for i in range(n+1):
    j = binarySearch(k - curr)
    # print(i, j)
    res = max(res, i+j)
    if i == n:
        break
    curr += a[i]
    if curr > k:
        break

print(res)