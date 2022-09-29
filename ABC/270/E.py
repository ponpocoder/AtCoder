n, k = map(int, input().split())
a = list(map(int, input().split()))


def check(x):
    cnt = 0
    for i in range(n):
        cnt += min(a[i], x)

    return cnt <= k


l, r = -1, k+1

while l + 1 < r:
    m = (l + r) // 2
    if check(m):
        l = m
    else:
        r = m

for i in range(n):
    if a[i] > l:
        a[i] -= l
        k -= l
    else:
        k -= a[i]
        a[i] = 0

for i in range(n):
    if a[i] and k:
        a[i] -= 1
        k -= 1

print(*a)
