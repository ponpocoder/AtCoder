n, x, y = map(int, input().split())
x -= 1
y -= 1
res = [0] * n

for i in range(n-1):
    for j in range(i+1, n):
        dist = min(j - i, abs(x - i) + 1 +  abs(y - j), abs(x - j) + 1 + abs(y - i))
        res[dist] += 1

for re in res[1:]:
    print(re)