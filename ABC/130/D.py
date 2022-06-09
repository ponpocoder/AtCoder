n, k = map(int, input().split())
a = list(map(int, input().split()))

l, r = 0, 0
curr = 0
res = 0

while l < n:
    while r < n and curr < k:
        curr += a[r]
        r += 1
    if curr >= k:
        res += n - r + 1
    curr -= a[l]
    l += 1

print(res)