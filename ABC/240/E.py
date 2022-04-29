import sys
sys.setrecursionlimit(10 ** 6)
n = int(input())

L = [0] * n
R = [0] * n

graph = [[] for _ in range(n)]

for _ in range(n - 1):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    graph[x].append(y)
    graph[y].append(x)

cnt = 0
def dfs(curr, prev):
    isLeaf = True
    global cnt
    l, r = cnt + 1, cnt + 1
    for node in graph[curr]:
        if node == prev:
            continue
        isLeaf = False
        dfs(node, curr)
        l = min(l, L[node])
        r = max(r, R[node])
    if isLeaf:
        cnt += 1
    L[curr] = l
    R[curr] = r

dfs(0, 0)
for l, r in zip(L, R):
    print(l, r)