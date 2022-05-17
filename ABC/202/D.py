a, b, k = map(int, input().split())
p = a + b
dp = [[0] * (p + 1) for _ in range(p + 1)]
dp[0][0] = 1

for i in range(p):
    for j in range(i+1):
        dp[i+1][j] += dp[i][j]
        dp[i+1][j+1] += dp[i][j]

res = ""

while p > 0:
    curr = 0
    if a > 0:
        curr = dp[p - 1][a - 1]
    
    if curr >= k:
        res += "a"
        p -= 1
        a -= 1
    else:
        res += "b"
        k -= curr
        p -= 1

print(res)