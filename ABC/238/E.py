n, q = map(int, input().split())

rank = [1] * (n+1)
par = [i for i in range(n+1)]

def find(n):
    p = n
    while p != par[p]:
        par[p] = par[par[p]]
        p = par[p]
    return p

def union(n1, n2):
    p1, p2 = find(n1), find(n2)
    if p1 == p2:
        return
    if rank[p1] > rank[p2]:
        rank[p1] += rank[p2]
        par[p2] = p1
    else:
        rank[p2] += rank[p1]
        par[p1] = p2
    return

for _ in range(q):
    l, r = map(int, input().split())
    l -= 1
    union(l, r)

x, y = find(0), find(n)
if x == y:
    print("Yes")
else:
    print("No")