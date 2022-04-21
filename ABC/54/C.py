n, m = map(int, input().split())
nodeMap = {i:[] for i in range(n)}

for _ in range(m):
    a, b = map(int, input().split())
    nodeMap[a - 1].append(b - 1)
    nodeMap[b - 1].append(a - 1)

visited = set()
visited.add(0)
res = 0


def dfs(i):
    global res
    if len(visited) == n:
        res += 1
        return
    
    for node in nodeMap[i]:
        if node not in visited:
            visited.add(node)
            dfs(node)
            visited.remove(node)

dfs(0)
print(res)
