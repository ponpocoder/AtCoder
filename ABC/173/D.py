n = int(input())
a = list(map(int, input().split()))

a.sort(reverse=True)

res = 0
t = n-1

for i in range(n):
    lim = 1 if i==0 else 2
    for j in range(lim):
        if t > 0:
            res += a[i]
            t -= 1

print(res)