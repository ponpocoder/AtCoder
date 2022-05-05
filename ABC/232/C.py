from itertools import permutations

n, m = map(int, input().split())
a = [[False] * n for _ in range(n)]
b = [[False] * n for _ in range(n)]

for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    a[u][v] = a[v][u] = True

for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    b[u][v] = b[v][u] = True

res = False
for perm in permutations(range(n)):
    canForm = True
    for i in range(n):
        for j in range(n):
            if a[i][j] != b[perm[i]][perm[j]]:
                canForm = False
    if canForm:
        res = True

if res:
    print("Yes")
else:
    print("No")