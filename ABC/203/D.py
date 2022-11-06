n, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

x = k*k//2 + 1
l, r = -1, 10**10

while l + 1 < r:
    m = (l + r) // 2
    flag = False

    s = [[0] * (n+1) for _ in range(n+1)]
    for i in range(n):
        for j in range(n):
            s[i+1][j+1] = 1 if a[i][j] > m else 0
    for i in range(n+1):
        for j in range(n):
            s[i][j+1] += s[i][j]
    for i in range(n):
        for j in range(n+1):
            s[i+1][j] += s[i][j]
    for i in range(n-k+1):
        for j in range(n-k+1):
            curr = s[i+k][j+k]
            curr -= s[i+k][j]
            curr -= s[i][j+k]
            curr += s[i][j]
            if curr < x:
                flag = True
                break
    if flag:
        r = m
    else:
        l = m

print(r)
