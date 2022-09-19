h, w = map(int, input().split())
array = []
for _ in range(h):
    row = list(map(int, input().split()))
    array.append(row)

rowSums = [0] * h
colSums = [0] * w

for row in range(h):
    rowSum = 0
    for col in range(w):
        rowSum += array[row][col]
    
    rowSums[row] = rowSum

for col in range(w):
    colSum = 0
    for row in range(h):
        colSum += array[row][col]
    
    colSums[col] = colSum

for row in range(h):
    for col in range(w):
        array[row][col] = rowSums[row] + colSums[col] - array[row][col]

for i in range(h):
  print(*array[i])