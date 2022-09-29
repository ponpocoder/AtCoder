n, m = map(int, input().split())
mod = 998244353
par = [i for i in range(n)]
rank = [1] * (n)


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


edges = []
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    edges.append((u, v))
    union(u, v)


cntV = [0] * n
cntE = [0] * n

for a, b in edges:
    cntE[find(a)] += 1
for i in range(n):
    cntV[find(i)] += 1

res = 1
for i in range(n):
    if cntV[i] == 0:
        continue
    if cntV[i] != cntE[i]:
        res = 0
    res *= 2
    res %= mod

print(res)
