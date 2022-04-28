n, k, x = map(int, input().split())
a = list(map(int, input().split()))

res = 0
for i in range(n):
    if a[i] >= x and k > 0:
        macC = a[i] // x
        if k >= macC:
            a[i] -= x * macC
            k -= macC
        else:
            a[i] -= x * k
            k = 0   

a.sort(reverse=True)
for v in a:
    if k > 0 and v != 0:
        k -= 1
    else:
        res += v

print(res)
