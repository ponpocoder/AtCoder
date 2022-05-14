import sys
sys.setrecursionlimit(10**5)

n, q = map(int, input().split())
graph = [[] for _ in range(n)]

for _ in range(n-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

dist = [0] * n

def dfs(curr, prev, cnt):   
    dist[curr] = cnt % 2
    for dest in graph[curr]:
        if dest != prev:
            dfs(dest, curr, cnt+1)

dfs(0, -1, 0)

for _ in range(q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if dist[c] ^ dist[d] == 1:
        print("Road")
    else:
        print("Town")
