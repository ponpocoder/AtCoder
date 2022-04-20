n, x = map(int, input().split())
matrix = [[False for _ in range(10001)] for _ in range(n + 1)]
matrix[0][0] = True
idx1 = 0
idx2 = 0

for i in range(1,n + 1):
    a, b = map(int, input().split())
    for j in range(x):
        if matrix[i - 1][j]:
            matrix[i][j + a] = matrix[i - 1][j]
            matrix[i][j + b] = matrix[i - 1][j]

if matrix[n][x]:
    print("Yes")
else:
    print("No")