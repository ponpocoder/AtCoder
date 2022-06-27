import sys
sys.setrecursionlimit(10**6)

n = int(input())
graph = [[] for i in range(n)]

for _ in range(n-1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append((v, w))
    graph[v].append((u, w))

res = [0] * n
visited = [False] * n

def dfs(i, j):
    res[i] = j
    visited[i] = True
    for dest, dist in graph[i]:
        if visited[dest]:
            continue
        if dist % 2 == 0:
            dfs(dest, j)
        else:
            dfs(dest, j^1)

dfs(0, 0)
for r in res:
    print(r)