n, m = map(int, input().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append(v)
    graph[v].append(u)

res = 0

for i in range(n):
    for j in graph[i]:
        if j <= i:
            continue
        for k in graph[j]:
            if k <= j:
                continue
            if i in graph[k]:
                res += 1

print(res)
