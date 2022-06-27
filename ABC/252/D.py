from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))

dic = defaultdict(int)
for v in a:
    dic[v] += 1

b = []
for v in dic.values():
    b.append(v)

m = len(b)
dp = [[0] * (m+1) for _ in range(4)]

for i in range(m+1):
    dp[0][i] = 1

for i in range(1, m+1):
    for j in range(1, 4):
        dp[j][i] = dp[j][i-1] + dp[j-1][i-1] * b[i-1]

# for p in dp:
#     print(*p)
print(dp[-1][-1])
