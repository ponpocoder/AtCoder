import sys

n = int(input())
ways = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    ways[a].append(b)

visited = set()

def dfs(i, count):
    visited.add(i)
    count = 0
    newCount = 0
    for node in ways[i]:
        if node not in visited:
            newCount = max(newCount, dfs(node, newCount))
    visited.remove(i)
    count = max(count, newCount)
    return count
    
count = dfs(1, 0)
print(count + 1)