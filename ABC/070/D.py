import sys
sys.setrecursionlimit(10**6)

n = int(input())
graph = [[] for _ in range(n)]

for _ in range(n-1):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append((b, c))
    graph[b].append((a, c))

q, k = map(int, input().split())
k -= 1

dist = [-1] * n


def dfs(curr, prev, d):
    dist[curr] = d
    for dest, cost in graph[curr]:
        if dest == prev or dist[dest] != -1:
            continue
        dfs(dest, curr, d+cost)


dfs(k, -1, 0)

for _ in range(q):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    print(dist[x] + dist[y])
