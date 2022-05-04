import heapq

n, k =  map(int, input().split())
p = list(map(int, input().split()))

array = p[:k]
print(min(array))
heapq.heapify(array)

for i in range(k, n):
    curr = heapq.heappop(array)
    nxt = max(curr, p[i])
    heapq.heappush(array, nxt)
    res = heapq.heappop(array)
    print(res)
    heapq.heappush(array, res)