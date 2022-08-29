n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

mx = 1001
mn = 0

for i in range(n):
    mx = min(mx, max(a[i], b[i]))
    mn = max(mn, min(a[i], b[i]))

if mx - mn >= 0:
    print(mx-mn+1)
else:
    print(0)
