n = int(input())
a = list(map(int, input().split()))

l, r = 0, 0
res = 0
while l < n:
    while r < n - 1 and a[r+1] > a[r]:
        r += 1

    res += r - l + 1
    if r == l:
        r += 1
    l += 1

print(res)
