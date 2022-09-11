n = int(input())
l = []
r = []
for _ in range(n):
    a, b = map(int, input().split())
    l.append(a)
    r.append(b)

l.sort()
r.sort()

res = 0
if n % 2:
    cl = l[n//2]
    cr = r[n//2]
    res = cr - cl + 1
else:
    cl = l[n//2-1] + l[n//2]
    cr = r[n//2-1] + r[n//2]
    res = cr - cl + 1

print(res)
