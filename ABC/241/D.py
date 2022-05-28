#現時点では解けない wm, binary trieなどが必要   

import heapq
q = int(input())
queries = []
for _ in range(q):
    query = list(map(int, input().split()))
    queries.append(query)

minHeap = []
maxHeap = []

for query in queries:
    if query[0] == 1:
        heapq.heappush(minHeap, query[1])
        heapq.heappush(maxHeap, query[1])
    elif query[0] == 2:
        copy = maxHeap.copy()
        x, k = query[1], query[2]
        while copy and copy[-1] > x:
            heapq.heappop(minHeap)
        if len(copy) < k:
            print(-1)
        else:
            for _ in range(k - 1):
                heapq.heappop(minHeap)
            value = heapq.heappop(minHeap)
            print(value)
    else:
        copy = minHeap.copy()
        x, k = query[1], query[2]
        x, k = query[1], query[2]
        while copy and copy[-1] < x:
            heapq.heappop(minHeap)
        if len(copy) < k:
            print(-1)
        else:
            for _ in range(k - 1):
                heapq.heappop(minHeap)
            value = heapq.heappop(minHeap)
            print(value)