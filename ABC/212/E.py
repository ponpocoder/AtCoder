n, m, k = map(int, input().split())
mod = 998244353

graph = [[] for _ in range(n)]

for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append(v)
    graph[v].append(u)

dp = [0] * n
dp[0] = 1

for _ in range(k):
    p = dp
    dp = [0] * n
    s = sum(p)
    s %= mod
    for i in range(n):
        dp[i] = s
        for dest in graph[i]:
            dp[i] -= p[dest]
        dp[i] -= p[i]
        dp[i] %= mod

print(dp[0])
