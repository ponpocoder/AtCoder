a, b, c, d, e, f = map(int, input().split())

x1 = a - c
y1 = b - d
x2 = e - c
y2 = f - d

area = abs(x1*y2-x2*y1)/2
print(area)
