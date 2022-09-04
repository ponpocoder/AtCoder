from heapq import heapify, heappush, heappop
n, m = map(int, input().split())
a = list(map(int, input().split()))
graph = [[] for _ in range(n)]
cost = [0] * n
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append(v)
    graph[v].append(u)
    cost[u] += a[v]
    cost[v] += a[u]

heap = []

for i in range(n):
    heap.append((cost[i], i))

heapify(heap)

visited = [False] * n
res = 0
while heap:
    cc, ci = heappop(heap)
    if visited[ci]:
        continue
    visited[ci] = True
    res = max(res, cc)
    for dest in graph[ci]:
        if visited[dest]:
            continue
        cost[dest] -= a[ci]
        heappush(heap, (cost[dest], dest))

print(res)

# from collections import deque
# n, m = map(int, input().split())
# a = list(map(int, input().split()))
# graph = [[] for _ in range(n)]

# for _ in range(m):
#     u, v = map(int, input().split())
#     u -= 1
#     v -= 1
#     graph[u].append(v)
#     graph[v].append(u)


# def check(x):
#     cost = [0] * n
#     visited = [False] * n
#     q = deque()
#     for i in range(n):
#         for j in graph[i]:
#             cost[i] += a[j]
#         if cost[i] <= x:
#             q.append(i)
#             visited[i] = True
#     cnt = 0
#     while q:
#         curr = q.popleft()
#         cnt += 1
#         for dest in graph[curr]:
#             cost[dest] -= a[curr]
#             if not visited[dest] and cost[dest] <= x:
#                 visited[dest] = True
#                 q.append(dest)
#     return cnt == n


# l, r = 0, 10**16
# while l <= r:
#     m = (l + r) // 2
#     if check(m):
#         r = m - 1
#     else:
#         l = m + 1

# print(l)
