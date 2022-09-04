import sys
sys.setrecursionlimit(10**9)

n, m = map(int, input().split())
a = list(map(int, input().split()))

INF = 1001001001001
dp = [[-INF] * (m+1) for _ in range(n+1)]
dp[0][0] = 0


def dfs(i, j):
    if dp[i][j] != -INF:
        return dp[i][j]
    if j == 0:
        return 0
    if j > i:
        return -INF
    dp[i][j] = max(dfs(i-1, j), dfs(i-1, j-1) + j * a[i-1])
    # print(i, j, dp[i][j])
    return dp[i][j]


print(dfs(n, m))
# for r in dp:
#     print(*r)
