n = int(input())
a = list(map(int, input().split()))

x = [0] * n
y = [0] * n

for i in range(n):
    cnt = 0
    while a[i] % 2 == 0:
        cnt += 1
        a[i] //= 2
    x[i] = cnt
    curr = a[i]
    cnt = 0
    while a[i] % 3 == 0:
        cnt += 1
        a[i] //= 3
    y[i] = cnt

res = 0
minX = min(x)
minY = min(y)

for i in range(1, n):
    if a[i] != a[i-1]:
        print(-1)
        exit()

for i in range(n):
    res += x[i] - minX
    res += y[i] - minY

print(res)
