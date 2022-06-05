a, b, x = map(int, input().split())

def calc(n):
    return a * n + b * len(str(n))

l, r = 1, 10**9

while l <= r:
    m = (l + r) // 2
    curr = calc(m)
    if curr > x:
        r = m - 1
    else:
        l = m + 1

print(l-1)