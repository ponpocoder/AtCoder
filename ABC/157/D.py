from collections import defaultdict
n, m, k = map(int, input().split())

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
    if p1 == p2:
        return 0
    if rank[p1] > rank[p2]:
        rank[p1] += rank[p2]
        par[p2] = p1
    else:
        rank[p2] += rank[p1]
        par[p1] = p2
    return 1


graph = defaultdict(set)

for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].add(b)
    graph[b].add(a)
    union(a, b)

for _ in range(k):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if find(c) == find(d):  # 同じグループ内のブロック関係でなければ無視できる
        graph[c].add(d)
        graph[d].add(c)

res = []
for i in range(n):
    p = find(i)
    res.append(rank[p] - len(graph[i]) - 1)

print(*res)
