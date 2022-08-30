n = int(input())
a = list(map(int, input().split()))

res1 = 0
res2 = 0
t1 = 0
t2 = 0

for i in range(n):
    t1 += a[i]
    t2 += a[i]
    if i % 2 == 0:
        if t1 <= 0:
            res1 += 1 - t1
            t1 = 1

        if t2 >= 0:
            res2 += t2 + 1
            t2 = -1

    else:
        if t1 >= 0:
            res1 += t1 + 1
            t1 = -1
        if t2 <= 0:
            res2 += 1 - t2
            t2 = 1

print(min(res1, res2))
