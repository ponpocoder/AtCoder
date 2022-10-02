from math import cos, pi

a, b, h, m = map(int, input().split())

x = (h + m / 60) / 12
y = m / 60

diff = abs(x-y) * 360
print(diff)
res = a**2 + b**2 - 2*a*b*cos(diff/180*pi)

print(res**0.5)
