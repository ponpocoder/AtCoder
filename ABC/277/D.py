n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
a += a
n2 = 2*n
l = 0
r = 0
s = 0
while r < n2:
    curr = a[r]
    while r < n2 - 1 and ((a[r] % m == a[r+1] % m) or a[r] % m == (a[r+1]-1) % m):
        curr += a[r+1]
        r += 1
    s = max(s, curr)

    if l == r:
        r += 1
    l = r

res = max(0, sum(a)//2 - s)
print(res)
