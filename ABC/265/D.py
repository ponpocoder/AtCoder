n, p, q, r = map(int, input().split())
a = list(map(int, input().split()))

s = [0] * (n+1)
for i in range(1, n+1):
    s[i] = s[i-1] + a[i-1]


def binarySearch(x, target):
    left, right = x, n

    while left <= right:
        m = (left+right) // 2
        curr = s[m] - s[x]
        if curr == target:
            return m
        elif curr < target:
            left = m + 1
        else:
            right = m - 1

    return -1


for i in range(n):
    r1 = binarySearch(i, p)
    if r1 != -1:
        r2 = binarySearch(r1, q)
        if r2 != -1:
            r3 = binarySearch(r2, r)
            if r3 != -1:
                print("Yes")
                exit()

print("No")
