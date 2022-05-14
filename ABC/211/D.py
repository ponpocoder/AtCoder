from collections import deque

n, m = map(int, input().split())
mod = 10**9 + 7
path = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    path[a].append(b)
    path[b].append(a)

dist = [float("inf")] * n
dist[0] = 0
cnt = [0] * n
cnt[0] = 1
q = deque()
q.append(0)

while q:
    for _ in range(len(q)):
        curr = q.popleft()
        for dest in path[curr]:
            if dist[dest] == float("inf"):
                q.append(dest)
                dist[dest] = dist[curr] + 1
                cnt[dest] = cnt[curr]
            elif dist[dest] == dist[curr] + 1:
                cnt[dest] += cnt[curr]
                cnt[dest] %= mod
                
print(cnt[n-1])

