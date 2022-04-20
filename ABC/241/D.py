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
        if k > len(copy):
            print(-1)
        else:
            for _ in range(k - 1):
                heapq.heappop(copy)
            value = heapq.heappop(copy)
            if value < x:
                print(-1)
            else:
                print(value)
    else:
        copy = minHeap.copy()
        x, k = query[1], query[2]
        if k > len(copy):
            print(-1)
        else:
            for _ in range(k - 1):
                heapq.heappop(copy)
            value = heapq.heappop(copy)
            if value > x:
                print(-1)
            else:
                print(value)
