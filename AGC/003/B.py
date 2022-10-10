n = int(input())
a = []
for _ in range(n):
    x = int(input())
    a.append(x)

cnt = 0

for i in range(n):
    cnt += a[i] // 2
    if i < n - 1 and a[i] % 2 and a[i+1] > 0:
        cnt += 1
        a[i+1] -= 1

print(cnt)
