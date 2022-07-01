from collections import deque

n = int(input())
a = []

for _ in range(n):
    a.append(int(input()))

a.sort()
q = deque(a)
p = deque()

cnt = 0
while q:
    if cnt:
        p.append(q.pop())
    else:
        p.append(q.popleft())
    cnt ^= 1

if abs(p[0]-p[-1]) > abs(p[-1]-p[-2]):
    p.appendleft(p.pop())

s = list(p)
res1 = 0
for i in range(n-1):
    res1 += abs(s[i+1] - s[i])

q = deque(a)
p = deque()

cnt = 1
while q:
    if cnt:
        p.append(q.pop())
    else:
        p.append(q.popleft())
    cnt ^= 1

if abs(p[0]-p[-1]) > abs(p[-1]-p[-2]):
    p.appendleft(p.pop())

s = list(p)
res2 = 0
for i in range(n-1):
    res2 += abs(s[i+1] - s[i])

print(max(res1, res2))