s = input()
K = int(input())

n = len(s)

# i桁目まで決めてj個の0でない数字を使ってそこまでの値がNと一致しているか
dp = [[[0] * 2 for _ in range(K+1)] for _ in range(n+1)]
dp[0][0][0] = 1

for i in range(n):
    for j in range(K+1):
        for k in range(2):
            nd = int(s[i])
            for d in range(10):
                ni = i + 1
                nj = j
                nk = k
                if d != 0:
                    nj += 1
                if nj > K:
                    continue
                if k == 0:
                    if d > nd:
                        continue
                    if d < nd:
                        nk = 1
                dp[ni][nj][nk] += dp[i][j][k]

res = dp[n][K][0] + dp[n][K][1]
print(res)
