n, m = map(int, input().split())
res = 0

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
        return 
    if rank[p1] > rank[p2]:
        rank[p1] += rank[p2]
        par[p2] = p1
    else:
        rank[p2] += rank[p1]
        par[p1] = p2
    return 

for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    union(a, b)

print(max(rank))