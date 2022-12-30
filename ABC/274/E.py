n, m = map(int, input().split())
n2 = n+m+1
n3 = 1 << n2

cords = []
for _ in range(n2-1):
    x, y = map(int, input().split())
    cords.append((x, y))

dp = [[INF] * n2 for _ in range(n3)]
dp[n+m][0] = 0

for i in range(n3):
    for j in range(n
