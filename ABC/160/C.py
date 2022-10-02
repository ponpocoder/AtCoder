k, n = map(int, input().split())
a = list(map(int, input().split()))

idx = 0
mx = 0
for i in range(n):
    if i == 0:
        diff = a[0] + k - a[-1]
    else:
        diff = abs(a[i] - a[i-1])
    if diff > mx:
        idx = i
        mx = diff

print(k - mx)
