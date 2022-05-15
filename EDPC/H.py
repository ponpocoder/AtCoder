h, w = map(int, input().split())
matrix = []
for i in range(h):
    row = input()
    matrix.append(row)

result = [[0 for _ in range(w)] for _ in range(h)]
if matrix[0][0] == ".":
    result[0][0] = 1
else:
    result[0][0] = 0

for c in range(1, w):
    if matrix[0][c] == ".":
        result[0][c] = result[0][c - 1]
    else:
        result[0][c] = 0

for r in range(1, h):
    for c in range(w):
        if matrix[r][c] == "#":
            result[r][c] = 0
        else:
            if c == 0:
                result[r][c] = result[r - 1][c]
            else:
                result[r][c] = result[r - 1][c] + result[r][c - 1]

mod = 10**9 + 7
print(result[h - 1][w - 1] % mod)