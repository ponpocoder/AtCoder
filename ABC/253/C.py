from heapq import heapify, heappush, heappop
from collections import defaultdict
q = int(input())

minHeap = []
maxHeap = []
dic = defaultdict(int)

for _ in range(q):
    query = input().split()
    if len(query) == 1:
        while dic[minHeap[0]] == 0:
            heappop(minHeap)
        while dic[-maxHeap[0]] == 0:
            heappop(maxHeap)
        
        mx = -maxHeap[0]
        mn = minHeap[0]
        print(mx - mn)
    elif len(query) == 2:
        q, x = map(int, query)
        dic[x] += 1
        heappush(minHeap, x)
        heappush(maxHeap, -x)
        
    else:
        q, x, c = map(int, query)
        if c >= dic[x]:
            dic[x] = 0
        else:
            dic[x] -= c
        