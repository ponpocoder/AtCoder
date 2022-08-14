n, m, e = map(int, input().split())
cons = []
for _ in range(e):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    cons.append((u, v))

q = int(input())
x = []
for _ in range(q):
    x.append(int(input())-1)

par = [i for i in range(n+1)]
rank = [1] * (n+1)
rank[n] = 0


def find(n):
    p = par[n]
    while p != par[p]:
        par[p] = par[par[p]]
        p = par[p]
    return p


def union(n1, n2):
    n1 = min(n1, n)
    n2 = min(n2, n)
    p1, p2 = find(n1), find(n2)
    if p1 == p2:
        return 0
    if p1 == n or p2 == n:
        if p1 == n:
            cnt = rank[p2]
            rank[p1] += rank[p2]
            par[p2] = p1
        else:
            cnt = rank[p1]
            rank[p2] += rank[p1]
            par[p1] = p2
    else:
        if rank[p1] > rank[p2]:
            rank[p1] += rank[p2]
            par[p2] = p1
        else:
            rank[p2] += rank[p1]
            par[p1] = p2
        cnt = 0
    return cnt


s = set(x)
cnt = 0
for i in range(e):
    if i not in s:
        u, v = cons[i]
        cnt += union(u, v)

x.reverse()
res = []

for i in range(q):
    res.append(cnt)
    u, v = cons[x[i]]
    cnt += union(u, v)

res.reverse()

for a in res:
    print(a)
