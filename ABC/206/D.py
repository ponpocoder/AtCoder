from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))

par = [i for i in range(2*10**5+1)]
rank = [1] * (2*10**5+1)

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

l, r = 0, n - 1
res = 0

while l < r:
    res += union(a[l], a[r])
    l += 1
    r -= 1

print(res)