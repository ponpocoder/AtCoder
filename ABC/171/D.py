from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
q = int(input())

s = sum(a)
d = defaultdict(int)
for v in a:
    d[v] += 1

for _ in range(q):
    b, c = map(int, input().split())
    s += (c-b)*d[b]
    d[c] += d[b]
    d[b] = 0
    print(s)
