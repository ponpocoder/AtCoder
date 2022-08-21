n, a = map(int, input().split())
x = list(map(int, input().split()))

dp = [[[[0] * 50] for _ in range(51)] for _ in range(51)]
dp[0][0][0] = 1

for i in range(n):
    for j in range(n):
        for v in x:
            nj = ((i-1)*j+v)//i
            dp[i][nj] += dp[i-1][j]

for v in dp:
    print(v[:11])
cnt = 0
for i in range(1, n+1):
    cnt += dp[i][a]

print(cnt)
