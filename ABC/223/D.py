import heapq
import sys

n, m = map(int, input().split())

graph = {i:[] for i in range(n)}
cnt = [0 for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    cnt[b] += 1

q = []
for i, v in enumerate(cnt):
    if v == 0:
        heapq.heappush(q, i)
res = []

while q:
    curr = heapq.heappop(q)
    res.append(curr + 1)
    for node in graph[curr]:
        cnt[node] -= 1
        if cnt[node] == 0:
            heapq.heappush(q, node)

if len(res) == n:
    print(*res)
else:
    print(-1)
