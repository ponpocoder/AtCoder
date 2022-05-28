import sys
sys.setrecursionlimit(10**6)
import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')

n = int(input())
a = list(map(int, input().split()))

dp = [[-1] * n for _ in range(n)]

def getScore(l, r):
    if dp[l][r] != -1:
        return dp[l][r]

    if l == r:
        dp[l][r] = a[l]
        return a[l]
    
    dp[l][r] = max(a[l] - getScore(l+1, r), a[r] - getScore(l, r - 1))
    return dp[l][r]

print(getScore(0, n-1))