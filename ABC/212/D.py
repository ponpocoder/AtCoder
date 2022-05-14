from heapq import heappush, heappop

q = int(input())
curr = 0
heap = []
for _ in range(q):
    query = list(map(int, input().split()))
    one = query[0]

    if one == 1:
        heappush(heap, query[1] - curr)
    elif one == 2:
        curr += query[1]
    else:
        print(heappop(heap)+curr)




