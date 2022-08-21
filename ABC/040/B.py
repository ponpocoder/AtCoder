n = int(input())
res = n

if n == 1:
    print(0)
    exit()
for i in range(1, n):
    if i*i > n:
        break
    remain = n - i*i
    diff = remain//i
    remain %= i
    res = min(res, remain+diff)

print(res)
