n, m = map(int, input().split())
p = list(map(int, input().split()))

par = [i for i in range(n+1)]
rank = [1] * (n+1)


def find(n):
    p = par[n]
    while p != par[p]:
        par[p] = par[par[p]]
        p = par[p]
    return p


def union(n1, n2):
    p1, p2 = find(n1), find(n2)
    if p1 == p2:
        return 1
    if rank[p1] > rank[p2]:
        rank[p1] += rank[p2]
        par[p2] = p1
    else:
        rank[p2] += rank[p1]
        par[p1] = p2
    return 0


def same(n1, n2):
    p1, p2 = find(n1), find(n2)
    if p1 == p2:
        return 1
    else:
        return 0


for _ in range(m):
    x, y = map(int, input().split())
    union(x, y)

cnt = 0
for i in range(n):
    cnt += same(i+1, p[i])

print(cnt)
