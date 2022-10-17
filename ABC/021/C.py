from collections import deque

n = int(input())
a, b = map(int, input().split())
a -= 1
b -= 1
mod = 10**9 + 7

graph = [[] for _ in range(n)]
m = int(input())

for _ in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    graph[x].append(y)
    graph[y].append(x)

visiting = set()
visited = set()
cnt = [0] * n
q = deque()
q.append((a, 1))
while q:
    for _ in range(len(q)):
        curr, cd = q.popleft()
        if curr in visited:
            continue
        visiting.add(curr)
        cnt[curr] += cd
        cnt[curr] %= mod

    for curr in visiting:
        visited.add(curr)
        for dest in graph[curr]:
            q.append((dest, cnt[curr]))
    visiting = set()

print(cnt[b])
