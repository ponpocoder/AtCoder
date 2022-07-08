a, b, c = map(int, input().split())
x = 101
dp = [[[0] * x for _ in range(x)] for _ in range(x)]

for i in range(x-2, -1, -1):
    for j in range(x-2, -1, -1):
        for k in range(x-2, -1, -1):
            if i+j+k == 0:
                continue
            curr = 0
            curr += dp[i+1][j][k] * i
            curr += dp[i][j+1][k] * j
            curr += dp[i][j][k+1] * k
            dp[i][j][k] = curr / (i+j+k) + 1
            
print(dp[a][b][c])