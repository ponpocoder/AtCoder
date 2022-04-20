import sys
sys.setrecursionlimit(10**9)

n, m = map(int, input().split())
dic = {i:[] for i in range(1, n + 1)}
for _ in range(m):
    x, y = map(int, input().split())
    dic[x].append(y)

dp = [-1] * (n + 1)

def dfs(i):
    if dp[i] != -1:
        return dp[i]
    nexts = dic[i]
    if nexts == []: 
        dp[i] = 0
    else:
        for j in nexts:
            dp[i] = max(dp[i], dfs(j) + 1)
    return dp[i]

for i in range(1, n + 1):
    dfs(i)

print(max(dp))
        
            
        