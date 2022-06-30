import sys
sys.setrecursionlimit(10**6)

n = int(input())
x = list(map(int, input().split()))
c = list(map(int, input().split()))

graph = [[] for _ in range(n)]
for i in range(n):
    graph[x[i]-1].append((i, c[i-1]))

cycle = set()
visited = set()

def dfs(i):
    if i in cycle:
        return False
    if i in visited:
        return True
    
    cycle.add(i)
    visited.add(i)
    for d, c in graph[i]:
        if not dfs(d):
            return False
    cycle.remove(i)
    return True

res = 0
for i in range(n):
    if not dfs(i):
        # print(cycle)
        mn = float("inf")
        for i in cycle:
            mn = min(mn, c[i])
            visited.add(i)
        res += mn
        cycle = set()

print(res)