from math import cos, sin, pi

n = int(input())
x0, y0 = map(int, input().split())
xn, yn = map(int, input().split())
ox, oy = (x0 + xn) / 2, (y0 + yn) / 2

x1 = cos(2 * pi / n) *(x0 - ox) - sin(2 * pi / n) * (y0 - oy) + ox
y1 = sin(2 * pi / n) *(x0 - ox) + cos(2 * pi / n) * (y0 - oy) + oy

print(x1, y1)