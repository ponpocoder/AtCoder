import sys
sys.setrecursionlimit(10**7)

h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]
mod = 10**9+7

dp = [[0] * w for _ in range(h)]


def dfs(r, c, prev):
    if r < 0 or r >= h or c < 0 or c >= w or a[r][c] <= prev:
        return 0

    if dp[r][c]:
        return dp[r][c]

    curr = a[r][c]
    dp[r][c] = 1 + dfs(r+1, c, curr) + dfs(r-1, c, curr) + dfs(r, c+1, curr) + dfs(r, c-1, curr)
    dp[r][c] %= mod
    return dp[r][c]


res = 0
for i in range(h):
    for j in range(w):
        res += dfs(i, j, 0)
        res %= mod

# for r in dp:
    # print(*r)

print(res)
