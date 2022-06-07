import math
a, b, x = map(int, input().split())

if x < a*a*b//2:
    y = 2*x/(a*b)
    res = math.degrees(math.atan(b/y))
else:
    y = 2*x/(a**2) - b
    res = math.degrees(math.atan((b-y)/a))

print(res)