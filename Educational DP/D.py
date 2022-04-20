n, w = map(int, input().split())

weights, values = [], []

for _ in range(n):
    weight, value = map(int, input().split())
    weights.append(weight)
    values.append(value)

matrix = [[0 for _ in range(w + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(w + 1):
        if j >= weights[i - 1]:
            matrix[i][j] = max(matrix[i - 1][j], matrix[i - 1][j - weights[i - 1]] + values[i - 1])
        else:
            matrix[i][j] = matrix[i - 1][j]

print(max(matrix[-1]))