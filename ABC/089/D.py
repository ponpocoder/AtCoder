import sys
sys.setrecursionlimit(10**5)

h, w, d = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]

n = h * w + 1
cost = [-1] * n

for i in range(h):
    for j in range(w):
        k = a[i][j]
        cost[k] = (i, j)

s = [0] * (n + 1)


def dfs(i):
    global n
    if i + d >= n:
        return 0
    if s[i] != 0:
        return s[i]
    x, y = cost[i]
    nx, ny = cost[i+d]
    c = abs(x - nx) + abs(y - ny)
    s[i] = c + dfs(i+d)
    return s[i]


for i in range(1, n+1):
    dfs(i)
q = int(input())
for _ in range(q):
    l, r = map(int, input().split())
    print(s[l] - s[r])
