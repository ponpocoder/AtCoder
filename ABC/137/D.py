from heapq import heappush, heappop

n, m = map(int, input().split())
graph = [[] for _ in range(m)]

for _ in range(n):
    a, b = map(int, input().split())
    if a > m:
        continue
    graph[m-a].append(b)

heap = []
res = 0
for i in range(m-1, -1, -1):
    for job in graph[i]:
        heappush(heap, -job)
    if heap:
        res += -heappop(heap)

print(res)
