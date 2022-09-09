import sys
sys.setrecursionlimit(10**6)

n = int(input())
graph = [[] for _ in range(n)]
edge = []
for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    a -= 1
    b -= 1
    edge.append((a, b))
    graph[a].append(b)
    graph[b].append(a)

depth = [-1] * n


def getDepth(curr, cd, prev):
    depth[curr] = cd
    for dest in graph[curr]:
        if dest == prev:
            continue
        getDepth(dest, cd+1, curr)


getDepth(0, 0, -1)

dp = [0] * n

q = int(input())
for _ in range(q):
    t, e, x = map(int, sys.stdin.readline().split())
    if t == 1:
        a, b = edge[e-1]
    else:
        b, a = edge[e-1]

    if depth[a] > depth[b]:
        dp[a] += x
    else:
        dp[0] += x
        dp[b] -= x

# print(dp)


def dfs(curr, prev):
    if prev != -1:
        dp[curr] += dp[prev]
    for dest in graph[curr]:
        if dest == prev:
            continue
        dfs(dest, curr)


dfs(0, -1)
for v in dp:
    print(v)
