n = int(input())
s = input()

mod = 10**9 + 7
t = "atcoder"
dp = [0] * 7

for i in range(1, n+1):
    p = dp
    c = s[i-1]
    if c in t:
        x = t.index(c)
        if x == 0:
            dp[x] = p[x] + 1
        else:
            dp[x] += p[x-1]
        dp[x] %= mod

print(dp[-1])
