n = int(input())
f = [list(map(int, input().split())) for _ in range(n)]
p = [list(map(int, input().split())) for _ in range(n)]

res = float("-inf")

for i in range(1, 1<<10):
    q = [0] * n
    for j in range(10):
        if i & (1 << j):
            for k in range(n):
                q[k] += f[k][j]
    curr = 0
    for i in range(n):
        curr += p[i][q[i]]

    res = max(res, curr)

print(res)