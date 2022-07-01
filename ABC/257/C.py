n = int(input())
s = input()
w = list(map(int, input().split()))

a = []
c = []

for i in range(n):
    if s[i] == "0":
        c.append(w[i])
    else:
        a.append(w[i])

a.sort()
c.sort()
# print(a)
# print(c)

def binarySearch(target):
    l, r = 0, len(c) - 1
    while l <= r:
        m = (l + r) // 2
        if c[m] >= target:
            r = m - 1
        else:
            l = m + 1
    return l 

res = len(c)
for i, v in enumerate(a):
    l = len(a) - i
    r = binarySearch(v)
    res = max(res, l + r)

print(res)
