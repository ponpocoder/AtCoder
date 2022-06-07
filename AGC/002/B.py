n, m = map(int, input().split())
visited = [False] * (n + 1)
cnt = [1] * (n + 1)
visited[1] = True

for _ in range(m):
    x, y = map(int, input().split())
    if visited[x]:
        visited[y] = True
    if cnt[x] == 1:
        visited[x] = False
    cnt[x] -= 1
    cnt[y] += 1

res = 0

for i in range(n+1):
    if visited[i] and cnt[i]:
        res += 1

print(res)