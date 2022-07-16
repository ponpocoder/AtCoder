from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

flag = [-1] * (n+1)

q = deque()
q.append((-1, 1))

while q:
    for _ in range(len(q)):
        prev, curr = q.popleft()
        if flag[curr] != -1:
            continue
        flag[curr] = prev
        for nxt in graph[curr]:
            if nxt == prev or flag[nxt] != -1:
                continue
            q.append((curr, nxt))

print("Yes")
for v in flag[2:]:
    print(v)
