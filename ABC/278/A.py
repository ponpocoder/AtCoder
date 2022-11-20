from collections import deque

n, k = map(int, input().split())
a = list(map(int, input().split()))
q = deque(a)
for _ in range(k):
    q.popleft()
    q.append(0)

print(*q)
