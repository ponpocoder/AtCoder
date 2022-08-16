from collections import defaultdict

n = int(input())
a = []

for _ in range(n):
    a.append(int(input()))

b = sorted(a)
curr = 0
g = defaultdict(int)

for v in b:
    if v in g:
        continue
    g[v] = curr
    curr += 1

for i in range(n):
    print(g[a[i]])
