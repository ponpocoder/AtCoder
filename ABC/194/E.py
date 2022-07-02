from collections import defaultdict

n, m = map(int, input().split())
a = list(map(int, input().split()))

d = defaultdict(int)

for i in range(m):
    d[a[i]] += 1

res = 0
for i in range(m+1):
    if d[i] == 0:
        res = i
        break

for i in range(n-m):
    d[a[m+i]] += 1
    d[a[i]] -= 1
    if d[a[i]] == 0:
        res = min(res, a[i])

print(res)