n, x = map(int, input().split())
a = list(map(int, input().split()))

curr = 0
for i in range(n):
    if i % 2:
        curr += a[i]-1
    else:
        curr += a[i]

if x >= curr:
    print("Yes")
else:
    print("No")
