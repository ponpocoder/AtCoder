from math import radians, sin, cos
a, b, d = map(int, input().split())

degree = radians(d)
s = sin(degree)
c = cos(degree)

x = a * c - b * s
y = a * s + b * c

print(x, y)