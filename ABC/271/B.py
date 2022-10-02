n, q = map(int, input().split())

s = []
for _ in range(n):
    x = list(map(int, input().split()))
    s.append(x[1:])

for _ in range(q):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    print(s[u][v])
