h, w = map(int, input().split())

n = h * w
par = [i for i in range(n)]
rank = [1] * n


def get(r, c):
    return r * w + c


def find(n):
    p = n
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


def same(n1, n2):
    p1, p2 = find(n1), find(n2)
    return p1 == p2


s = set()
q = int(input())

for _ in range(q):
    query = list(map(int, input().split()))
    if len(query) == 3:
        t, r, c = query
        r -= 1
        c -= 1
        s.add((r, c))
        if r > 0 and (r-1, c) in s:
            union(get(r, c), get(r-1, c))
        if r < h - 1 and (r+1, c) in s:
            union(get(r, c), get(r+1, c))
        if c > 0 and (r, c-1) in s:
            union(get(r, c), get(r, c-1))
        if c < w - 1 and (r, c+1) in s:
            union(get(r, c), get(r, c+1))
    else:
        t, r1, c1, r2, c2 = query
        r1 -= 1
        c1 -= 1
        r2 -= 1
        c2 -= 1
        x = get(r1, c1)
        y = get(r2, c2)
        if (r1, c1) in s and (r2, c2) in s and same(x, y):
            print("Yes")
        else:
            print("No")
