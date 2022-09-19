from math import sin, cos, hypot, pi, atan2

t = int(input())
l, X, Y = map(int, input().split())

q = int(input())
for _ in range(q):
    e = int(input())
    y = -sin(e*2*pi / t) * (l / 2)
    z = -cos(e*2*pi / t) * (l / 2) + l / 2
    d = hypot(X, Y - y)
    angle = atan2(z, d)
    print(angle * 180 / pi)
