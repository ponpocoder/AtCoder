n, m = map(int, input().split())
q = [list(map(int, input().split())) for _ in range(m)]
q.sort(key=lambda x:x[2])

res = 0
rank = [1] * (n+1)
par = [i for i in range(n+1)]

def find(n):
    while n != par[n]:
        par[n] = par[par[n]]
        n = par[n]
    return n

def union(n1, n2, c):
    p1, p2 = find(n1), find(n2)
    if p1 == p2:
        if c > 0:
            return c    
        else:
            return 0
    if rank[p1] > rank[p2]:
        rank[p1] += rank[p2]
        par[p2] = p1
    else:
        rank[p2] += rank[p1]
        par[p1] = p2
    return 0

res = 0
for a, b, c in q:
    res += union(a, b, c)

print(res)