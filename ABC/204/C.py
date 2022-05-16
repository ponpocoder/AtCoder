import sys
sys.setrecursionlimit(10**5)

n, m = map(int, input().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)

res = 0
def dfs(curr):
    if visited[curr]:
        return
    visited[curr] = True
    global res
    res += 1
    for dest in graph[curr]:
        dfs(dest)

for i in range(n):
    visited = [False] * n
    dfs(i)

print(res)