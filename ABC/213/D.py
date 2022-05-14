import sys
sys.setrecursionlimit(10**9)

n = int(input())
path = [[] for _ in range(n+1)]

for _ in range(n-1):
    x, y = map(int, input().split())
    path[x].append(y)
    path[y].append(x)

for i in range(n+1):
    path[i].sort()

visited = [False] * (n+1)
res = []

def dfs(curr, prev):
    res.append(curr)
    for dest in path[curr]:
        if dest != prev:
            dfs(dest, curr)
            res.append(curr)

dfs(1, -1)
print(*res)
    
