n = int(input())
a = list(map(int, input().split()))

s = [0] * (n+1)

for i in range(1, n+1):
    s[i] = a[i-1] + s[i-1]

dp = [[0] * (n+1) for _ in range(n+1)]

def calcCost(l, r):
    if dp[l][r] != 0:
        return dp[l][r]
    
    if l == r:
        return 0
    
    curr = float("inf")
    for m in range(l, r):
        curr = min(curr, calcCost(l, m) + calcCost(m+1, r))
    dp[l][r] = curr + s[r] - s[l]

    return dp[l][r]

print(calcCost(1, n))
