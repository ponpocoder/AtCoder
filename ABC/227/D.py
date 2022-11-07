n, k = map(int, input().split())
a = list(map(int, input().split()))

l, r = 0, 10**18


def check(m):
    x = a.copy()
    for i in range(n):
        if x[i] > m:
            x[i] = m
    return sum(x) >= k*m


while l + 1 < r:
    m = (l + r) // 2
    if check(m):
        l = m
    else:
        r = m

print(l)
