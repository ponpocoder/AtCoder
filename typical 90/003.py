from collections import deque

n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

visited = set()


def bfs(i):
    dist = [-1] * n
    q = deque()
    q.append(i)
    cnt = 0
    while q:
        for _ in range(len(q)):
            curr = q.popleft()
            dist[curr] = cnt
            for dest in graph[curr]:
                if dist[dest] != -1:
                    continue
                q.append(dest)
        cnt += 1

    return dist


cd = bfs(0)
md = max(cd)
x = cd.index(md)
nd = bfs(x)
print(max(nd)+1)
