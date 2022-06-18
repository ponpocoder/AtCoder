n, a, b = map(int, input().split())
x = list(map(int, input().split()))
res = 0

for i in range(1, n):
    if b > a*(x[i] - x[i-1]):
        res += a*(x[i] - x[i-1])
    else:
        res += b

print(res)