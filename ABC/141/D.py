from heapq import heapify, heappop, heappush

n, m = map(int, input().split())
a = list(map(lambda x: -int(x), input().split()))

heapify(a)
for _ in range(m):
    curr = heappop(a)
    curr = (curr + 1) // 2
    heappush(a, curr)

print(-sum(a))