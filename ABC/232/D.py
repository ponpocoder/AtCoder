h, w = map(int, input().split())
matrix = [input() for _ in range(h)]
dp = [[0 for _ in range(w)] for _ in range(h)]

def dfs(r, c):
    if r >= h or c >= w or matrix[r][c] == "#":
        return 0
    
    if dp[r][c]:
        return dp[r][c]

    dp[r][c] = max(dfs(r+1, c), dfs(r, c+1)) + 1
    return dp[r][c]

dfs(0, 0)
print(dp[0][0])