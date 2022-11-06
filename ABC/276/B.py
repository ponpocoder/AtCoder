n, m = map(int, input().split())
graph = [[] for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

for i in range(n):
    graph[i].sort()

for i in range(n):
    res = []
    res.append(len(graph[i]))
    for x in graph[i]:
        res.append(x+1)
    print(*res)
