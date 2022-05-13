from collections import deque
n, m = map(int, input().split())
A = []
cnt = [0] * (n+1)
pos = [[] for _ in range(n+1)]
q = deque()

for i in range(m):
    k = int(input())
    a = list(map(int, input().split()))
    curr = a.pop()
    A.append(a)
    pos[curr].append(i)
    cnt[curr] += 1
    if cnt[curr] == 2:
        q.append(curr)

res = 0
while q:
    x, y = pos[q.popleft()]
    res += 1
    if A[x]:
        curr = A[x].pop()
        cnt[curr] += 1
        pos[curr].append(x)
        if cnt[curr] == 2:
            q.append(curr)
    if A[y]:
        curr = A[y].pop()
        cnt[curr] += 1
        pos[curr].append(y)
        if cnt[curr] == 2:
            q.append(curr)

if res == n:
    print("Yes")
else:
    print("No")