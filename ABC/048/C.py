n, x = map(int, input().split())
a = list(map(int, input().split()))

res = 0

for i in range(1, n):
    diff = a[i] + a[i-1] - x
    if diff > 0:
        res += diff
        if a[i] >= diff:
            a[i] -= diff
        else:
            a[i] = 0

print(res)