n, s = map(int, input().split())
x = []

for _ in range(n):
    a, b = map(int, input().split())
    x.append((a, b))

# i番目のカードを使ってその時の和がjとなる組み合わせが存在するか
dp = [[False] * 10001 for _ in range(n+1)]
dp[0][0] = True

for i in range(1, n+1):
    a, b = x[i-1]
    for j in range(10001):
        if a + j < 10001:
            dp[i][a+j] |= dp[i-1][j]

        if b + j < 10001:
            dp[i][b+j] |= dp[i-1][j]

res = []


def get(i, curr):
    if i == 0:
        return
    a, b = x[i-1]
    if curr >= a and dp[i-1][curr-a]:
        res.append("H")
        get(i-1, curr-a)
    else:
        res.append("T")
        get(i-1, curr-b)


# for i in range(n+1):
#     print(*dp[i][:12])

if dp[n][s]:
    print("Yes")
    get(n, s)
    res.reverse()
    print("".join(res))
else:
    print("No")
