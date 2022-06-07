from collections import deque

n = int(input())
a = list(map(int, input().split()))

res = deque()
for i in range(n):
    if i & 1:
        res.append(a[i])
    else:
        res.appendleft(a[i])

if i & 1:
    res.reverse()
    print(*res)
else:
    print(*res)
