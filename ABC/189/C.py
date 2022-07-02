n = int(input())
a = list(map(int, input().split()))

res = 0
for l in range(n):
    mn = 10**6
    for r in range(l, n):
        mn = min(mn, a[r])
        curr = (r - l + 1) * mn
        res = max(res, curr)

print(res)