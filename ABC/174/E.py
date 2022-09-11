n, k = map(int, input().split())
a = list(map(int, input().split()))

l, r = 1, max(a)

while l < r:
    m = (l + r) // 2
    cnt = 0
    for v in a:
        cnt += (v-1) // m
    if cnt > k:
        l = m + 1
    else:
        r = m

print(l)
