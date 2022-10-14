n = int(input())
INF = 1000
dp = [INF] * 301
dp[0] = 0

x = []
for _ in range(3):
    x.append(int(input()))


def dfs(curr):
    if curr in x:
        return 101
    if curr < 0:
        return False
    if dp[curr] != INF:
        return dp[curr]

    cnt = INF
    for j in range(1, 4):
        cnt = min(cnt, dfs(curr-j) + 1)

    dp[curr] = cnt
    return cnt


if dfs(n) <= 100:
    print("YES")
else:
    print("NO")
