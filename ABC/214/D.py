n = int(input())

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
        cnt = rank[p1] * rank[p2]
        if rank[p1] > rank[p2]:
            rank[p1] += rank[p2]
            par[p2] = p1
        else:
            rank[p2] += rank[p1]
            par[p1] = p2
        return cnt

edges = []
for _ in range(n-1):
    u, v, w = map(int, input().split())
    edges.append((u-1, v-1, w))
    
edges.sort(key=lambda x:x[2])

res = 0
for u, v, w in edges:
    res += w * union(u, v)

print(res)