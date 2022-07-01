from collections import defaultdict
n = int(input())

cnt = defaultdict(int)
for i in range(1, n+1):
    e = i % 10
    while i:
        s = i
        i //= 10
    cnt[(s, e)] += 1

res = 0
for i in range(1, n+1):
    e = i % 10
    while i:
        s = i
        i //= 10
    res += cnt[(e, s)]

print(res)