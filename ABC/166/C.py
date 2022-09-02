n, m = map(int, input().split())
h = list(map(int, input().split()))

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

res = 0
for i in range(1, n+1):
    ch = h[i-1]
    nh = 0
    for j in graph[i]:
        nh = max(nh, h[j-1])
    if ch > nh:
        res += 1

print(res)
