import sys
sys.setrecursionlimit(10**9)
n, q = map(int, input().split())
x = list(map(int, input().split()))

graph = [[] for _ in range(n)]

for _ in range(n-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

res = [[x[i]] for i in range(n)]


def dfs(curr, prev):
    for node in graph[curr]:
        if node != prev:
            dfs(node, curr)
            res[curr].extend(res[node])
    res[curr].sort(reverse=True)
    res[curr] = res[curr][:20]

dfs(0, - 1)

for _ in range(q):
    v, k = map(int, input().split())
    v -= 1
    k -= 1
    print(res[v][k])
