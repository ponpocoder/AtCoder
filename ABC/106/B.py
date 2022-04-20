n = int(input())
dp = [0] * (n + 1)

for i in range(1, n + 1, 2):
    for j in range(1, i + 1):
        if i % j == 0:
            dp[i] += 1

res = 0
for v in dp:
    if v == 8:
        res += 1

print(res)