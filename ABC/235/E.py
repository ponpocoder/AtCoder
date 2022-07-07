n, m, q = map(int, input().split())
edges = []
extra = []

for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    edges.append((c, a, b))

edges.sort()

for i in range(q):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    extra.append((w, u, v, i))

extra.sort()


par = [i for i in range(n)]
rank = [1] * n

def find(n):
    p = par[n]
    while p != par[p]:
        par[p] = par[par[p]]
        p = par[p]
    return p

def union(n1, n2):
    p1, p2 = find(n1), find(n2)
    if p1 != p2:
        if rank[p1] > rank[p2]:
            rank[p1] += rank[p2]
            par[p2] = p1
        else:
            rank[p2] += rank[p1]
            par[p1] = p2

def same(n1, n2):
    p1, p2 = find(n1), find(n2)
    return p1 == p2

p = 0
used = [False] * q

for i in range(m):
    c, a, b = edges[i]
    while p < q and extra[p][0] < c:
        w, u, v, j = extra[p]
        used[j] = not same(u, v)
        p += 1
    union(a, b)

for i in range(q):
    if used[i]:
        print("Yes")
    else:
        print("No")
    