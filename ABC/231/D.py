import sys

n, m = map(int, input().split())
parents = [i for i in range(n)]
ranks = [1] * n

def find(n):
    while n != parents[n]:
        parents[n] = parents[parents[n]]
        n = parents[n]
    return n

def union(p1, p2):
    if ranks[p1] > ranks[p2]:
        ranks[p2] += ranks[p1]
        parents[p2] = p1
    else:
        ranks[p1] += ranks[p2]
        parents[p1] = p2

cnt = [2] * n

for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    cnt[a] -= 1
    cnt[b] -= 1
    pa, pb = find(a), find(b)
    if pa == pb:
        print("No")
        sys.exit()
    union(pa, pb)

one = 0
for v in cnt:
    if v < 0:
        print("No")
        sys.exit()
    if v >= 1:
        one += 1

print("Yes")