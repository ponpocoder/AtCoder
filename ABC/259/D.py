n = int(input())
sx, sy, tx, ty = map(int, input().split())
cords = []
ps, pt = -1, -1

def dist(x, y, a, b):
    return (x-a)**2 + (y-b)**2

for i in range(n):
    x, y, r = map(int, input().split())
    cords.append((x, y, r))
    ds = dist(x, y, sx, sy)
    if ds == r*r:
        ps = i
    dt = dist(x, y, tx, ty)
    if dt == r*r:
        pt = i

# print(cords)
# print(ps, pt)

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
        return
    if rank[p1] > rank[p2]:
        rank[p1] += rank[p2]
        par[p2] = p1
    else:
        rank[p2] += rank[p1]
        par[p1] = p2

for i in range(n-1):
    xi, yi, ri = cords[i]
    for j in range(i+1, n):
        xj, yj, rj = cords[j]
        d = dist(xi, yi, xj, yj)
        mx = max(ri, rj)
        mn = min(ri, rj)
        if (mx - mn)**2 <= d <= (mx + mn)**2:
            union(i, j)

parS, parT = find(ps), find(pt)

# print(par)

if parS == parT:
    print("Yes")
else:
    print("No")