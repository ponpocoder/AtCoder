n, l, r = map(int, input().split())
a = list(map(int, input().split()))

lsum = [0] * n
lsum[0] = l - a[0]

for i in range(1, n):
    lsum[i] = lsum[i-1] - (a[i] - l)

idx = -1
curr = 0
for i in range(n):
    if lsum[i] < curr:
        curr = lsum[i]
        idx = i

for i in range(idx+1):
    a[i] = l

rsum = [0] * n
rsum[n-1] = r - a[n-1]

for i in range(n-2, -1, -1):
    rsum[i] = rsum[i+1] - (a[i] - r)

idx = n
curr = 0
for i in range(n):
    if rsum[i] < curr:
        curr = rsum[i]
        idx = i
for i in range(n-1, idx-1, -1):
    a[i] = r

print(lsum)
print(rsum)
print(sum(a))
