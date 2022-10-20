n = int(input())

x, y = -1, -1
res = 10**13
for i in range(1, n+1):
    if i*i > n:
        break
    if n % i == 0:
        res = min(res, i+n//i-2)

print(res)
