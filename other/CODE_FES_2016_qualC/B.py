from heapq import heapify, heappop, heappush

k, t = map(int, input().split())
a = list(map(int, input().split()))

for i in range(t):
    a[i] = -a[i]

heapify(a)

while len(a) > 1:
    first, second = heappop(a), heappop(a)
    remain = first - second
    if remain:
        heappush(a, remain)
        
if len(a) == 0:
    print(0)
else:
    print(abs(a[0]) - 1)