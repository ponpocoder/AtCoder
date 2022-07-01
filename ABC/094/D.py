n = int(input())
a = list(map(int, input().split()))
a.sort()
b = a[-1]
c = float("inf")
d = b // 2

for v in a[:-1]:
    if v == b:
        continue
    if abs(d - v) <= abs(d - c):
        c = v

print(b, c)