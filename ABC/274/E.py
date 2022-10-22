n, m = map(int, input().split())
n2 = n+m
n3 = 1 << (n+m)
cords = []
for _ in range(n2):
    x, y = map(int, input().split())
    cords.append((x, y))

dist = [[0] * n2 for _ in range(n2)]
for i in range(n2):
    x, y = cords[i]
    for j in range(n2):
        nx, ny = cords[j]
        dist[i][j] = (nx-x)**2+(ny-y)**2

dp = [[float("inf")] * n2 for _ in range(n3)]
for i in range(n2):
    x, y = cords[i]
    dp[1<<i][i] = x**2+y**2

for p in dp:
    print(*p)
curr = 1
for i in range(n3):
    for j in range(n2):
        if (i>>j&1) == 0:
            continue
        for k in range(n2):
            if i>>k&1:
                continue
            if k >= m:
                dp[i|1<<k][k] = min(dp[i|1<<k][k], dp[i][j] + dist[j][k]/curr**2)
            else:
                curr *= 2
print("-------------")
for row in dp:
    print(*row)
print(dp[n3-1][0])


