from collections import defaultdict

n = int(input())

cnt = [0] * (n+1)

dic = defaultdict(int)
array = []
for _ in range(n):
    a, b = map(int, input().split())
    array.append((a, 1))
    array.append((a+b, -1))

array.sort()

curr = 0
res = [0] * (n + 1)

for i in range(len(array) - 1):
    curr += array[i][1]
    res[curr] += array[i+1][0] - array[i][0]

print(*res[1:])