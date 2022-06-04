n, m = map(int, input().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

def getCount(x, k, curr):
    curr.add(x+1)
    if k == 0:
        return curr.copy()
    for node in graph[x]:
        curr | getCount(node, k - 1, curr)
    return curr

q = int(input())
for _ in range(q):
    x, k = map(int, input().split())
    x -= 1
    t = getCount(x, k, set())
    curr = 0
    for v in t:
        curr += v
    print(curr)

