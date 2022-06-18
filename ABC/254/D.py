n = int(input())
p = [i for i in range(n+1)]
for i in range(2, n+1):
    x = i*i
    if x > n:
        break
    for j in range(x, n+1, x):
        while p[j] % x == 0:
            p[j] //= x

cnt = [0] * (n+1)
for i in range(1, n+1):
    cnt[p[i]] += 1

res = 0
for i in range(n+1):
    res += cnt[i]*cnt[i]

print(res)