from collections import deque
import heapq

n = int(input())
q = deque()
heap = []
sortedLen = 0
for _ in range(n):
    query = list(map(int, input().split()))
    if query[0] == 1:
        x = query[1]
        q.append(x)
    elif query[0] == 2:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(q.popleft())
    else:
        for v in q:
            heapq.heappush(heap, v)
        q.clear()