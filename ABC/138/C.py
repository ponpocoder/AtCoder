from heapq import heappop, heappush

n = int(input())
v = list(map(int, input().split()))

heap = []
for x in v:
    heappush(heap, x)

while len(heap) > 1:
    x, y = heappop(heap), heappop(heap)
    z = (x + y) / 2
    heappush(heap, z)

print(heap[0])
