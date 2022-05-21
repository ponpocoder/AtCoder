n, k = map(int, input().split())
a = list(map(int, input().split()))

x = 0

#mi key:余り value:Index
#mx key:余り value:アメの個数
mi, mx = {}, {}
for i in range(k):
    r = x % n
    if r in mi:
        p = i - mi[r]
        if (k - i) % p == 0:
            x += (x -mx[r]) * (k - i) // p
            break
    mi[r] = i
    mx[r] = x
    x += a[x%n]

print(x)