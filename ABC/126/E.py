n, m = map(int, input().split())

par = [i for i in range(n)]
rank = [1] * n


def find(n):
    p = n
    while p != par[p]:
        par[p] = par[par[p]]
        p = par[p]

    return p


def union(n1, n2):
    p1, p2 = find(n1), find(n2)
    if p1 == p2:
        return 0
    else:
        if rank[p1] > rank[p2]:
            rank[p1] += rank[p2]
            par[p2] = p1
        else:
            rank[p2] += rank[p1]
            par[p1] = p2
    return 1


res = n
for _ in range(m):
    x, y, z = map(int, input().split())
    x -= 1
    y -= 1
    res -= union(x, y)

print(res)
