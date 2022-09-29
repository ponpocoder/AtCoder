import sys
sys.setrecursionlimit(10**6)
n, x, y = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

res = []


def dfs(curr, prev, res):
    res.append(curr)
    if curr == y:
        print(*res)
        exit()
    for dest in graph[curr]:
        if dest == prev:
            continue
        dfs(dest, curr, res)
    res.pop()


dfs(x, -1, [])
