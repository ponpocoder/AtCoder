n, m = map(int, input().split())
ab = []

for _ in range(m):
    a, b = map(int, input().split())
    ab.append((a, b))

def bridge(u):
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
            par[p2] = p1
            return 1

    par = [i for i in range(n+1)]
    v = n
    for i in range(m):
        if i == u:
            continue
        v -= union(ab[i][0], ab[i][1])

    if v == 1:
        return False
    else:
        return True

    
res = 0
for i in range(m):
    if bridge(i):
        res += 1

print(res)