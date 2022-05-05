n, m, k, s, t, x = map(int, input().split())
s -= 1
t -= 1
x -= 1

edges = []
mod = 998244353

for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1  
    edges.append((u, v))
    edges.append((v, u))

dp = [[[0 for _ in range(2)] for _ in range(k + 1)] for _ in range(n)]
dp[s][0][0] = 1

for i in range(k):
    for u, v in edges:
        if v == x:
            dp[v][i+1][0] += dp[u][i][1]
            dp[v][i+1][1] += dp[u][i][0]
        else:
            dp[v][i+1][0] += dp[u][i][0]
            dp[v][i+1][1] += dp[u][i][1]
        dp[v][i+1][0] %= mod
        dp[v][i+1][1] %= mod

print(dp[t][k][0])

# dfsは計算量がNMKになるのでTLE、メモ化使えばTLEしない
# cnt = 0

# def dfs(i, j, r):  # i:currentIndex j:NumberOfVisitedNodes k:xtimes
#     if j == k:
#         if i == t and r % 2 == 0:
#             global cnt
#             cnt += 1
#         return
    
#     for next in graph[i]:
#         if i == x:
#             dfs(next, j + 1, r + 1)
#         else:
#             dfs(next, j + 1, r)

# dfs(s, 0, 0)
# print(cnt % mod)



