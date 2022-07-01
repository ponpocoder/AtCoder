import sys
sys.setrecursionlimit(10**6)

n = int(input())

coin = []
i = 1

while i <= 10**5:
    coin.append(i)
    i *= 6

i = 9
while i <= 10**5:
    coin.append(i)
    i *= 9

dp = [n] * (n + 1)
dp[0] = 0


def dfs(x):
    if dp[x] != n:
        return dp[x]
    
    curr = n
    for i in range(len(coin)):
        if x - coin[i] < 0:
            continue
        curr = min(curr, dfs(x - coin[i]) + 1)
    
    dp[x] = curr
    return curr

dfs(n)
print(dp[-1])