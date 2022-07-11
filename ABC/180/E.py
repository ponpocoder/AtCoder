n = int(input())
n2 = 1 << n
cords = []
for _ in range(n):
    x, y, z = map(int, input().split())
    cords.append((x, y, z))

dist = [[0] * n for _ in range(n)]
for i in range(n):
    x, y, z = cords[i]
    for j in range(n):
        nx, ny, nz = cords[j]
        dist[i][j] = abs(x-nx)+abs(y-ny)+max(0, nz-z)

dp = [[float("inf")] * n for _ in range(n2)]

for i in range(n):
    if i == 0:
        continue
    dp[1<<i][i] = dist[0][i]

for i in range(n2):
    for j in range(n):
        if (i>>j&1) == 0:
            continue
        for k in range(n):
            if i>>k&1:
                continue
            dp[i|1<<k][k] = min(dp[i|1<<k][k], dp[i][j] + dist[j][k])

print(dp[n2-1][0])

