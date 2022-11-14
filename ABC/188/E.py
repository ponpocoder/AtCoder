n, m = map(int, input().split())
a = list(map(int, input().split()))
graph = [[] for _ in range(n)]
INF = 1001001001001

for _ in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    graph[x].append(y)

dp = [INF] * n

res = -INF
for i in range(n):
    res = max(res, a[i] - dp[i])
    for j in graph[i]:
        dp[j] = min(dp[j], dp[i])
        dp[j] = min(dp[j], a[i])

print(res)
