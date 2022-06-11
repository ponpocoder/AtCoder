import sys
sys.setrecursionlimit(10**6)
n, q = map(int, input().split())
cnt = [0] * n
graph = [[] for _ in range(n)]

for _ in range(n-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

for _ in range(q):
    p, x = map(int, input().split())
    cnt[p-1] += x

def dfs(curr, prev = -1):
    for dest in graph[curr]:
        if dest != prev:
            cnt[dest] += cnt[curr]
            dfs(dest, curr)

dfs(0)
print(*cnt)